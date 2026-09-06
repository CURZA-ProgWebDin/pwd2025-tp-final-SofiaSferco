<script setup>
import CampoFormulario from './CampoFormulario.vue'
import {
  ESTADOS_OBRA,
  requiereFechaInicio,
  requiereFechaFin,
  requiereMotivo,
} from '../utils/opciones.js'
defineProps({
  modelo: { type: Object, required: true },
  errores: { type: Object, default: () => ({}) },
})
</script>
<template>
  <div class="form-grid">
    <CampoFormulario
      label="Estado de ejecución"
      required
      :error="errores.estado_ejecucion"
    >
      <select v-model="modelo.estado_ejecucion">
        <option v-for="estado in ESTADOS_OBRA" :key="estado">{{ estado }}</option>
      </select>
    </CampoFormulario>
    <CampoFormulario
      label="Fecha de inicio"
      :required="requiereFechaInicio(modelo.estado_ejecucion)"
      :error="errores.fecha_inicio"
    >
      <input v-model="modelo.fecha_inicio" type="date" />
    </CampoFormulario>
    <CampoFormulario
      label="Fecha de finalización"
      :required="requiereFechaFin(modelo.estado_ejecucion)"
      :error="errores.fecha_fin"
    >
      <input v-model="modelo.fecha_fin" type="date" />
    </CampoFormulario>
    <CampoFormulario
      label="Motivo del estado"
      :required="requiereMotivo(modelo.estado_ejecucion)"
      :error="errores.motivo_estado"
    >
      <textarea v-model="modelo.motivo_estado" rows="3"></textarea>
    </CampoFormulario>
  </div>
</template>
