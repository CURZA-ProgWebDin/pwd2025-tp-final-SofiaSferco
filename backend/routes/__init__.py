from .clientes import blueprint_rutas as blueprint_clientes
from .cotizaciones import blueprint_rutas as blueprint_cotizaciones
from .facturas import blueprint_rutas as blueprint_facturas
from .obras import blueprint_rutas as blueprint_obras
from .pagos import blueprint_rutas as blueprint_pagos


def registrar_blueprints(aplicacion):
    for blueprint_rutas in (
        blueprint_clientes,
        blueprint_cotizaciones,
        blueprint_obras,
        blueprint_facturas,
        blueprint_pagos,
    ):
        aplicacion.register_blueprint(blueprint_rutas)
