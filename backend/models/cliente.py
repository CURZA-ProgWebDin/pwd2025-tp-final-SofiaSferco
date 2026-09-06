def listar_todos(conexion):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM cliente ORDER BY id_cliente DESC")
        return cursor.fetchall()


def obtener_por_id(conexion, cliente_id, para_actualizar=False):
    consulta = "SELECT * FROM cliente WHERE id_cliente = %s"
    if para_actualizar:
        consulta += " FOR UPDATE"
    with conexion.cursor() as cursor:
        cursor.execute(consulta, (cliente_id,))
        return cursor.fetchone()


def obtener_por_cuit(conexion, cuit_cuil, id_excluido=None):
    consulta = "SELECT id_cliente FROM cliente WHERE cuit_cuil = %s"
    parametros = [cuit_cuil]
    if id_excluido is not None:
        consulta += " AND id_cliente <> %s"
        parametros.append(id_excluido)
    with conexion.cursor() as cursor:
        cursor.execute(consulta, parametros)
        return cursor.fetchone()


def crear(conexion, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """INSERT INTO cliente (cuit_cuil, razon_social, responsable, telefono, email)
               VALUES (%s, %s, %s, %s, %s) RETURNING *""",
            (datos["cuit_cuil"], datos["razon_social"], datos["responsable"], datos["telefono"], datos["email"]),
        )
        return cursor.fetchone()


def actualizar(conexion, cliente_id, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """UPDATE cliente SET cuit_cuil=%s, razon_social=%s, responsable=%s,
               telefono=%s, email=%s WHERE id_cliente=%s RETURNING *""",
            (datos["cuit_cuil"], datos["razon_social"], datos["responsable"], datos["telefono"], datos["email"], cliente_id),
        )
        return cursor.fetchone()


def tiene_cotizaciones(conexion, cliente_id):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT EXISTS(SELECT 1 FROM cotizacion WHERE id_cliente=%s) AS existe", (cliente_id,))
        return cursor.fetchone()["existe"]


def eliminar(conexion, cliente_id):
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE id_cliente=%s", (cliente_id,))
