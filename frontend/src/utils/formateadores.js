const formateadorMoneda = new Intl.NumberFormat('es-AR', {
  style: 'currency',
  currency: 'ARS',
  currencyDisplay: 'narrowSymbol',
  minimumFractionDigits: 2,
})
export const formatearMoneda = (value) =>
  formateadorMoneda.format(Number(value || 0))
export function formatearFecha(value) {
  if (!value) return '—'
  const [year, month, day] = value.split('-')
  return `${day}/${month}/${year}`
}
export const mostrarValor = (value) => value || '—'
