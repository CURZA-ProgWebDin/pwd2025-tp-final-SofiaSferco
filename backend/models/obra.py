CONSULTA_BASE = """
    SELECT o.*, c.codigo_cotizacion, c.id_cliente, cl.razon_social,
           COALESCE((SELECT SUM(f.importe) FROM factura f WHERE f.id_obra=o.id_obra), 0) AS total_facturado,
           COALESCE((SELECT SUM(p.importe) FROM factura f JOIN pago p ON p.id_factura=f.id_factura WHERE f.id_obra=o.id_obra), 0) AS total_cobrado,
           EXISTS(SELECT 1 FROM factura f WHERE f.id_obra=o.id_obra) AS tiene_facturas
    FROM obra o
    JOIN cotizacion c ON c.id_cotizacion=o.id_cotizacion
    JOIN cliente cl ON cl.id_cliente=c.id_cliente
"""


def listar_todos(conexion, estado_ejecucion=None, con_saldo=False):
    condiciones, parametros = [], []
    if estado_ejecucion:
        condiciones.append("o.estado_ejecucion=%s")
        parametros.append(estado_ejecucion)
    if con_saldo:
        condiciones.append("COALESCE((SELECT SUM(f.importe) FROM factura f WHERE f.id_obra=o.id_obra),0) < o.monto_contratado")
    consulta = CONSULTA_BASE + ((" WHERE " + " AND ".join(condiciones)) if condiciones else "") + " ORDER BY o.id_obra DESC"
    with conexion.cursor() as cursor:
        cursor.execute(consulta, parametros)
        return cursor.fetchall()


def obtener_por_id(conexion, obra_id, para_actualizar=False):
    with conexion.cursor() as cursor:
        if para_actualizar:
            cursor.execute("SELECT id_obra FROM obra WHERE id_obra=%s FOR UPDATE", (obra_id,))
            if not cursor.fetchone():
                return None
        cursor.execute(CONSULTA_BASE + " WHERE o.id_obra=%s", (obra_id,))
        return cursor.fetchone()


def crear(conexion, datos, anio):
    with conexion.cursor() as cursor:
        cursor.execute("SELECT nextval(pg_get_serial_sequence('obra', 'id_obra')) AS id")
        obra_id = cursor.fetchone()["id"]
        codigo = f"OBR-{anio}-{obra_id:03d}"
        cursor.execute(
            """INSERT INTO obra
               (id_obra,codigo_obra,id_cotizacion,titulo,fecha_inicio,fecha_estimada_fin,fecha_fin,
                monto_contratado,estado_ejecucion,tipo_documento,numero_documento,fecha_documento,motivo_estado)
               VALUES (%s,%s,%s,%s,NULL,%s,NULL,%s,'Pendiente',%s,%s,%s,NULL)""",
            (obra_id, codigo, datos["id_cotizacion"], datos["titulo"], datos["fecha_estimada_fin"], datos["monto_contratado"], datos["tipo_documento"], datos["numero_documento"], datos["fecha_documento"]),
        )
        return obra_id


def actualizar(conexion, obra_id, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """UPDATE obra SET titulo=%s, fecha_inicio=%s, fecha_estimada_fin=%s, fecha_fin=%s,
               monto_contratado=%s, estado_ejecucion=%s, tipo_documento=%s, numero_documento=%s,
               fecha_documento=%s, motivo_estado=%s WHERE id_obra=%s""",
            (datos["titulo"], datos["fecha_inicio"], datos["fecha_estimada_fin"], datos["fecha_fin"], datos["monto_contratado"], datos["estado_ejecucion"], datos["tipo_documento"], datos["numero_documento"], datos["fecha_documento"], datos["motivo_estado"], obra_id),
        )


def actualizar_seguimiento(conexion, obra_id, datos):
    with conexion.cursor() as cursor:
        cursor.execute(
            """UPDATE obra SET estado_ejecucion=%s, fecha_inicio=%s, fecha_fin=%s, motivo_estado=%s
               WHERE id_obra=%s""",
            (datos["estado_ejecucion"], datos["fecha_inicio"], datos["fecha_fin"], datos["motivo_estado"], obra_id),
        )


def eliminar(conexion, obra_id):
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM obra WHERE id_obra=%s", (obra_id,))
