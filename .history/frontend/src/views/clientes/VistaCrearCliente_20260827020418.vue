<script setup>
import { storeToRefs } from 'pinia'
import { useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import FormularioCliente from '../../components/forms/FormularioCliente.vue'
import { usarAlmacenClientes } from '../../stores/almacenClientes.js'

const almacen = usarAlmacenClientes()
const { cargando, error } = storeToRefs(almacen)
const enrutador = useRouter()

async function guardar(datosEnvio) {
  try {
    const resultado = await almacen.crear(datosEnvio)
    enrutador.push({ name: 'clientes', query: { message: resultado.message } })
  } catch {}
}
</script>

<template>
  <div class="narrow">
    <EncabezadoPagina
      titulo="Nuevo cliente"
      descripcion="Los campos con * son obligatorios."
    />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <FormularioCliente
      :ocupado="cargando"
      @cancelar="enrutador.push('/clientes')"
      @guardar="guardar"
    />
  </div>
</template>
