<script setup>
import { computed, reactive, watch } from 'vue'
import CampoFormulario from '../CampoFormulario.vue'
import { textoOpcional, textoObligatorio, validarImporte } from '../../utils/formularios.js'
import { formatearMoneda } from '../../utils/formateadores.js'

const propiedades = defineProps({
  inicial: { type: Object, default: () => ({}) },
  obras: { type: Array, default: () => [] },
  editando: Boolean,
  ocupado: Boolean,
})
const emitir = defineEmits(['guardar', 'cancelar'])
const formulario = reactive({
  id_obra: '',
  numero_factura: '',
  fecha_emision: '',
  importe: '',
  observaciones: '',
})
const errores = reactive({})
const obraSeleccionada = computed(() =>
  propiedades.obras.find((item) => item.id_obra === Number(formulario.id_obra)),
)
watch(
  () => propiedades.inicial,
  (v) =>
    Object.assign(formulario, {
      id_obra: v.id_obra || '',
      numero_factura: v.numero_factura || '',
      fecha_emision: v.fecha_emision || '',
      importe: v.importe ?? '',
      observaciones: v.observaciones || '',
    }),
  { immediate: true },
)

function guardar() {
  Object.keys(errores).forEach((k) => delete errores[k])
  if (!propiedades.editando && !formulario.id_obra) errores.id_obra = 'Seleccione una obra.'
  if (!textoObligatorio(formulario.numero_factura))
    errores.numero_factura = 'El número es obligatorio.'
  if (!formulario.fecha_emision) errores.fecha_emision = 'La fecha es obligatoria.'
  const errorImporte = validarImporte(formulario.importe, 'El importe')
  if (errorImporte) errores.importe = errorImporte
  if (
    !errorImporte &&
    !propiedades.editando &&
    obraSeleccionada.value &&
    Number(formulario.importe) > Number(obraSeleccionada.value.saldo_por_facturar)
  )
    errores.importe = `No puede superar ${formatearMoneda(obraSeleccionada.value.saldo_por_facturar)}.`
  if (Object.keys(errores).length) return
  const datosEnvio = {
    numero_factura: textoObligatorio(formulario.numero_factura),
    fecha_emision: formulario.fecha_emision,
    importe: Number(formulario.importe),
    observaciones: textoOpcional(formulario.observaciones),
  }
  if (!propiedades.editando) datosEnvio.id_obra = Number(formulario.id_obra)
  emitir('guardar', datosEnvio)
}
</script>

<template>
  <form class="form-card" novalidate @submit.prevent="guardar">
    <p v-if="!editando && !obras.length" class="note">
      No hay obras con saldo por facturar.
    </p>
    <div class="form-grid">
      <CampoFormulario v-if="!editando" label="Obra" required :error="errores.id_obra">
        <select v-model="formulario.id_obra">
          <option value="">Seleccione…</option>
          <option
            v-for="obra in obras"
            :key="obra.id_obra"
            :value="obra.id_obra"
          >
            {{ obra.codigo_obra }} · saldo
            {{ formatearMoneda(obra.saldo_por_facturar) }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario
        label="Número de factura"
        required
        :error="errores.numero_factura"
      >
        <input v-model="formulario.numero_factura" />
      </CampoFormulario>
      <CampoFormulario
        label="Fecha de emisión"
        required
        :error="errores.fecha_emision"
      >
        <input v-model="formulario.fecha_emision" type="date" />
      </CampoFormulario>
      <CampoFormulario label="Importe" required :error="errores.importe">
        <input v-model="formulario.importe" type="number" min="0.01" step="0.01" />
      </CampoFormulario>
      <CampoFormulario label="Observaciones">
        <textarea v-model="formulario.observaciones"></textarea>
      </CampoFormulario>
    </div>
    <div class="form-actions">
      <button class="btn btn-neutral" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
      <button
        class="btn btn-create"
        :disabled="ocupado || (!editando && !obras.length)"
      >
        {{ editando ? 'Guardar cambios' : 'Crear factura' }}
      </button>
    </div>
  </form>
</template>
