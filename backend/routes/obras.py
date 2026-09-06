from flask import Blueprint, jsonify, request as solicitud

from backend.controllers import obra


blueprint_rutas = Blueprint("obras", __name__, url_prefix="/api/obras")


@blueprint_rutas.get("")
def listar_elementos():
    cuerpo, estado_http = obra.listar_obras(solicitud.args.get("estado_ejecucion"), solicitud.args.get("con_saldo_por_facturar"))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.get("/<int:id_elemento>")
def obtener_elemento(id_elemento):
    cuerpo, estado_http = obra.obtener_obra(id_elemento)
    return jsonify(cuerpo), estado_http


@blueprint_rutas.post("")
def crear_elemento():
    cuerpo, estado_http = obra.crear_obra(solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.put("/<int:id_elemento>")
def actualizar_elemento(id_elemento):
    cuerpo, estado_http = obra.actualizar_obra(id_elemento, solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.patch("/<int:id_elemento>")
def actualizar_seguimiento_elemento(id_elemento):
    cuerpo, estado_http = obra.actualizar_seguimiento_obra(id_elemento, solicitud.get_json(silent=True))
    return jsonify(cuerpo), estado_http


@blueprint_rutas.delete("/<int:id_elemento>")
def eliminar_elemento(id_elemento):
    cuerpo, estado_http = obra.eliminar_obra(id_elemento)
    return jsonify(cuerpo), estado_http
