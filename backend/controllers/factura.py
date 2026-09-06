from psycopg.errors import UniqueViolation

from backend.controllers.comun import respuesta_factura
from backend.database import obtener_conexion
from backend.models import factura as modelo
from backend.models import obra as modelo_obra
from backend.utils.errores import ErrorApi
from backend.utils.validacion import id_entero, texto_opcional, importe_positivo, texto_obligatorio, requerir_objeto_json, filtro_verdadero, fecha_valida


def _validar(contenido, creando):
    datos = requerir_objeto_json(contenido)
    resultado = {
        "numero_factura": texto_obligatorio(datos, "numero_factura", "El número de factura"),
        "fecha_emision": fecha_valida(datos, "fecha_emision"),
        "importe": importe_positivo(datos, "importe", "El importe"),
        "observaciones": texto_opcional(datos, "observaciones"),
    }
    if creando:
        resultado["id_obra"] = id_entero(datos, "id_obra")
    return resultado


def listar_facturas(sin_pago=None):
    solo_sin = filtro_verdadero(sin_pago, "sin_pago")
    conexion = obtener_conexion()
    try:
        return {"data": [respuesta_factura(fila) for fila in modelo.listar_todos(conexion, solo_sin)]}, 200
    finally:
        conexion.close()


def obtener_factura(factura_id):
    conexion = obtener_conexion()
    try:
        fila = modelo.obtener_por_id(conexion, factura_id)
        if not fila:
            raise ErrorApi("Factura no encontrada", 404)
        return {"data": respuesta_factura(fila)}, 200
    finally:
        conexion.close()


def crear_factura(contenido):
    datos = _validar(contenido, True)
    conexion = obtener_conexion()
    try:
        obra = modelo_obra.obtener_por_id(conexion, datos["id_obra"], para_actualizar=True)
        if not obra:
            raise ErrorApi("Obra no encontrada", 404)
        if modelo.obtener_por_numero(conexion, datos["numero_factura"]):
            raise ErrorApi("Ya existe una factura con el número indicado.", 409)
        total = modelo.total_por_obra(conexion, datos["id_obra"]) + datos["importe"]
        if total > obra["monto_contratado"]:
            raise ErrorApi("No se puede registrar la factura porque el monto total facturado excede el monto contratado de la obra.", 409)
        factura_id = modelo.crear(conexion, datos)
        fila = modelo.obtener_por_id(conexion, factura_id)
        conexion.commit()
        return {"message": "Factura creada correctamente", "data": respuesta_factura(fila)}, 201
    except UniqueViolation as error:
        conexion.rollback()
        raise ErrorApi("Ya existe una factura con el número indicado.", 409) from error
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_factura(factura_id, contenido):
    datos = _validar(contenido, False)
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, factura_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Factura no encontrada", 404)
        if actual["tiene_pago"]:
            raise ErrorApi("La factura no puede modificarse porque tiene un pago asociado.", 409)
        obra = modelo_obra.obtener_por_id(conexion, actual["id_obra"], para_actualizar=True)
        if modelo.obtener_por_numero(conexion, datos["numero_factura"], id_excluido=factura_id):
            raise ErrorApi("Ya existe una factura con el número indicado.", 409)
        total = modelo.total_por_obra(conexion, actual["id_obra"], id_excluido=factura_id) + datos["importe"]
        if total > obra["monto_contratado"]:
            raise ErrorApi("No se puede modificar la factura porque el monto total facturado excede el monto contratado de la obra.", 409)
        modelo.actualizar(conexion, factura_id, datos)
        fila = modelo.obtener_por_id(conexion, factura_id)
        conexion.commit()
        return {"message": "Factura modificada correctamente", "data": respuesta_factura(fila)}, 200
    except UniqueViolation as error:
        conexion.rollback()
        raise ErrorApi("Ya existe una factura con el número indicado.", 409) from error
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_factura(factura_id):
    conexion = obtener_conexion()
    try:
        actual = modelo.obtener_por_id(conexion, factura_id, para_actualizar=True)
        if not actual:
            raise ErrorApi("Factura no encontrada", 404)
        if actual["tiene_pago"]:
            raise ErrorApi("La factura no puede eliminarse porque tiene un pago asociado.", 409)
        modelo.eliminar(conexion, factura_id)
        conexion.commit()
        return {"message": "Factura eliminada correctamente"}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
