<script setup>
import { nextTick, onMounted, onUpdated, ref, useId } from 'vue'

const propiedades = defineProps({
  label: { type: String, required: true },
  error: { type: String, default: '' },
  required: Boolean,
  hint: { type: String, default: '' },
})
const contenedor = ref(null)
const idControl = useId()
const idDescripcion = `${idControl}-description`
function conectarControl() {
  nextTick(() => {
    const control = contenedor.value?.querySelector('input, select, textarea')
    if (!control) return
    control.id = idControl
    control.setAttribute('aria-required', String(propiedades.required))
    control.setAttribute('aria-invalid', String(Boolean(propiedades.error)))
    if (propiedades.error || propiedades.hint)
      control.setAttribute('aria-describedby', idDescripcion)
    else control.removeAttribute('aria-describedby')
  })
}
onMounted(conectarControl)
onUpdated(conectarControl)
</script>
<template>
  <div ref="contenedor" class="form-field" :class="{ invalid: error }">
    <label :for="idControl">
      {{ label }}
      <span v-if="required">*</span>
    </label>
    <slot />
    <small v-if="error" :id="idDescripcion" class="field-error" role="alert">
      {{ error }}
    </small>
    <small v-else-if="hint" :id="idDescripcion" class="field-hint">
      {{ hint }}
    </small>
  </div>
</template>
