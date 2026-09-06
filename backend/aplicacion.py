import logging

from flask import Flask, jsonify
from flask_cors import CORS

from backend.config import Configuracion
from backend.routes import registrar_blueprints
from backend.utils.errores import ErrorApi


def crear_aplicacion(configuracion_prueba=None):
    aplicacion = Flask(__name__)
    aplicacion.config.from_object(Configuracion)
    if configuracion_prueba:
        aplicacion.config.update(configuracion_prueba)
    CORS(aplicacion)
    registrar_blueprints(aplicacion)

    @aplicacion.errorhandler(ErrorApi)
    def manejar_error_api(error):
        return jsonify(error=error.mensaje), error.status_code

    @aplicacion.errorhandler(404)
    def manejar_ruta_desconocida(_error):
        return jsonify(error="Recurso no encontrado"), 404

    @aplicacion.errorhandler(405)
    def manejar_metodo_no_permitido(_error):
        return jsonify(error="Método no permitido"), 405

    @aplicacion.errorhandler(Exception)
    def manejar_error_inesperado(error):
        aplicacion.logger.exception("Error inesperado de la API", exc_info=error)
        return jsonify(error="Ocurrió un error interno. Intente nuevamente."), 500

    return aplicacion


aplicacion = crear_aplicacion()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    aplicacion.run(debug=False)
