<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import FormularioCotizacion from '../../components/forms/FormularioCotizacion.vue'
import { usarAlmacenCotizaciones } from '../../stores/almacenCotizaciones.js'
import { usarAlmacenClientes } from '../../stores/almacenClientes.js'
const almacen = usarAlmacenCotizaciones()
const almacenClientes = usarAlmacenClientes()
const { cargando, error } = storeToRefs(almacen)
const { elementos: clientes, cargando: cargandoOpciones } = storeToRefs(almacenClientes)
const enrutador = useRouter()
onMounted(() => almacenClientes.obtenerTodos().catch(() => {}))
async function guardar(datosEnvio) {
  try {
    const resultado = await almacen.crear(datosEnvio)
    enrutador.push({ name: 'cotizaciones', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina
      titulo="Nueva cotización"
      descripcion="Comienza en estado Presentada."
    />
    <AlertaAplicacion :mensaje="error || almacenClientes.error" />
    <EstadoCarga v-if="cargandoOpciones" />
    <FormularioCotizacion
      v-else
      :clientes="clientes"
      :ocupado="cargando"
      @cancelar="enrutador.push('/cotizaciones')"
      @guardar="guardar"
    />
  </div>
</template>
