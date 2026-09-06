from datetime import date

from backend.controllers.comun import respuesta_obra
from backend.database import obtener_conexion
from backend.models import cotizacion as modelo_cotizacion
from backend.models import obra as modelo
from backend.utils.errores import ErrorApi
from backend.utils.validacion import valor_permitido, id_entero, texto_opcional, importe_positivo, texto_obligatorio, requerir_objeto_json, filtro_verdadero, fecha_valida


ESTADOS = {"Pendiente", "En ejecución", "Finalizada", "Suspendida", "Cancelada"}
TIPOS_DOCUMENTO = {"Contrato", "Orden de compra", "Pedido de compra", "Resolución", "Otros"}
CAMPOS_SEGUIMIENTO = {"estado_ejecucion", "fecha_inicio", "fecha_fin", "motivo_estado"}


def _documento(datos):
    tipo = texto_opcional(datos, "tipo_documento")
    numero = texto_opcional(datos, "numero_documento")
    fecha_documento = fecha_valida(datos, "fecha_documento", required=False)
    valores = (tipo, numero, fecha_documento)
    if any(valores) and not all(valores):
        raise ErrorApi("Los tres datos del documento contractual deben completarse juntos.", 400)
    if tipo and tipo not in TIPOS_DOCUMENTO:
        raise ErrorApi("tipo_documento no contiene un valor permitido.", 400)
    return tipo, numero, fecha_documento


def _validar_estado(datos):
    estado = datos["estado_ejecucion"]
    inicio, fin, motivo = datos["fecha_inicio"], datos["fecha_fin"], datos["motivo_estado"]
    if estado == "Pendiente" and (inicio or fin):
        raise ErrorApi("Una obra Pendiente no puede tener fecha de inicio ni de finalización.", 400)
    if estado in {"En ejecución", "Finalizada", "Suspendida"} and not inicio:
        raise ErrorApi(f"El estado {estado} requiere fecha de inicio.", 400)
    if estado == "Finalizada" and not fin:
        raise ErrorApi("El estado Finalizada requiere fecha de finalización.", 400)
    if fin and estado != "Finalizada":
        raise ErrorApi("Si se informa fecha de finalización, el estado debe ser Finalizada.", 400)
    if inicio and fin and fin < inicio:
        raise ErrorApi("La fecha de finalización no puede ser anterior a la fecha de inicio.", 400)
    if estado in {"Suspendida", "Cancelada"} and not motivo:
        raise ErrorApi(f"El estado {estado} requiere un motivo.", 400)


def _datos_generales(contenido):
    datos = requerir_objeto_json(contenido)
    tipo, numero, fecha_documento = _documento(datos)
    resultado = {
        "titulo": texto_obligatorio(datos, "titulo", "El título"),
        "fecha_inicio": fecha_valida(datos, "fecha_inicio", False),
        "fecha_estimada_fin": fecha_valida(datos, "fecha_estimada_fin", False),
        "fecha_fin": fecha_valida(datos, "fecha_fin", False),
        "monto_contratado": importe_positivo(datos, "monto_contratado", "El monto contratado"),
        "estado_ejecucion": valor_permitido(datos, "estado_ejecucion", ESTADOS),
        "tipo_documento": tipo,
        "numero_documento": numero,
        "fecha_documento": fecha_documento,
        "motivo_estado": texto_opcional(datos, "motivo_estado"),
    }
    _validar_estado(resultado)
    return resultado


def listar_obras(estado_ejecucion=None, con_saldo=None):
    if estado_ejecucion and estado_ejecucion not in ESTADOS:
        raise ErrorApi("estado_ejecucion no contiene un valor permitido.", 400)
    solo_con_saldo = filtro_verdadero(con_saldo, "con_saldo_por_facturar")
    conexion = obtener_conexion()
    try:
        return {"data": [respuesta_obra(fila) for fila in modelo.listar_todos(conexion, estado_ejecucion, solo_con_saldo)]}, 200
    finally:
        conexion.close()


def obtener_obra(obra_id):
    conexion = obtener_conexion()
    try:
        fila = modelo.obtener_por_id(conexion, obra_id)
        if not fila:
            raise ErrorApi("Obra no encontrada", 404)
        return {"data": respuesta_obra(fila)}, 200
    finally:
        conexion.close()


def crear_obra(contenido):
    datos_originales = requerir_objeto_json(contenido)
    prohibidos = [campo for campo in ("fecha_inicio", "fecha_fin", "motivo_estado") if datos_originales.get(campo) not in (None, "")]
    if prohibidos:
        raise ErrorApi("Una obra nueva no admite fecha de inicio, fecha de finalización ni motivo de estado.", 400)
    tipo, numero, fecha_documento = _documento(datos_originales)
    datos = {
        "id_cotizacion": id_entero(datos_originales, "id_cotizacion"),
        "titulo": texto_obligatorio(datos_originales, "titulo", "El título"),
        "monto_contratado": importe_positivo(datos_originales, "monto_contratado", "El monto contratado"),
        "fecha_estimada_fin": fecha_valida(datos_originales, "fecha_estimada_fin", False),
        "tipo_documento": tipo,
        "numero_documento": numero,
        "fecha_documento": fecha_documento,
    }
    conexion = obtener_conexion()
    try:
        cotizacion = modelo_cotizacion.obtener_por_id(conexion, datos["id_cotizacion"], para_actualizar=True)
        if not cotizacion:
            raise ErrorApi("Cotización no encontrada", 404)
        if cotizacion["estado"] != "Aceptada":
            raise ErrorApi("La cotización debe estar Aceptada para originar una obra.", 409)
        if cotizacion["tiene_obra"]:
            raise ErrorApi("La cotización ya tiene una obra asociada.", 409)
        obra_id = modelo.crear(conexion, datos, date.today().year)
        fila = modelo.obtener_por_id(conexion, obra_id)
        conexion.commit()
        return {"message": "Obra creada correctamente", "data": respuesta_obra(fila)}, 201
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_obra(obra_id, contenido):
    datos = _datos_generales(contenido)
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, obra_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Obra no encontrada", 404)
        if actual["tiene_facturas"]:
            raise ErrorApi("La obra no puede modificarse de forma general porque tiene facturas asociadas.", 409)
        modelo.actualizar(conexion, obra_id, datos)
        fila = modelo.obtener_por_id(conexion, obra_id)
        conexion.commit()
        return {"message": "Obra modificada correctamente", "data": respuesta_obra(fila)}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_seguimiento_obra(obra_id, contenido):
    cambios = requerir_objeto_json(contenido)
    if not cambios or any(campo not in CAMPOS_SEGUIMIENTO for campo in cambios):
        raise ErrorApi("PATCH solo admite campos de seguimiento de ejecución.", 400)
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, obra_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Obra no encontrada", 404)
        resultado = {
            "estado_ejecucion": actual["estado_ejecucion"],
            "fecha_inicio": actual["fecha_inicio"],
            "fecha_fin": actual["fecha_fin"],
            "motivo_estado": actual["motivo_estado"],
        }
        if "estado_ejecucion" in cambios:
            resultado["estado_ejecucion"] = valor_permitido(cambios, "estado_ejecucion", ESTADOS)
        for campo in ("fecha_inicio", "fecha_fin"):
            if campo in cambios:
                resultado[campo] = fecha_valida(cambios, campo, False)
        if "motivo_estado" in cambios:
            resultado["motivo_estado"] = texto_opcional(cambios, "motivo_estado")
        _validar_estado(resultado)
        modelo.actualizar_seguimiento(conexion, obra_id, resultado)
        fila = modelo.obtener_por_id(conexion, obra_id)
        conexion.commit()
        return {"message": "Seguimiento de obra modificado correctamente", "data": respuesta_obra(fila)}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_obra(obra_id):
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, obra_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Obra no encontrada", 404)
        if actual["tiene_facturas"]:
            raise ErrorApi("La obra no puede eliminarse porque tiene facturas asociadas.", 409)
        modelo.eliminar(conexion, obra_id)
        conexion.commit()
        return {"message": "Obra eliminada correctamente"}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
