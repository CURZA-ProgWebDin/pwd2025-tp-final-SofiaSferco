import { defineStore } from 'pinia'
import servicioObras from '../services/servicioObras.js'
import { usarEstadoRecurso } from './estadoRecurso.js'
export const usarAlmacenObras = defineStore('obras', () => {
  const estado = usarEstadoRecurso(servicioObras)
  async function actualizarEjecucion(id, datosEnvio) {
    const respuesta = await estado.ejecutar(() =>
      servicioObras.actualizarEjecucion(id, datosEnvio),
    )
    estado.actual.value = respuesta.data.data
    return respuesta.data
  }
  return { ...estado, actualizarEjecucion }
})
