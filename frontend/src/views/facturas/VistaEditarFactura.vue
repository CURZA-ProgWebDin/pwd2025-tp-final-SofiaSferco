<script setup>
import { onMounted } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import FormularioFactura from '../../components/forms/FormularioFactura.vue'
import { usarAlmacenFacturas } from '../../stores/almacenFacturas.js'
const almacen = usarAlmacenFacturas()
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
    enrutador.push({ name: 'facturas', query: { message: resultado.message } })
  } catch {}
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina titulo="Editar factura" />
    <AlertaAplicacion :mensaje="error" />
    <EstadoCarga v-if="cargando && !actual" />
    <EstadoVacio v-else-if="!actual" titulo="No se pudo cargar la factura" />
    <EstadoVacio
      v-else-if="actual.estado_pago === 'Pagada'"
      titulo="Factura bloqueada"
      texto="Tiene un pago asociado."
    />
    <FormularioFactura
      v-else
      editando
      :inicial="actual"
      :ocupado="cargando"
      @cancelar="enrutador.push('/facturas')"
      @guardar="guardar"
    />
  </div>
</template>
