export const TIPOS_COTIZACION = [
  'Presupuesto',
  'Licitación pública',
  'Licitación privada',
  'Concurso de precios',
  'Compra directa',
]
export const ESTADOS_COTIZACION = ['Presentada', 'Aceptada', 'Rechazada']
export const ESTADOS_OBRA = [
  'Pendiente',
  'En ejecución',
  'Finalizada',
  'Suspendida',
  'Cancelada',
]
export const TIPOS_DOCUMENTO = [
  'Contrato',
  'Orden de compra',
  'Pedido de compra',
  'Resolución',
  'Otros',
]
export const MEDIOS_PAGO = [
  'Transferencia',
  'Efectivo',
  'Cheque',
  'Echeq',
  'Otros',
]
export const requiereNumeroContratacion = (type) => type && type !== 'Presupuesto'
export const requiereFechaInicio = (estado) =>
  ['En ejecución', 'Finalizada', 'Suspendida'].includes(estado)
export const requiereFechaFin = (estado) => estado === 'Finalizada'
export const requiereMotivo = (estado) =>
  ['Suspendida', 'Cancelada'].includes(estado)
