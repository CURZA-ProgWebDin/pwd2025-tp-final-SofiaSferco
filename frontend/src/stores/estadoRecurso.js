import { ref } from 'vue'
import { obtenerErrorApi } from '../services/api.js'

export function usarEstadoRecurso(servicio) {
  const elementos = ref([])
  const actual = ref(null)
  const cargando = ref(false)
  const cargado = ref(false)
  const error = ref('')

  async function ejecutar(solicitud) {
    cargando.value = true
    error.value = ''
    try {
      return await solicitud()
    } catch (errorSolicitud) {
      error.value = obtenerErrorApi(errorSolicitud)
      throw errorSolicitud
    } finally {
      cargando.value = false
    }
  }
  async function obtenerTodos(params) {
    try {
      const respuesta = await ejecutar(() => servicio.listar(params))
      elementos.value = respuesta.data.data
      cargado.value = true
      return elementos.value
    } catch (errorSolicitud) {
      cargado.value = false
      throw errorSolicitud
    }
  }
  async function obtenerUno(id) {
    actual.value = null
    const respuesta = await ejecutar(() => servicio.obtener(id))
    actual.value = respuesta.data.data
    return actual.value
  }
  async function crear(datosEnvio) {
    return (await ejecutar(() => servicio.crear(datosEnvio))).data
  }
  async function actualizar(id, datosEnvio) {
    const respuesta = await ejecutar(() => servicio.actualizar(id, datosEnvio))
    actual.value = respuesta.data.data
    return respuesta.data
  }
  async function eliminar(id) {
    return (await ejecutar(() => servicio.eliminar(id))).data
  }
  function limpiarError() {
    error.value = ''
  }
  return {
    elementos,
    actual,
    cargando,
    cargado,
    error,
    obtenerTodos,
    obtenerUno,
    crear,
    actualizar,
    eliminar,
    ejecutar,
    limpiarError,
  }
}
