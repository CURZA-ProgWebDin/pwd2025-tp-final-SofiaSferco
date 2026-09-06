CONSULTA_BASE = """
    SELECT p.*, f.numero_factura, f.id_obra, o.codigo_obra
    FROM pago p JOIN factura f ON f.id_factura=p.id_factura JOIN obra o ON o.id_obra=f.id_obra
"""


def listar_todos(conexion):
    with conexion.cursor() as cursor:
        cursor.execute(CONSULTA_BASE + " ORDER BY p.id_pago DESC")
        return cursor.fetchall()


def obtener_por_id(conexion, pago_id):
    with conexion.cursor() as cursor:
        cursor.execute(CONSULTA_BASE + " WHERE p.id_pago=%s", (pago_id,))
        return cursor.fetchone()


def crear(conexion, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """INSERT INTO pago (id_factura,fecha_pago,importe,medio_pago,observaciones)
               VALUES (%s,%s,%s,%s,%s) RETURNING id_pago""",
            (datos["id_factura"], datos["fecha_pago"], datos["importe"], datos["medio_pago"], datos["observaciones"]),
        )
        return cursor.fetchone()["id_pago"]


def eliminar(conexion, pago_id):
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM pago WHERE id_pago=%s RETURNING id_pago", (pago_id,))
        return cursor.fetchone()
