<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioObra from '../../components/forms/FormularioObra.vue'
import { usarAlmacenObras } from '../../stores/almacenObras.js'
import servicioCotizaciones from '../../services/servicioCotizaciones.js'
import { obtenerErrorApi } from '../../services/api.js'
const almacen = usarAlmacenObras()
const { cargando, error } = storeToRefs(almacen)
const enrutador = useRouter()
const cotizaciones = ref([])
const cargandoOpciones = ref(true)
const opcionesCargadas = ref(false)
const errorOpciones = ref('')
async function cargarOpciones() {
  cargandoOpciones.value = true
  try {
    const respuesta = await servicioCotizaciones.listar({
      estado: 'Aceptada',
      sin_obra: true,
    })
    cotizaciones.value = respuesta.data.data
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
    enrutador.push({ name: 'obras', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina
      titulo="Nueva obra"
      descripcion="Comienza en estado Pendiente."
    />
    <AlertaAplicacion :mensaje="error || errorOpciones" />
    <EstadoCarga v-if="cargandoOpciones" />
    <EstadoVacio
      v-else-if="!opcionesCargadas"
      titulo="No se pudieron cargar las cotizaciones"
    >
      <button class="btn btn-primary" @click="cargarOpciones">Reintentar</button>
    </EstadoVacio>
    <FormularioObra
      v-else
      :cotizaciones="cotizaciones"
      :ocupado="cargando"
      @cancelar="enrutador.push('/obras')"
      @guardar="guardar"
    />
  </div>
</template>
