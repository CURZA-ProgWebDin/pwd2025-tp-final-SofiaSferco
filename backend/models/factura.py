CONSULTA_BASE = """
    SELECT f.*, o.codigo_obra, o.titulo AS titulo_obra,
           EXISTS(SELECT 1 FROM pago p WHERE p.id_factura=f.id_factura) AS tiene_pago
    FROM factura f JOIN obra o ON o.id_obra=f.id_obra
"""


def listar_todos(conexion, sin_pago=False):
    consulta = CONSULTA_BASE
    if sin_pago:
        consulta += " WHERE NOT EXISTS(SELECT 1 FROM pago p WHERE p.id_factura=f.id_factura)"
    consulta += " ORDER BY f.id_factura DESC"
    with conexion.cursor() as cursor:
        cursor.execute(consulta)
        return cursor.fetchall()


def obtener_por_id(conexion, factura_id, para_actualizar=False):
    with conexion.cursor() as cursor:
        if para_actualizar:
            cursor.execute("SELECT id_factura FROM factura WHERE id_factura=%s FOR UPDATE", (factura_id,))
            if not cursor.fetchone():
                return None
        cursor.execute(CONSULTA_BASE + " WHERE f.id_factura=%s", (factura_id,))
        return cursor.fetchone()


def obtener_por_numero(conexion, numero, id_excluido=None):
    consulta = "SELECT id_factura FROM factura WHERE numero_factura=%s"
    parametros = [numero]
    if id_excluido is not None:
        consulta += " AND id_factura<>%s"
        parametros.append(id_excluido)
    with conexion.cursor() as cursor:
        cursor.execute(consulta, parametros)
        return cursor.fetchone()


def total_por_obra(conexion, obra_id, id_excluido=None):
    consulta = "SELECT COALESCE(SUM(importe),0) AS total FROM factura WHERE id_obra=%s"
    parametros = [obra_id]
    if id_excluido is not None:
        consulta += " AND id_factura<>%s"
        parametros.append(id_excluido)
    with conexion.cursor() as cursor:
        cursor.execute(consulta, parametros)
        return cursor.fetchone()["total"]


def crear(conexion, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """INSERT INTO factura (id_obra,numero_factura,fecha_emision,importe,observaciones)
               VALUES (%s,%s,%s,%s,%s) RETURNING id_factura""",
            (datos["id_obra"], datos["numero_factura"], datos["fecha_emision"], datos["importe"], datos["observaciones"]),
        )
        return cursor.fetchone()["id_factura"]


def actualizar(conexion, factura_id, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """UPDATE factura SET numero_factura=%s,fecha_emision=%s,importe=%s,observaciones=%s
               WHERE id_factura=%s""",
            (datos["numero_factura"], datos["fecha_emision"], datos["importe"], datos["observaciones"], factura_id),
        )


def eliminar(conexion, factura_id):
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM factura WHERE id_factura=%s", (factura_id,))
