from flask import Blueprint, jsonify, request as solicitud

from backend.controllers import cotizacion


blueprint_rutas = Blueprint("cotizaciones", __name__, url_prefix="/api/cotizaciones")


@blueprint_rutas.get("")
def listar_elementos():
    cuerpo, estado_http = cotizacion.listar_cotizaciones(solicitud.args.get("estado"), solicitud.args.get("sin_obra"))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.get("/<int:id_elemento>")
def obtener_elemento(id_elemento):
    cuerpo, estado_http = cotizacion.obtener_cotizacion(id_elemento)
    return jsonify(cuerpo), estado_http


@blueprint_rutas.post("")
def crear_elemento():
    cuerpo, estado_http = cotizacion.crear_cotizacion(solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.put("/<int:id_elemento>")
def actualizar_elemento(id_elemento):
    cuerpo, estado_http = cotizacion.actualizar_cotizacion(id_elemento, solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.delete("/<int:id_elemento>")
def eliminar_elemento(id_elemento):
    cuerpo, estado_http = cotizacion.eliminar_cotizacion(id_elemento)
    return jsonify(cuerpo), estado_http
