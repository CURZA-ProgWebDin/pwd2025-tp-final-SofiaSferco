from backend.database import obtener_conexion
from backend.models import factura as modelo_factura
from backend.models import obra as modelo_obra
from backend.models import pago as modelo
from backend.utils.errores import ErrorApi
from backend.utils.serializacion import serializar
from backend.utils.validacion import valor_permitido, id_entero, texto_opcional, importe_positivo, requerir_objeto_json, fecha_valida


MEDIOS_PAGO = {"Transferencia", "Efectivo", "Cheque", "Echeq", "Otros"}
ADVERTENCIA = "Pago registrado correctamente. La obra se encuentra totalmente cobrada. Si la obra ya finalizó, recuerde cambiar su estado a Finalizada e indicar la fecha de finalización."


def _validar(contenido):
    datos = requerir_objeto_json(contenido)
    resultado = {
        "id_factura": id_entero(datos, "id_factura"),
        "fecha_pago": fecha_valida(datos, "fecha_pago"),
        "importe": importe_positivo(datos, "importe", "El importe"),
        "medio_pago": valor_permitido(datos, "medio_pago", MEDIOS_PAGO),
        "observaciones": texto_opcional(datos, "observaciones"),
    }
    if resultado["medio_pago"] == "Otros" and not resultado["observaciones"]:
        raise ErrorApi("Las observaciones son obligatorias cuando el medio de pago es Otros.", 400)
    return resultado


def listar_pagos():
    conexion = obtener_conexion()
    try:
        return {"data": serializar(modelo.listar_todos(conexion))}, 200
    finally:
        conexion.close()


def obtener_pago(pago_id):
    conexion = obtener_conexion()
    try:
        fila = modelo.obtener_por_id(conexion, pago_id)
        if not fila:
            raise ErrorApi("Pago no encontrado", 404)
        return {"data": serializar(fila)}, 200
    finally:
        conexion.close()


def crear_pago(contenido):
    datos = _validar(contenido)
    conexion = obtener_conexion()
    try:
        factura = modelo_factura.obtener_por_id(conexion, datos["id_factura"], para_actualizar=True)
        if not factura:
            raise ErrorApi("Factura no encontrada", 404)
        if factura["tiene_pago"]:
            raise ErrorApi("Ya existe un pago registrado para esta factura.", 409)
        if datos["importe"] != factura["importe"]:
            raise ErrorApi("El importe del pago debe coincidir con el importe total de la factura.", 409)
        modelo_obra.obtener_por_id(conexion, factura["id_obra"], para_actualizar=True)
        pago_id = modelo.crear(conexion, datos)
        fila = modelo.obtener_por_id(conexion, pago_id)
        obra = modelo_obra.obtener_por_id(conexion, factura["id_obra"])
        mensaje = "Pago registrado correctamente"
        if obra["total_cobrado"] == obra["monto_contratado"] and obra["estado_ejecucion"] != "Finalizada":
            mensaje = ADVERTENCIA
        conexion.commit()
        return {"message": mensaje, "data": serializar(fila)}, 201
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_pago(pago_id):
    conexion = obtener_conexion()
    try:
        if not modelo.eliminar(conexion, pago_id):
            raise ErrorApi("Pago no encontrado", 404)
        conexion.commit()
        return {"message": "Pago eliminado correctamente"}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
