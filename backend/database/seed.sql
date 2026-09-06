SET client_encoding TO 'UTF8';

WITH nuevos_clientes AS (
    INSERT INTO cliente (cuit_cuil, razon_social, responsable, telefono, email) VALUES
        ('30710111223', 'Municipalidad de Puerto Norte', 'Ana Torres', '2994123456', 'obras@puertonorte.gob.ar'),
        ('30720222334', 'Cooperativa Eléctrica del Valle', 'Martín Ruiz', '2994234567', 'proyectos@coopvalle.com.ar'),
        ('20330333445', 'Desarrollos Patagonia SA', 'Lucía Pérez', '2994345678', 'administracion@patagonia.com.ar')
    RETURNING id_cliente, cuit_cuil
), nuevas_cotizaciones AS (
    INSERT INTO cotizacion (codigo_cotizacion, id_cliente, tipo_cotizacion, numero_contratacion, titulo, fecha, monto, estado) VALUES
        ('COT-2026-001', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='30710111223'), 'Presupuesto', NULL, 'Ampliación de red de baja tensión', '2026-01-10', 1100000, 'Aceptada'),
        ('COT-2026-002', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='30720222334'), 'Licitación pública', 'LP-04/2026', 'Renovación de alumbrado público', '2026-01-18', 2100000, 'Aceptada'),
        ('COT-2026-003', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='20330333445'), 'Licitación privada', 'LPR-08/2026', 'Extensión de red de media tensión', '2026-02-02', 3200000, 'Aceptada'),
        ('COT-2026-004', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='30710111223'), 'Concurso de precios', 'CP-12/2026', 'Adecuación de subestación y cableado', '2026-02-15', 1600000, 'Aceptada'),
        ('COT-2026-005', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='30720222334'), 'Compra directa', 'CD-21/2026', 'Instalación eléctrica de plaza central', '2026-03-01', 2600000, 'Aceptada'),
        ('COT-2026-006', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='20330333445'), 'Presupuesto', NULL, 'Tableros para complejo habitacional', '2026-03-12', 950000, 'Presentada'),
        ('COT-2026-007', (SELECT id_cliente FROM nuevos_clientes WHERE cuit_cuil='30710111223'), 'Licitación pública', 'LP-18/2026', 'Recambio de luminarias avenida sur', '2026-03-20', 1800000, 'Rechazada')
    RETURNING id_cotizacion, codigo_cotizacion
), nuevas_obras AS (
    INSERT INTO obra (codigo_obra, id_cotizacion, titulo, fecha_inicio, fecha_estimada_fin, fecha_fin, monto_contratado, estado_ejecucion, tipo_documento, numero_documento, fecha_documento, motivo_estado) VALUES
        ('OBR-2026-001', (SELECT id_cotizacion FROM nuevas_cotizaciones WHERE codigo_cotizacion='COT-2026-001'), 'Ampliación de red de baja tensión - Barrio Norte', NULL, '2026-10-30', NULL, 1000000, 'Pendiente', NULL, NULL, NULL, NULL),
        ('OBR-2026-002', (SELECT id_cotizacion FROM nuevas_cotizaciones WHERE codigo_cotizacion='COT-2026-002'), 'Renovación de alumbrado público - Etapa I', '2026-03-01', '2026-11-30', NULL, 2000000, 'En ejecución', 'Contrato', 'CT-15/2026', '2026-02-25', NULL),
        ('OBR-2026-003', (SELECT id_cotizacion FROM nuevas_cotizaciones WHERE codigo_cotizacion='COT-2026-003'), 'Extensión de red de media tensión - Parque Industrial', '2026-02-20', '2026-06-30', '2026-06-25', 3000000, 'Finalizada', 'Orden de compra', 'OC-3301', '2026-02-18', NULL),
        ('OBR-2026-004', (SELECT id_cotizacion FROM nuevas_cotizaciones WHERE codigo_cotizacion='COT-2026-004'), 'Adecuación eléctrica de subestación central', '2026-04-10', '2026-09-30', NULL, 1500000, 'Suspendida', NULL, NULL, NULL, 'Espera de autorización técnica del comitente'),
        ('OBR-2026-005', (SELECT id_cotizacion FROM nuevas_cotizaciones WHERE codigo_cotizacion='COT-2026-005'), 'Instalación de alumbrado en plaza central', NULL, '2026-12-15', NULL, 2500000, 'Cancelada', 'Resolución', 'RES-88/2026', '2026-03-05', 'Cancelación presupuestaria del comitente')
    RETURNING id_obra, codigo_obra
), nuevas_facturas AS (
    INSERT INTO factura (id_obra, numero_factura, fecha_emision, importe, observaciones) VALUES
        ((SELECT id_obra FROM nuevas_obras WHERE codigo_obra='OBR-2026-002'), 'A-0001-00000101', '2026-05-10', 800000, NULL),
        ((SELECT id_obra FROM nuevas_obras WHERE codigo_obra='OBR-2026-003'), 'A-0001-00000102', '2026-06-26', 3000000, NULL),
        ((SELECT id_obra FROM nuevas_obras WHERE codigo_obra='OBR-2026-004'), 'A-0001-00000103', '2026-05-20', 600000, NULL)
    RETURNING id_factura, numero_factura
)
INSERT INTO pago (id_factura, fecha_pago, importe, medio_pago, observaciones) VALUES
    ((SELECT id_factura FROM nuevas_facturas WHERE numero_factura='A-0001-00000101'), '2026-05-20', 800000, 'Transferencia', NULL),
    ((SELECT id_factura FROM nuevas_facturas WHERE numero_factura='A-0001-00000102'), '2026-07-05', 3000000, 'Cheque', NULL);
