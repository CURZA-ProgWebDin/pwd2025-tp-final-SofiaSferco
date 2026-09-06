from flask import Blueprint, jsonify, request as solicitud

from backend.controllers import pago


blueprint_rutas = Blueprint("pagos", __name__, url_prefix="/api/pagos")


@blueprint_rutas.get("")
def listar_elementos():
    cuerpo, estado_http = pago.listar_pagos()
    return jsonify(cuerpo), estado_http


@blueprint_rutas.get("/<int:id_elemento>")
def obtener_elemento(id_elemento):
    cuerpo, estado_http = pago.obtener_pago(id_elemento)
    return jsonify(cuerpo), estado_http


@blueprint_rutas.post("")
def crear_elemento():
    cuerpo, estado_http = pago.crear_pago(solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.delete("/<int:id_elemento>")
def eliminar_elemento(id_elemento):
    cuerpo, estado_http = pago.eliminar_pago(id_elemento)
    return jsonify(cuerpo), estado_http
