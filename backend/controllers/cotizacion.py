from datetime import date

from backend.database import obtener_conexion
from backend.models import cliente as modelo_cliente
from backend.models import cotizacion as modelo
from backend.utils.errores import ErrorApi
from backend.utils.serializacion import serializar
from backend.utils.validacion import valor_permitido, id_entero, texto_opcional, importe_positivo, texto_obligatorio, requerir_objeto_json, filtro_verdadero, fecha_valida


TIPOS = {"Presupuesto", "Licitación pública", "Licitación privada", "Concurso de precios", "Compra directa"}
ESTADOS = {"Presentada", "Aceptada", "Rechazada"}


def _validar(contenido, creando):
    datos = requerir_objeto_json(contenido)
    resultado = {
        "id_cliente": id_entero(datos, "id_cliente", "id_cliente"),
        "tipo_cotizacion": valor_permitido(datos, "tipo_cotizacion", TIPOS),
        "numero_contratacion": texto_opcional(datos, "numero_contratacion"),
        "titulo": texto_obligatorio(datos, "titulo", "El título"),
        "fecha": fecha_valida(datos, "fecha"),
        "monto": importe_positivo(datos, "monto", "El monto"),
    }
    if resultado["tipo_cotizacion"] != "Presupuesto" and not resultado["numero_contratacion"]:
        raise ErrorApi("El número de contratación es obligatorio para el tipo seleccionado.", 400)
    if not creando:
        resultado["estado"] = valor_permitido(datos, "estado", ESTADOS)
    return resultado


def listar_cotizaciones(estado=None, sin_obra=None):
    if estado and estado not in ESTADOS:
        raise ErrorApi("estado no contiene un valor permitido.", 400)
    solo_sin = filtro_verdadero(sin_obra, "sin_obra")
    conexion = obtener_conexion()
    try:
        return {"data": serializar(modelo.listar_todos(conexion, estado, solo_sin))}, 200
    finally:
        conexion.close()


def obtener_cotizacion(cotizacion_id):
    conexion = obtener_conexion()
    try:
        fila = modelo.obtener_por_id(conexion, cotizacion_id)
        if not fila:
            raise ErrorApi("Cotización no encontrada", 404)
        return {"data": serializar(fila)}, 200
    finally:
        conexion.close()


def crear_cotizacion(contenido):
    datos = _validar(contenido, True)
    conexion = obtener_conexion()
    try:
        if not modelo_cliente.obtener_por_id(conexion, datos["id_cliente"], para_actualizar=True):
            raise ErrorApi("Cliente no encontrado", 404)
        id_elemento = modelo.crear(conexion, datos, date.today().year)
        fila = modelo.obtener_por_id(conexion, id_elemento)
        conexion.commit()
        return {"message": "Cotización creada correctamente", "data": serializar(fila)}, 201
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_cotizacion(cotizacion_id, contenido):
    datos = _validar(contenido, False)
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, cotizacion_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Cotización no encontrada", 404)
        if actual["tiene_obra"]:
            raise ErrorApi("La cotización no puede modificarse porque ya tiene una obra asociada.", 409)
        if not modelo_cliente.obtener_por_id(conexion, datos["id_cliente"], para_actualizar=True):
            raise ErrorApi("Cliente no encontrado", 404)
        modelo.actualizar(conexion, cotizacion_id, datos)
        fila = modelo.obtener_por_id(conexion, cotizacion_id)
        conexion.commit()
        return {"message": "Cotización modificada correctamente", "data": serializar(fila)}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_cotizacion(cotizacion_id):
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, cotizacion_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Cotización no encontrada", 404)
        if actual["tiene_obra"]:
            raise ErrorApi("La cotización no puede eliminarse porque tiene una obra asociada.", 409)
        modelo.eliminar(conexion, cotizacion_id)
        conexion.commit()
        return {"message": "Cotización eliminada correctamente"}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
