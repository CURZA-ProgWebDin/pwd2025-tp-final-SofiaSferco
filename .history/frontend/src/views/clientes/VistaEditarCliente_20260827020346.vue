<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioCliente from '../../components/forms/FormularioCliente.vue'
import { usarAlmacenClientes } from '../../stores/almacenClientes.js'

const almacen = usarAlmacenClientes()
const { actual, cargando, error } = storeToRefs(almacen)
const ruta = useRoute()
const enrutador = useRouter()

function cargar() {
  almacen.obtenerUno(ruta.params.id).catch(() => {})
}
onMounted(cargar)
async function guardar(datosEnvio) {
  try {
    const resultado = await almacen.actualizar(ruta.params.id, datosEnvio)
    enrutador.push({ name: 'clientes', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina titulo="Editar cliente" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !actual" />
    <EstadoVacio v-else-if="!actual" titulo="No se pudo cargar el cliente">
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <FormularioCliente
      v-else
      editando
      :inicial="actual"
      :ocupado="cargando"
      @cancelar="enrutador.push('/clientes')"
      @guardar="guardar"
    />
  </div>
</template>
