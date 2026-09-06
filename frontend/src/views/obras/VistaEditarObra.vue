<script setup>
import { onMounted, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import DialogoConfirmacion from '../../components/DialogoConfirmacion.vue'
import FormularioObra from '../../components/forms/FormularioObra.vue'
import { usarAlmacenObras } from '../../stores/almacenObras.js'
const almacen = usarAlmacenObras()
const { actual, cargando, error } = storeToRefs(almacen)
const ruta = useRoute()
const enrutador = useRouter()
const pendiente = ref(null)
function cargar() {
  almacen.obtenerUno(ruta.params.id).catch(() => {})
}
onMounted(cargar)
async function guardar() {
  try {
    const resultado = await almacen.actualizar(ruta.params.id, pendiente.value)
    enrutador.push({ name: 'obras', query: { message: resultado.message } })
  } catch {
    pendiente.value = null
  }
}
</script>
<template>
  <div class="narrow">
    <EncabezadoPagina titulo="Editar obra" />
    <AlertaAplicacion :mensaje="error" />
    <EstadoCarga v-if="cargando && !actual" />
    <EstadoVacio v-else-if="!actual" titulo="No se pudo cargar la obra" />
    <EstadoVacio
      v-else-if="actual.tiene_facturas"
      titulo="Obra bloqueada"
      texto="Solo puede actualizar su ejecución desde el listado."
    />
    <FormularioObra
      v-else
      editando
      :inicial="actual"
      :ocupado="cargando"
      @cancelar="enrutador.push('/obras')"
      @guardar="pendiente = $event"
    />
    <DialogoConfirmacion
      :abierto="!!pendiente"
      titulo="Confirmar modificación"
      mensaje="¿Confirma que desea guardar los cambios?"
      :ocupado="cargando"
      @cancelar="pendiente = null"
      @confirmar="guardar"
    />
  </div>
</template>
