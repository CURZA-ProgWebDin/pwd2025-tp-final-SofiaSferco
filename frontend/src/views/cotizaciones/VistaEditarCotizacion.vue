<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioCotizacion from '../../components/forms/FormularioCotizacion.vue'
import { usarAlmacenCotizaciones } from '../../stores/almacenCotizaciones.js'
import { usarAlmacenClientes } from '../../stores/almacenClientes.js'
const almacen = usarAlmacenCotizaciones()
const almacenClientes = usarAlmacenClientes()
const { actual, cargando, error } = storeToRefs(almacen)
const { elementos: clientes } = storeToRefs(almacenClientes)
const ruta = useRoute()
const enrutador = useRouter()
async function cargar() {
  try {
    await Promise.all([
      almacen.obtenerUno(ruta.params.id),
      almacenClientes.obtenerTodos(),
    ])
  } catch {}
}
onMounted(cargar)
async function guardar(datosEnvio) {
  try {
    const resultado = await almacen.actualizar(ruta.params.id, datosEnvio)
    enrutador.push({ name: 'cotizaciones', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina titulo="Editar cotización" />
    <AlertaAplicacion :mensaje="error || almacenClientes.error" />
    <EstadoCarga v-if="cargando && !actual" />
    <EstadoVacio v-else-if="!actual" titulo="No se pudo cargar la cotización" />
    <EstadoVacio
      v-else-if="actual.tiene_obra"
      titulo="Cotización bloqueada"
      texto="Ya originó una obra."
    />
    <FormularioCotizacion
      v-else
      editando
      :inicial="actual"
      :clientes="clientes"
      :ocupado="cargando"
      @cancelar="enrutador.push('/cotizaciones')"
      @guardar="guardar"
    />
  </div>
</template>
