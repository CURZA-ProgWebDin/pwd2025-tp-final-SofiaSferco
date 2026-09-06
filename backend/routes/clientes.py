from flask import Blueprint, jsonify, request as solicitud

from backend.controllers import cliente


blueprint_rutas = Blueprint("clientes", __name__, url_prefix="/api/clientes")


@blueprint_rutas.get("")
def listar_elementos():
    cuerpo, estado_http = cliente.listar_clientes()
    return jsonify(cuerpo), estado_http


@blueprint_rutas.get("/<int:id_elemento>")
def obtener_elemento(id_elemento):
    cuerpo, estado_http = cliente.obtener_cliente(id_elemento)
    return jsonify(cuerpo), estado_http


@blueprint_rutas.post("")
def crear_elemento():
    cuerpo, estado_http = cliente.crear_cliente(solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.put("/<int:id_elemento>")
def actualizar_elemento(id_elemento):
    cuerpo, estado_http = cliente.actualizar_cliente(id_elemento, solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.delete("/<int:id_elemento>")
def eliminar_elemento(id_elemento):
    cuerpo, estado_http = cliente.eliminar_cliente(id_elemento)
    return jsonify(cuerpo), estado_http
