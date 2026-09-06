import { defineStore } from 'pinia'
import { ref } from 'vue'
import servicioPagos from '../services/servicioPagos.js'
import { obtenerErrorApi } from '../services/api.js'

export const usarAlmacenPagos = defineStore('pagos', () => {
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
  async function obtenerTodos() {
    try {
      const respuesta = await ejecutar(() => servicioPagos.listar())
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
    const respuesta = await ejecutar(() => servicioPagos.obtener(id))
    actual.value = respuesta.data.data
    return actual.value
  }
  async function crear(datosEnvio) {
    return (await ejecutar(() => servicioPagos.crear(datosEnvio))).data
  }
  async function eliminar(id) {
    return (await ejecutar(() => servicioPagos.eliminar(id))).data
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
    eliminar,
    limpiarError,
  }
})
