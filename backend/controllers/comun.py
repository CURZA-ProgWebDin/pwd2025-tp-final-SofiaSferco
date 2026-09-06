from decimal import Decimal

from backend.utils.serializacion import serializar


def campos_derivados_obra(monto_contratado, total_facturado=0, total_cobrado=0):
    contratado = Decimal(str(monto_contratado))
    facturado = Decimal(str(total_facturado or 0))
    cobrado = Decimal(str(total_cobrado or 0))

    if facturado == 0:
        estado_facturacion = "Sin facturar"
    elif facturado < contratado:
        estado_facturacion = "Facturada parcialmente"
    else:
        estado_facturacion = "Facturada totalmente"

    if cobrado == 0:
        estado_cobro = "Adeudada"
    elif cobrado < contratado:
        estado_cobro = "Pagada parcialmente"
    else:
        estado_cobro = "Pagada"

    return {
        "total_facturado": facturado,
        "saldo_por_facturar": contratado - facturado,
        "estado_facturacion": estado_facturacion,
        "total_cobrado": cobrado,
        "saldo_por_cobrar": contratado - cobrado,
        "estado_cobro": estado_cobro,
    }


def respuesta_obra(fila):
    if not fila:
        return None
    resultado = dict(fila)
    resultado.update(
        campos_derivados_obra(
            resultado["monto_contratado"],
            resultado.pop("total_facturado", 0),
            resultado.pop("total_cobrado", 0),
        )
    )
    return serializar(resultado)


def respuesta_factura(fila):
    if not fila:
        return None
    resultado = dict(fila)
    resultado["estado_pago"] = "Pagada" if resultado.pop("tiene_pago", False) else "Pendiente"
    return serializar(resultado)
