CREATE TABLE IF NOT EXISTS cliente (
    id_cliente SERIAL PRIMARY KEY,
    cuit_cuil VARCHAR(11) NOT NULL UNIQUE,
    razon_social TEXT NOT NULL,
    responsable TEXT,
    telefono TEXT,
    email TEXT,
    CONSTRAINT cliente_cuit_cuil_formato CHECK (cuit_cuil ~ '^[0-9]{11}$')
);

CREATE TABLE IF NOT EXISTS cotizacion (
    id_cotizacion SERIAL PRIMARY KEY,
    codigo_cotizacion VARCHAR(20) UNIQUE,
    id_cliente INTEGER NOT NULL REFERENCES cliente(id_cliente),
    tipo_cotizacion VARCHAR(30) NOT NULL,
    numero_contratacion TEXT,
    titulo TEXT NOT NULL,
    fecha DATE NOT NULL,
    monto NUMERIC(12,2) NOT NULL,
    estado VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS obra (
    id_obra SERIAL PRIMARY KEY,
    codigo_obra VARCHAR(20) UNIQUE NOT NULL,
    id_cotizacion INTEGER NOT NULL UNIQUE REFERENCES cotizacion(id_cotizacion),
    titulo TEXT NOT NULL,
    fecha_inicio DATE,
    fecha_estimada_fin DATE,
    fecha_fin DATE,
    monto_contratado NUMERIC(12,2) NOT NULL,
    estado_ejecucion VARCHAR(20) NOT NULL,
    tipo_documento VARCHAR(30),
    numero_documento TEXT,
    fecha_documento DATE,
    motivo_estado TEXT
);

CREATE TABLE IF NOT EXISTS factura (
    id_factura SERIAL PRIMARY KEY,
    id_obra INTEGER NOT NULL REFERENCES obra(id_obra),
    numero_factura TEXT NOT NULL UNIQUE,
    fecha_emision DATE NOT NULL,
    importe NUMERIC(12,2) NOT NULL,
    observaciones TEXT
);

CREATE TABLE IF NOT EXISTS pago (
    id_pago SERIAL PRIMARY KEY,
    id_factura INTEGER NOT NULL UNIQUE REFERENCES factura(id_factura),
    fecha_pago DATE NOT NULL,
    importe NUMERIC(12,2) NOT NULL,
    medio_pago VARCHAR(30) NOT NULL,
    observaciones TEXT
);
