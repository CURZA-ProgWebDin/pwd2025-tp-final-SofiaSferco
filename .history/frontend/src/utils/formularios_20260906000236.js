export const IMPORTE_MAXIMO = 9999999999.99

export const textoOpcional = (value) => String(value ?? '').trim() || null

export const textoObligatorio = (value) => String(value ?? '').trim()

export function validarImporte(value, label) {
  const text = String(value ?? '').trim()
  const number = Number(text)
  if (!text || !Number.isFinite(number) || number <= 0)
    return `${label} debe ser un número mayor que cero.`
  if (!/^(?:\d+|\d*\.\d{1,2})$/.test(text))
    return `${label} admite como máximo dos decimales.`
  if (number > IMPORTE_MAXIMO) return `${label} no puede superar 9.999.999.999,99.`
  return ''
}

export function validarEjecucionObra(formulario) {
  const errores = {}
  if (
    formulario.estado_ejecucion === 'Pendiente' &&
    (formulario.fecha_inicio || formulario.fecha_fin)
  )
    errores.estado_ejecucion =
      'Una obra Pendiente no puede tener fecha de inicio ni de finalización.'
  if (
    ['En ejecución', 'Finalizada', 'Suspendida'].includes(
      formulario.estado_ejecucion,
    ) &&
    !formulario.fecha_inicio
  )
    errores.fecha_inicio = 'La fecha de inicio es obligatoria para este estado.'
  if (formulario.estado_ejecucion === 'Finalizada' && !formulario.fecha_fin)
    errores.fecha_fin = 'La fecha de finalización es obligatoria.'
  if (formulario.fecha_fin && formulario.estado_ejecucion !== 'Finalizada')
    errores.fecha_fin =
      'Solo una obra Finalizada puede tener fecha de finalización.'
  if (formulario.fecha_inicio && formulario.fecha_fin && formulario.fecha_fin < formulario.fecha_inicio)
    errores.fecha_fin =
      'La fecha de finalización no puede ser anterior al inicio.'
  if (
    ['Suspendida', 'Cancelada'].includes(formulario.estado_ejecucion) &&
    !textoObligatorio(formulario.motivo_estado)
  )
    errores.motivo_estado = 'El motivo es obligatorio para este estado.'
  return errores
}
