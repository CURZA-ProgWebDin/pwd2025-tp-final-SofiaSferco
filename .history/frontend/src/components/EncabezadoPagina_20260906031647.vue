<script setup>
defineProps({
  titulo: { type: String, required: true },
  descripcion: { type: String, default: '' },
})
</script>

<template>
  <header class="page-header">
    <div>
      <h1>{{ titulo }}</h1>
      <p v-if="descripcion">{{ descripcion }}</p>
    </div>
    <div class="page-actions"><slot /></div>
  </header>
</template>
