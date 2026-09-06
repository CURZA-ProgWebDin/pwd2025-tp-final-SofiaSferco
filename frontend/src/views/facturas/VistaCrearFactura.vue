<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioFactura from '../../components/forms/FormularioFactura.vue'
import { usarAlmacenFacturas } from '../../stores/almacenFacturas.js'
import servicioObras from '../../services/servicioObras.js'
import { obtenerErrorApi } from '../../services/api.js'
const almacen = usarAlmacenFacturas()
const { cargando, error } = storeToRefs(almacen)
const enrutador = useRouter()
const obras = ref([])
const cargandoOpciones = ref(true)
const opcionesCargadas = ref(false)
const errorOpciones = ref('')
async function cargarOpciones() {
  cargandoOpciones.value = true
  try {
    const respuesta = await servicioObras.listar({ con_saldo_por_facturar: true })
    obras.value = respuesta.data.data
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
    enrutador.push({ name: 'facturas', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina titulo="Nueva factura" />
    <AlertaAplicacion :mensaje="error || errorOpciones" />
    <EstadoCarga v-if="cargandoOpciones" />
    <EstadoVacio
      v-else-if="!opcionesCargadas"
      titulo="No se pudieron cargar las obras"
    >
      <button class="btn btn-primary" @click="cargarOpciones">Reintentar</button>
    </EstadoVacio>
    <FormularioFactura
      v-else
      :obras="obras"
      :ocupado="cargando"
      @cancelar="enrutador.push('/facturas')"
      @guardar="guardar"
    />
  </div>
</template>
