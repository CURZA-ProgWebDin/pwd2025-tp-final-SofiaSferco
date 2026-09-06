<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import DialogoConfirmacion from '../../components/DialogoConfirmacion.vue'
import { usarAlmacenPagos } from '../../stores/almacenPagos.js'
import { formatearMoneda, formatearFecha } from '../../utils/formateadores.js'
const almacen = usarAlmacenPagos()
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
    const resultado = await almacen.eliminar(seleccionado.value.id_pago)
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
    <EncabezadoPagina titulo="Pagos" descripcion="Cobros completos por factura.">
      <RouterLink class="btn btn-create" to="/pagos/nuevo">
        Registrar pago
      </RouterLink>
    </EncabezadoPagina>
    <AlertaAplicacion :mensaje="exito" tipo="success" @cerrar="cerrarExito" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !elementos.length" />
    <EstadoVacio
      v-else-if="!cargado && !elementos.length"
      titulo="No se pudieron cargar los pagos"
    >
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <EstadoVacio v-else-if="!elementos.length" titulo="No hay pagos" />
    <div v-else class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Pago</th>
            <th>Factura</th>
            <th>Obra</th>
            <th>Fecha</th>
            <th>Importe</th>
            <th>Medio</th>
            <th>Observaciones</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="payment in elementos" :key="payment.id_pago">
            <td>#{{ payment.id_pago }}</td>
            <td>{{ payment.numero_factura }}</td>
            <td>{{ payment.codigo_obra }}</td>
            <td>{{ formatearFecha(payment.fecha_pago) }}</td>
            <td>{{ formatearMoneda(payment.importe) }}</td>
            <td>{{ payment.medio_pago }}</td>
            <td>{{ payment.observaciones || '—' }}</td>
            <td>
              <button
                class="btn btn-small btn-danger"
                @click="seleccionado = payment"
              >
                Eliminar
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <DialogoConfirmacion
      :abierto="!!seleccionado"
      peligro
      titulo="Eliminar pago"
      :mensaje="`¿Confirma que desea eliminar el pago #${seleccionado?.id_pago}?`"
      texto-confirmacion="Eliminar"
      :ocupado="cargando"
      @cancelar="seleccionado = null"
      @confirmar="eliminar"
    />
  </div>
</template>
