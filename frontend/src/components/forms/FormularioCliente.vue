<script setup>
import { reactive, watch } from 'vue'
import CampoFormulario from '../CampoFormulario.vue'
import { textoOpcional, textoObligatorio } from '../../utils/formularios.js'

const propiedades = defineProps({
  inicial: { type: Object, default: () => ({}) },
  editando: Boolean,
  ocupado: Boolean,
})
const emitir = defineEmits(['guardar', 'cancelar'])
const formulario = reactive({
  cuit_cuil: '',
  razon_social: '',
  responsable: '',
  telefono: '',
  email: '',
})
const errores = reactive({})
watch(
  () => propiedades.inicial,
  (value) =>
    Object.assign(formulario, {
      cuit_cuil: value.cuit_cuil || '',
      razon_social: value.razon_social || '',
      responsable: value.responsable || '',
      telefono: value.telefono || '',
      email: value.email || '',
    }),
  { immediate: true },
)

function guardar() {
  Object.keys(errores).forEach((key) => delete errores[key])
  const cuit = formulario.cuit_cuil.replace(/[\s-]/g, '')
  if (!/^\d{11}$/.test(cuit))
    errores.cuit_cuil = 'Debe contener exactamente 11 dígitos.'
  if (!textoObligatorio(formulario.razon_social))
    errores.razon_social = 'La razón social es obligatoria.'
  if (formulario.telefono.trim() && !/^\d+$/.test(formulario.telefono.trim()))
    errores.telefono = 'El teléfono solo puede contener números.'
  if (
    formulario.email.trim() &&
    !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formulario.email.trim())
  )
    errores.email = 'Ingrese un email válido.'
  if (Object.keys(errores).length) return
  emitir('guardar', {
    cuit_cuil: cuit,
    razon_social: textoObligatorio(formulario.razon_social),
    responsable: textoOpcional(formulario.responsable),
    telefono: textoOpcional(formulario.telefono),
    email: textoOpcional(formulario.email),
  })
}
</script>

<template>
  <form class="form-card" novalidate @submit.prevent="guardar">
    <div class="form-grid">
      <CampoFormulario label="CUIT/CUIL" required :error="errores.cuit_cuil">
        <input v-model="formulario.cuit_cuil" placeholder="20-12345678-3" />
      </CampoFormulario>
      <CampoFormulario label="Razón social" required :error="errores.razon_social">
        <input v-model="formulario.razon_social" />
      </CampoFormulario>
      <CampoFormulario label="Responsable">
        <input v-model="formulario.responsable" />
      </CampoFormulario>
      <CampoFormulario label="Teléfono" :error="errores.telefono">
        <input v-model="formulario.telefono" />
      </CampoFormulario>
      <CampoFormulario label="Email" :error="errores.email">
        <input v-model="formulario.email" type="email" />
      </CampoFormulario>
    </div>
    <div class="form-actions">
      <button
        class="btn btn-neutral"
        type="button"
        :disabled="ocupado"
        @click="$emit('cancelar')"
      >
        Cancelar
      </button>
      <button
        class="btn"
        :class="editando ? 'btn-primary' : 'btn-create'"
        :disabled="ocupado"
      >
        {{
          ocupado ? 'Guardando…' : editando ? 'Guardar cambios' : 'Crear cliente'
        }}
      </button>
    </div>
  </form>
</template>
