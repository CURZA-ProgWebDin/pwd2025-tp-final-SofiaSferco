<script setup>
defineProps({
  titulo: { type: String, default: 'No hay registros' },
  texto: { type: String, default: 'Todavía no se cargó información.' },
})
</script>

<template>
  <div class="state-panel">
    <strong>{{ titulo }}</strong>
    <p>{{ texto }}</p>
    <slot />
  </div>
</template>
