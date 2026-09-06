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
import { usarAlmacenFacturas } from '../../stores/almacenFacturas.js'
import { formatearMoneda, formatearFecha } from '../../utils/formateadores.js'
const almacen = usarAlmacenFacturas()
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
    const resultado = await almacen.eliminar(seleccionado.value.id_factura)
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
      titulo="Facturas"
      descripcion="Comprobantes y estado individual de pago."
    >
      <RouterLink class="btn btn-create" to="/facturas/nueva">
        Crear factura
      </RouterLink>
    </EncabezadoPagina>
    <AlertaAplicacion :mensaje="exito" tipo="success" @cerrar="cerrarExito" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !elementos.length" />
    <EstadoVacio
      v-else-if="!cargado && !elementos.length"
      titulo="No se pudieron cargar las facturas"
    >
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <EstadoVacio v-else-if="!elementos.length" titulo="No hay facturas" />
    <div v-else class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Número</th>
            <th>Obra</th>
            <th>Emisión</th>
            <th>Importe</th>
            <th>Estado</th>
            <th>Observaciones</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="factura in elementos" :key="factura.id_factura">
            <td>{{ factura.numero_factura }}</td>
            <td>{{ factura.codigo_obra }}</td>
            <td>{{ formatearFecha(factura.fecha_emision) }}</td>
            <td>{{ formatearMoneda(factura.importe) }}</td>
            <td><InsigniaEstado :valor="factura.estado_pago" /></td>
            <td>{{ factura.observaciones || '—' }}</td>
            <td class="actions">
              <template v-if="factura.estado_pago !== 'Pagada'">
                <RouterLink
                  class="btn btn-small btn-primary"
                  :to="`/facturas/${factura.id_factura}/editar`"
                >
                  Editar
                </RouterLink>
                <button
                  class="btn btn-small btn-danger"
                  @click="seleccionado = factura"
                >
                  Eliminar
                </button>
              </template>
              <small v-else>Bloqueada por pago</small>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <DialogoConfirmacion
      :abierto="!!seleccionado"
      peligro
      titulo="Eliminar factura"
      :mensaje="`¿Confirma que desea eliminar ${seleccionado?.numero_factura}?`"
      texto-confirmacion="Eliminar"
      :ocupado="cargando"
      @cancelar="seleccionado = null"
      @confirmar="eliminar"
    />
  </div>
</template>
