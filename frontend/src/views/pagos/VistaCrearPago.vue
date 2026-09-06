<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioPago from '../../components/forms/FormularioPago.vue'
import { usarAlmacenPagos } from '../../stores/almacenPagos.js'
import servicioFacturas from '../../services/servicioFacturas.js'
import { obtenerErrorApi } from '../../services/api.js'
const almacen = usarAlmacenPagos()
const { cargando, error } = storeToRefs(almacen)
const enrutador = useRouter()
const facturas = ref([])
const cargandoOpciones = ref(true)
const opcionesCargadas = ref(false)
const errorOpciones = ref('')
async function cargarOpciones() {
  cargandoOpciones.value = true
  try {
    const respuesta = await servicioFacturas.listar({ sin_pago: true })
    facturas.value = respuesta.data.data
    opcionesCargadas.value = true
  } catch (e) {
    opcionesCargadas.value = false
    errorOpciones.value = obtenerErrorApi(e)
  } finally {
    cargandoOpciones.value = false
  }
}
onMounted(cargarOpciones)
async function guardar(datosEnvio) {
  try {
    const resultado = await almacen.crear(datosEnvio)
    enrutador.push({ name: 'pagos', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina
      titulo="Registrar pago"
      descripcion="El importe debe coincidir con la factura."
    />
    <AlertaAplicacion :mensaje="error || errorOpciones" />
    <EstadoCarga v-if="cargandoOpciones" />
    <EstadoVacio
      v-else-if="!opcionesCargadas"
      titulo="No se pudieron cargar las facturas"
    >
      <button class="btn btn-primary" @click="cargarOpciones">Reintentar</button>
    </EstadoVacio>
    <FormularioPago
      v-else
      :facturas="facturas"
      :ocupado="cargando"
      @cancelar="enrutador.push('/pagos')"
      @guardar="guardar"
    />
  </div>
</template>
