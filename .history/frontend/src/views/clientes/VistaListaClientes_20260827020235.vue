<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import DialogoConfirmacion from '../../components/DialogoConfirmacion.vue'
import { usarAlmacenClientes } from '../../stores/almacenClientes.js'
import { mostrarValor } from '../../utils/formateadores.js'

const almacen = usarAlmacenClientes()
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
    const resultado = await almacen.eliminar(seleccionado.value.id_cliente)
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
      titulo="Clientes"
      descripcion="Personas y organizaciones que originan el ciclo."
    >
      <RouterLink class="btn btn-create" to="/clientes/nuevo">
        Crear cliente
      </RouterLink>
    </EncabezadoPagina>
    <AlertaAplicacion :mensaje="exito" tipo="success" @cerrar="cerrarExito" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !elementos.length" />
    <EstadoVacio
      v-else-if="!cargado && !elementos.length"
      titulo="No se pudieron cargar los clientes"
    >
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <EstadoVacio
      v-else-if="!elementos.length"
      titulo="No hay clientes"
      texto="Registre el primer cliente."
    />
    <div v-else class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>Razón social</th>
            <th>CUIT/CUIL</th>
            <th>Responsable</th>
            <th>Contacto</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cliente in elementos" :key="cliente.id_cliente">
            <td>
              <strong>{{ cliente.razon_social }}</strong>
            </td>
            <td>{{ cliente.cuit_cuil }}</td>
            <td>{{ mostrarValor(cliente.responsable) }}</td>
            <td>
              {{ mostrarValor(cliente.telefono) }}
              <small>{{ mostrarValor(cliente.email) }}</small>
            </td>
            <td class="actions">
              <RouterLink
                class="btn btn-small btn-primary"
                :to="`/clientes/${cliente.id_cliente}/editar`"
              >
                Editar
              </RouterLink>
              <button
                class="btn btn-small btn-danger"
                @click="seleccionado = cliente"
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
      titulo="Eliminar cliente"
      :mensaje="`¿Confirma que desea eliminar a ${seleccionado?.razon_social}?`"
      texto-confirmacion="Eliminar"
      :ocupado="cargando"
      @cancelar="seleccionado = null"
      @confirmar="eliminar"
    />
  </div>
</template>
