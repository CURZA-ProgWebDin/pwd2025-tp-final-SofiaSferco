<script setup>
import { reactive, watch } from 'vue'
import CampoFormulario from '../CampoFormulario.vue'
import { MEDIOS_PAGO } from '../../utils/opciones.js'
import { textoOpcional, textoObligatorio, validarImporte } from '../../utils/formularios.js'
import { formatearMoneda } from '../../utils/formateadores.js'

const propiedades = defineProps({
  facturas: { type: Array, default: () => [] },
  ocupado: Boolean,
})
const emitir = defineEmits(['guardar', 'cancelar'])
const formulario = reactive({
  id_factura: '',
  fecha_pago: '',
  importe: '',
  medio_pago: '',
  observaciones: '',
})
const errores = reactive({})
watch(
  () => formulario.id_factura,
  (id) => {
    const factura = propiedades.facturas.find(
      (item) => item.id_factura === Number(id),
    )
    formulario.importe = factura?.importe ?? ''
  },
)

function guardar() {
  Object.keys(errores).forEach((k) => delete errores[k])
  if (!formulario.id_factura) errores.id_factura = 'Seleccione una factura.'
  if (!formulario.fecha_pago) errores.fecha_pago = 'La fecha es obligatoria.'
  const errorImporte = validarImporte(formulario.importe, 'El importe')
  if (errorImporte) errores.importe = errorImporte
  const factura = propiedades.facturas.find(
    (item) => item.id_factura === Number(formulario.id_factura),
  )
  if (factura && Number(formulario.importe) !== Number(factura.importe))
    errores.importe = 'Debe coincidir con la factura.'
  if (!MEDIOS_PAGO.includes(formulario.medio_pago))
    errores.medio_pago = 'Seleccione un medio.'
  if (formulario.medio_pago === 'Otros' && !textoObligatorio(formulario.observaciones))
    errores.observaciones = 'Las observaciones son obligatorias.'
  if (Object.keys(errores).length) return
  emitir('guardar', {
    id_factura: Number(formulario.id_factura),
    fecha_pago: formulario.fecha_pago,
    importe: Number(formulario.importe),
    medio_pago: formulario.medio_pago,
    observaciones: textoOpcional(formulario.observaciones),
  })
}
</script>

<template>
  <form class="form-card" novalidate @submit.prevent="guardar">
    <p v-if="!facturas.length" class="note">No hay facturas pendientes.</p>
    <div class="form-grid">
      <CampoFormulario label="Factura pendiente" required :error="errores.id_factura">
        <select v-model="formulario.id_factura">
          <option value="">Seleccione…</option>
          <option
            v-for="factura in facturas"
            :key="factura.id_factura"
            :value="factura.id_factura"
          >
            {{ factura.numero_factura }} · {{ formatearMoneda(factura.importe) }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario label="Fecha de pago" required :error="errores.fecha_pago">
        <input v-model="formulario.fecha_pago" type="date" />
      </CampoFormulario>
      <CampoFormulario label="Importe" required :error="errores.importe">
        <input v-model="formulario.importe" type="number" min="0.01" step="0.01" />
      </CampoFormulario>
      <CampoFormulario label="Medio de pago" required :error="errores.medio_pago">
        <select v-model="formulario.medio_pago">
          <option value="">Seleccione…</option>
          <option v-for="method in MEDIOS_PAGO" :key="method">
            {{ method }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario
        label="Observaciones"
        :required="formulario.medio_pago === 'Otros'"
        :error="errores.observaciones"
      >
        <textarea v-model="formulario.observaciones"></textarea>
      </CampoFormulario>
    </div>
    <div class="form-actions">
      <button class="btn btn-neutral" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
      <button class="btn btn-create" :disabled="ocupado || !facturas.length">
        Registrar pago
      </button>
    </div>
  </form>
</template>
