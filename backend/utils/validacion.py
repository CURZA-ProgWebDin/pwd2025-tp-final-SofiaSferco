from datetime import date
from decimal import Decimal, InvalidOperation

from backend.utils.errores import ErrorApi


def requerir_objeto_json(datos):
    if not isinstance(datos, dict):
        raise ErrorApi("El cuerpo de la solicitud debe ser un objeto JSON.", 400)
    return datos


def texto_obligatorio(datos, campo, etiqueta=None):
    valor = datos.get(campo)
    if not isinstance(valor, str) or not valor.strip():
        raise ErrorApi(f"{etiqueta or campo} es obligatorio.", 400)
    return valor.strip()


def texto_opcional(datos, campo):
    valor = datos.get(campo)
    if valor is None:
        return None
    if not isinstance(valor, str):
        raise ErrorApi(f"{campo} debe ser texto.", 400)
    return valor.strip() or None


def importe_positivo(datos, campo, etiqueta=None):
    valor = datos.get(campo)
    if isinstance(valor, bool):
        raise ErrorApi(f"{etiqueta or campo} debe ser un importe mayor que cero.", 400)
    try:
        numero = Decimal(str(valor))
    except (InvalidOperation, TypeError, ValueError):
        raise ErrorApi(f"{etiqueta or campo} debe ser un importe válido.", 400)
    if not numero.is_finite() or numero <= 0 or numero.as_tuple().exponent < -2:
        raise ErrorApi(f"{etiqueta or campo} debe ser mayor que cero y tener hasta dos decimales.", 400)
    if numero > Decimal("9999999999.99"):
        raise ErrorApi(f"{etiqueta or campo} excede el máximo permitido.", 400)
    return numero


def id_entero(datos, campo, etiqueta=None):
    valor = datos.get(campo)
    if isinstance(valor, bool) or not isinstance(valor, int) or valor <= 0:
        raise ErrorApi(f"{etiqueta or campo} debe ser un identificador válido.", 400)
    return valor


def fecha_valida(datos, campo, required=True):
    valor = datos.get(campo)
    if valor in (None, ""):
        if required:
            raise ErrorApi(f"{campo} es obligatorio.", 400)
        return None
    if not isinstance(valor, str):
        raise ErrorApi(f"{campo} debe tener formato YYYY-MM-DD.", 400)
    try:
        return date.fromisoformat(valor)
    except ValueError:
        raise ErrorApi(f"{campo} debe ser una fecha válida con formato YYYY-MM-DD.", 400)


def valor_permitido(datos, campo, permitidos):
    valor = texto_obligatorio(datos, campo, campo)
    if valor not in permitidos:
        raise ErrorApi(f"{campo} no contiene un valor permitido.", 400)
    return valor


def filtro_verdadero(valor, nombre):
    if valor is None:
        return False
    if valor != "true":
        raise ErrorApi(f"El parámetro {nombre} solo admite el valor true.", 400)
    return True
