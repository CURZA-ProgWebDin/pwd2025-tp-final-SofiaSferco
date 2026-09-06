<script setup>
import { RouterLink, RouterView } from 'vue-router'

const enlaces = [
  { to: '/', label: 'Inicio' },
  { to: '/clientes', label: 'Clientes' },
  { to: '/cotizaciones', label: 'Cotizaciones' },
  { to: '/obras', label: 'Obras' },
  { to: '/facturas', label: 'Facturas' },
  { to: '/pagos', label: 'Pagos' },
]
</script>

<template>
  <div class="app-shell">
    <aside class="sidebar">
      <RouterLink class="brand" to="/">
        <img class="brand-mark" src="/app-logo.png" alt="" />
        <span>
          <strong>Sistema de Gestión</strong>
          <small>de Obras</small>
        </span>
      </RouterLink>
      <nav aria-label="Navegación principal">
        <RouterLink v-for="link in enlaces" :key="link.to" :to="link.to">
          {{ link.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="main-content">
      <RouterView />
    </main>
  </div>
</template>
