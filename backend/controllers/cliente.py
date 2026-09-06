import re

from psycopg.errors import UniqueViolation

from backend.database import obtener_conexion
from backend.models import cliente as modelo
from backend.utils.errores import ErrorApi
from backend.utils.serializacion import serializar
from backend.utils.validacion import texto_opcional, texto_obligatorio, requerir_objeto_json


def _validar(datos):
    datos = requerir_objeto_json(datos)
    cuit_original = datos.get("cuit_cuil")
    if not isinstance(cuit_original, str):
        raise ErrorApi("El CUIT/CUIL es obligatorio.", 400)
    cuit = re.sub(r"[\s-]", "", cuit_original)
    if not re.fullmatch(r"\d{11}", cuit):
        raise ErrorApi("El CUIT/CUIL debe contener exactamente 11 dígitos.", 400)
    telefono = texto_opcional(datos, "telefono")
    if telefono and not telefono.isdigit():
        raise ErrorApi("El teléfono debe contener únicamente números.", 400)
    email = texto_opcional(datos, "email")
    if email and not re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email):
        raise ErrorApi("El email no tiene un formato válido.", 400)
    return {
        "cuit_cuil": cuit,
        "razon_social": texto_obligatorio(datos, "razon_social", "La razón social"),
        "responsable": texto_opcional(datos, "responsable"),
        "telefono": telefono,
        "email": email,
    }


def listar_clientes():
    conexion = obtener_conexion()
    try:
        return {"data": serializar(modelo.listar_todos(conexion))}, 200
    finally:
        conexion.close()


def obtener_cliente(cliente_id):
    conexion = obtener_conexion()
    try:
        fila = modelo.obtener_por_id(conexion, cliente_id)
        if not fila:
            raise ErrorApi("Cliente no encontrado", 404)
        return {"data": serializar(fila)}, 200
    finally:
        conexion.close()


def crear_cliente(contenido):
    datos = _validar(contenido)
    conexion = obtener_conexion()
    try:
        if modelo.obtener_por_cuit(conexion, datos["cuit_cuil"]):
            raise ErrorApi("Ya existe un cliente con el CUIT/CUIL indicado.", 409)
        fila = modelo.crear(conexion, datos)
        conexion.commit()
        return {"message": "Cliente creado correctamente", "data": serializar(fila)}, 201
    except UniqueViolation as error:
        conexion.rollback()
        raise ErrorApi("Ya existe un cliente con el CUIT/CUIL indicado.", 409) from error
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def actualizar_cliente(cliente_id, contenido):
    datos = _validar(contenido)
    conexion = obtener_conexion()
    try:
        if not modelo.obtener_por_id(conexion, cliente_id, para_actualizar=True):
            raise ErrorApi("Cliente no encontrado", 404)
        if modelo.obtener_por_cuit(conexion, datos["cuit_cuil"], id_excluido=cliente_id):
            raise ErrorApi("Ya existe un cliente con el CUIT/CUIL indicado.", 409)
        fila = modelo.actualizar(conexion, cliente_id, datos)
        conexion.commit()
        return {"message": "Cliente modificado correctamente", "data": serializar(fila)}, 200
    except UniqueViolation as error:
        conexion.rollback()
        raise ErrorApi("Ya existe un cliente con el CUIT/CUIL indicado.", 409) from error
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()


def eliminar_cliente(cliente_id):
    conexion = obtener_conexion()
    try:
        if not modelo.obtener_por_id(conexion, cliente_id, para_actualizar=True):
            raise ErrorApi("Cliente no encontrado", 404)
        if modelo.tiene_cotizaciones(conexion, cliente_id):
            raise ErrorApi("El cliente no puede eliminarse porque tiene cotizaciones asociadas.", 409)
        modelo.eliminar(conexion, cliente_id)
        conexion.commit()
        return {"message": "Cliente eliminado correctamente"}, 200
    except Exception:
        conexion.rollback()
        raise
    finally:
        conexion.close()
