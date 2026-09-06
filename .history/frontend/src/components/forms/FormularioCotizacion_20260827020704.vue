<script setup>
import { reactive, watch } from 'vue'
import CampoFormulario from '../CampoFormulario.vue'
import {
  TIPOS_COTIZACION,
  ESTADOS_COTIZACION,
  requiereNumeroContratacion,
} from '../../utils/opciones.js'
import { textoOpcional, textoObligatorio, validarImporte } from '../../utils/formularios.js'

const propiedades = defineProps({
  inicial: { type: Object, default: () => ({}) },
  clientes: { type: Array, default: () => [] },
  editando: Boolean,
  ocupado: Boolean,
})
const emitir = defineEmits(['guardar', 'cancelar'])
const formulario = reactive({
  id_cliente: '',
  tipo_cotizacion: '',
  numero_contratacion: '',
  titulo: '',
  fecha: '',
  monto: '',
  estado: 'Presentada',
})
const errores = reactive({})
watch(
  () => propiedades.inicial,
  (v) =>
    Object.assign(formulario, {
      id_cliente: v.id_cliente || '',
      tipo_cotizacion: v.tipo_cotizacion || '',
      numero_contratacion: v.numero_contratacion || '',
      titulo: v.titulo || '',
      fecha: v.fecha || '',
      monto: v.monto ?? '',
      estado: v.estado || 'Presentada',
    }),
  { immediate: true },
)

function guardar() {
  Object.keys(errores).forEach((k) => delete errores[k])
  if (!formulario.id_cliente) errores.id_cliente = 'Seleccione un cliente.'
  if (!TIPOS_COTIZACION.includes(formulario.tipo_cotizacion))
    errores.tipo_cotizacion = 'Seleccione un tipo.'
  if (
    requiereNumeroContratacion(formulario.tipo_cotizacion) &&
    !textoObligatorio(formulario.numero_contratacion)
  )
    errores.numero_contratacion = 'El número es obligatorio.'
  if (!textoObligatorio(formulario.titulo)) errores.titulo = 'El título es obligatorio.'
  if (!formulario.fecha) errores.fecha = 'La fecha es obligatoria.'
  const errorImporte = validarImporte(formulario.monto, 'El monto')
  if (errorImporte) errores.monto = errorImporte
  if (Object.keys(errores).length) return
  const datosEnvio = {
    id_cliente: Number(formulario.id_cliente),
    tipo_cotizacion: formulario.tipo_cotizacion,
    numero_contratacion: textoOpcional(formulario.numero_contratacion),
    titulo: textoObligatorio(formulario.titulo),
    fecha: formulario.fecha,
    monto: Number(formulario.monto),
  }
  if (propiedades.editando) datosEnvio.estado = formulario.estado
  emitir('guardar', datosEnvio)
}
</script>
<template>
  <form class="form-card" novalidate @submit.prevent="guardar">
    <p v-if="!clientes.length" class="note">
      Primero debe registrar un cliente.
    </p>
    <div class="form-grid">
      <CampoFormulario label="Cliente" required :error="errores.id_cliente">
        <select v-model="formulario.id_cliente">
          <option value="">Seleccione…</option>
          <option
            v-for="cliente in clientes"
            :key="cliente.id_cliente"
            :value="cliente.id_cliente"
          >
            {{ cliente.razon_social }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario label="Tipo" required :error="errores.tipo_cotizacion">
        <select v-model="formulario.tipo_cotizacion">
          <option value="">Seleccione…</option>
          <option v-for="type in TIPOS_COTIZACION" :key="type">
            {{ type }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario
        label="Número de contratación"
        :required="requiereNumeroContratacion(formulario.tipo_cotizacion)"
        :error="errores.numero_contratacion"
      >
        <input v-model="formulario.numero_contratacion" />
      </CampoFormulario>
      <CampoFormulario v-if="editando" label="Estado" required>
        <select v-model="formulario.estado">
          <option v-for="estado in ESTADOS_COTIZACION" :key="estado">
            {{ estado }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario label="Título" required :error="errores.titulo">
        <input v-model="formulario.titulo" />
      </CampoFormulario>
      <CampoFormulario label="Fecha" required :error="errores.fecha">
        <input v-model="formulario.fecha" type="date" />
      </CampoFormulario>
      <CampoFormulario label="Monto" required :error="errores.monto">
        <input v-model="formulario.monto" type="number" min="0.01" step="0.01" />
      </CampoFormulario>
    </div>
    <div class="form-actions">
      <button class="btn btn-neutral" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
      <button class="btn btn-create" :disabled="ocupado || !clientes.length">
        {{ editando ? 'Guardar cambios' : 'Crear cotización' }}
      </button>
    </div>
  </form>
</template>
