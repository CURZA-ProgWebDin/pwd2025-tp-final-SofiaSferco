from flask import Blueprint, jsonify, request as solicitud

from backend.controllers import factura


blueprint_rutas = Blueprint("facturas", __name__, url_prefix="/api/facturas")


@blueprint_rutas.get("")
def listar_elementos():
    cuerpo, estado_http = factura.listar_facturas(solicitud.args.get("sin_pago"))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.get("/<int:id_elemento>")
def obtener_elemento(id_elemento):
    cuerpo, estado_http = factura.obtener_factura(id_elemento)
    return jsonify(cuerpo), estado_http


@blueprint_rutas.post("")
def crear_elemento():
    cuerpo, estado_http = factura.crear_factura(solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.put("/<int:id_elemento>")
def actualizar_elemento(id_elemento):
    cuerpo, estado_http = factura.actualizar_factura(id_elemento, solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.delete("/<int:id_elemento>")
def eliminar_elemento(id_elemento):
    cuerpo, estado_http = factura.eliminar_factura(id_elemento)
    return jsonify(cuerpo), estado_http
