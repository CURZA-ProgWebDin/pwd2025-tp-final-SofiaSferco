<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import DialogoConfirmacion from '../../components/DialogoConfirmacion.vue'
import InsigniaEstado from '../../components/InsigniaEstado.vue'
import { usarAlmacenCotizaciones } from '../../stores/almacenCotizaciones.js'
import { formatearMoneda, formatearFecha } from '../../utils/formateadores.js'
const almacen = usarAlmacenCotizaciones()
const { elementos, cargando, cargado, error } = storeToRefs(almacen)
const ruta = useRoute()
const enrutador = useRouter()
const seleccionado = ref(null)
const exito = ref(String(ruta.query.message || ''))
function cargar() {
  almacen.obtenerTodos().catch(() => {})
}
onMounted(cargar)
async function eliminar() {
  try {
    const resultado = await almacen.eliminar(seleccionado.value.id_cotizacion)
    seleccionado.value = null
    exito.value = resultado.message
    await almacen.obtenerTodos()
  } catch {
    seleccionado.value = null
  }
}
function cerrarExito() {
  exito.value = ''
  if (ruta.query.message) enrutador.replace({ query: {} })
}
</script>
<template>
  <div>
    <EncabezadoPagina
      titulo="Cotizaciones"
      descripcion="Propuestas y situación comercial."
    >
      <RouterLink class="btn btn-create" to="/cotizaciones/nueva">
        Crear cotización
      </RouterLink>
    </EncabezadoPagina>
    <AlertaAplicacion :mensaje="exito" tipo="success" @cerrar="cerrarExito" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !elementos.length" />
    <EstadoVacio
      v-else-if="!cargado && !elementos.length"
      titulo="No se pudieron cargar las cotizaciones"
    >
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <EstadoVacio v-else-if="!elementos.length" titulo="No hay cotizaciones" />
    <div v-else class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Código / título</th>
            <th>Cliente</th>
            <th>Tipo</th>
            <th>Fecha</th>
            <th>Monto</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cotizacion in elementos" :key="cotizacion.id_cotizacion">
            <td>
              <strong>{{ cotizacion.codigo_cotizacion }}</strong>
              <small>{{ cotizacion.titulo }}</small>
            </td>
            <td>{{ cotizacion.razon_social }}</td>
            <td>{{ cotizacion.tipo_cotizacion }}</td>
            <td>{{ formatearFecha(cotizacion.fecha) }}</td>
            <td>{{ formatearMoneda(cotizacion.monto) }}</td>
            <td><InsigniaEstado :valor="cotizacion.estado" /></td>
            <td class="actions">
              <template v-if="!cotizacion.tiene_obra">
                <RouterLink
                  class="btn btn-small btn-primary"
                  :to="`/cotizaciones/${cotizacion.id_cotizacion}/editar`"
                >
                  Editar
                </RouterLink>
                <button
                  class="btn btn-small btn-danger"
                  @click="seleccionado = cotizacion"
                >
                  Eliminar
                </button>
              </template>
              <small v-else>Bloqueada por obra</small>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <DialogoConfirmacion
      :abierto="!!seleccionado"
      peligro
      titulo="Eliminar cotización"
      :mensaje="`¿Confirma que desea eliminar ${seleccionado?.codigo_cotizacion}?`"
      texto-confirmacion="Eliminar"
      :ocupado="cargando"
      @cancelar="seleccionado = null"
      @confirmar="eliminar"
    />
  </div>
</template>
