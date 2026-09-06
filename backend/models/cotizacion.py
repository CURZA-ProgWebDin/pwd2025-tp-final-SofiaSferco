CONSULTA_BASE = """
    SELECT c.*, cl.razon_social,
           EXISTS(SELECT 1 FROM obra o WHERE o.id_cotizacion=c.id_cotizacion) AS tiene_obra
    FROM cotizacion c JOIN cliente cl ON cl.id_cliente=c.id_cliente
"""


def listar_todos(conexion, estado=None, sin_obra=False):
    condiciones, parametros = [], []
    if estado:
        condiciones.append("c.estado=%s")
        parametros.append(estado)
    if sin_obra:
        condiciones.append("NOT EXISTS(SELECT 1 FROM obra o WHERE o.id_cotizacion=c.id_cotizacion)")
    consulta = CONSULTA_BASE + ((" WHERE " + " AND ".join(condiciones)) if condiciones else "") + " ORDER BY c.id_cotizacion DESC"
    with conexion.cursor() as cursor:
        cursor.execute(consulta, parametros)
        return cursor.fetchall()


def obtener_por_id(conexion, cotizacion_id, para_actualizar=False):
    with conexion.cursor() as cursor:
        if para_actualizar:
            cursor.execute("SELECT id_cotizacion FROM cotizacion WHERE id_cotizacion=%s FOR UPDATE", (cotizacion_id,))
            if not cursor.fetchone():
                return None
        cursor.execute(CONSULTA_BASE + " WHERE c.id_cotizacion=%s", (cotizacion_id,))
        return cursor.fetchone()


def crear(conexion, datos, anio):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nextval(pg_get_serial_sequence('cotizacion', 'id_cotizacion')) AS id")
        cotizacion_id = cursor.fetchone()["id"]
        codigo = f"COT-{anio}-{cotizacion_id:03d}"
        cursor.execute(
            """INSERT INTO cotizacion
               (id_cotizacion, codigo_cotizacion, id_cliente, tipo_cotizacion, numero_contratacion, titulo, fecha, monto, estado)
               VALUES (%s,%s,%s,%s,%s,%s,%s,%s,'Presentada') RETURNING id_cotizacion""",
            (cotizacion_id, codigo, datos["id_cliente"], datos["tipo_cotizacion"], datos["numero_contratacion"], datos["titulo"], datos["fecha"], datos["monto"]),
        )
        return cotizacion_id


def actualizar(conexion, cotizacion_id, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """UPDATE cotizacion SET id_cliente=%s, tipo_cotizacion=%s, numero_contratacion=%s,
               titulo=%s, fecha=%s, monto=%s, estado=%s WHERE id_cotizacion=%s""",
            (datos["id_cliente"], datos["tipo_cotizacion"], datos["numero_contratacion"], datos["titulo"], datos["fecha"], datos["monto"], datos["estado"], cotizacion_id),
        )


def eliminar(conexion, cotizacion_id):
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cotizacion WHERE id_cotizacion=%s", (cotizacion_id,))
