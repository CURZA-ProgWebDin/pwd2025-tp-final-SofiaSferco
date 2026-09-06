<script setup>
defineProps({
  mensaje: { type: String, default: '' },
  tipo: { type: String, default: 'error' },
})
defineEmits(['cerrar'])
</script>

<template>
  <div v-if="mensaje" class="alert" :class="`alert-${tipo}`" role="alert">
    <span>{{ mensaje }}</span>
    <button type="button" aria-label="Cerrar mensaje" @click="$emit('cerrar')">
      ×
    </button>
  </div>
</template>
