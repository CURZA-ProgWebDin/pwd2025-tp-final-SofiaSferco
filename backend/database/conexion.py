import psycopg
from psycopg.rows import dict_row

from backend.config import Configuracion


def obtener_conexion():
    """Devuelve una conexión administrada por el controlador que la solicita."""
    return psycopg.connect(**Configuracion.parametros_base_datos(), row_factory=dict_row)
