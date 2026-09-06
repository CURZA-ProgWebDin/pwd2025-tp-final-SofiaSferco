<script setup>
import { computed } from 'vue'

const propiedades = defineProps({ valor: { type: String, required: true } })
const tono = computed(() => {
  if (propiedades.valor === 'Finalizada') return 'finalizada'
  if (
    [
      'En ejecución',
      'Aceptada',
      'Pagada',
      'Facturada totalmente',
    ].includes(propiedades.valor)
  )
    return 'success'
  if (['Rechazada', 'Cancelada'].includes(propiedades.valor)) return 'danger'
  if (
    [
      'Pendiente',
      'Suspendida',
      'Pagada parcialmente',
      'Facturada parcialmente',
    ].includes(propiedades.valor)
  )
    return 'warning'
  return 'neutral'
})
</script>

<template>
  <span class="status" :class="`status-${tono}`">{{ valor }}</span>
</template>
