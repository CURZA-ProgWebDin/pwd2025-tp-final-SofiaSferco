<script setup>
import { nextTick, ref, watch } from 'vue'

const propiedades = defineProps({
  abierto: Boolean,
  titulo: { type: String, default: 'Confirmar acción' },
  mensaje: { type: String, required: true },
  textoConfirmacion: { type: String, default: 'Confirmar' },
  peligro: Boolean,
  ocupado: Boolean,
})
const emitir = defineEmits(['confirmar', 'cancelar'])
const botonConfirmar = ref(null)
watch(
  () => propiedades.abierto,
  async (abierto) => {
    if (abierto) {
      await nextTick()
      botonConfirmar.value?.focus()
    }
  },
)

function cancelar() {
  if (!propiedades.ocupado) emitir('cancelar')
}
</script>
<template>
  <Teleport to="body">
    <div v-if="abierto" class="dialog-backdrop" @click.self="cancelar">
      <section class="dialog" role="alertdialog" aria-modal="true">
        <h2>{{ titulo }}</h2>
        <p>{{ mensaje }}</p>
        <div class="form-actions">
          <button
            class="btn btn-neutral"
            type="button"
            :disabled="ocupado"
            @click="cancelar"
          >
            Cancelar
          </button>
          <button
            ref="botonConfirmar"
            class="btn"
            :class="peligro ? 'btn-danger' : 'btn-primary'"
            type="button"
            :disabled="ocupado"
            @click="$emit('confirmar')"
          >
            {{ ocupado ? 'Procesando…' : textoConfirmacion }}
          </button>
        </div>
      </section>
    </div>
  </Teleport>
</template>
