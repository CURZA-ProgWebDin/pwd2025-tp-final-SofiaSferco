<script setup>
import { reactive, watch } from 'vue'
import CampoFormulario from '../CampoFormulario.vue'
import CamposEjecucionObra from '../CamposEjecucionObra.vue'
import { TIPOS_DOCUMENTO } from '../../utils/opciones.js'
import {
  textoOpcional,
  textoObligatorio,
  validarImporte,
  validarEjecucionObra,
} from '../../utils/formularios.js'

const propiedades = defineProps({
  inicial: { type: Object, default: () => ({}) },
  cotizaciones: { type: Array, default: () => [] },
  editando: Boolean,
  ocupado: Boolean,
})
const emitir = defineEmits(['guardar', 'cancelar'])
const formulario = reactive({
  id_cotizacion: '',
  titulo: '',
  monto_contratado: '',
  fecha_estimada_fin: '',
  tipo_documento: '',
  numero_documento: '',
  fecha_documento: '',
  estado_ejecucion: 'Pendiente',
  fecha_inicio: '',
  fecha_fin: '',
  motivo_estado: '',
})
const errores = reactive({})
watch(
  () => propiedades.inicial,
  (v) =>
    Object.assign(formulario, {
      id_cotizacion: v.id_cotizacion || '',
      titulo: v.titulo || '',
      monto_contratado: v.monto_contratado ?? '',
      fecha_estimada_fin: v.fecha_estimada_fin || '',
      tipo_documento: v.tipo_documento || '',
      numero_documento: v.numero_documento || '',
      fecha_documento: v.fecha_documento || '',
      estado_ejecucion: v.estado_ejecucion || 'Pendiente',
      fecha_inicio: v.fecha_inicio || '',
      fecha_fin: v.fecha_fin || '',
      motivo_estado: v.motivo_estado || '',
    }),
  { immediate: true },
)
function cambioCotizacion() {
  const seleccionado = propiedades.cotizaciones.find(
    (item) => item.id_cotizacion === Number(formulario.id_cotizacion),
  )
  if (seleccionado) formulario.titulo = seleccionado.titulo
}
function guardar() {
  Object.keys(errores).forEach((k) => delete errores[k])
  if (!propiedades.editando && !formulario.id_cotizacion)
    errores.id_cotizacion = 'Seleccione una cotización.'
  if (!textoObligatorio(formulario.titulo)) errores.titulo = 'El título es obligatorio.'
  const errorImporte = validarImporte(
    formulario.monto_contratado,
    'El monto contratado',
  )
  if (errorImporte) errores.monto_contratado = errorImporte
  const valoresDocumento = [
    formulario.tipo_documento,
    formulario.numero_documento.trim(),
    formulario.fecha_documento,
  ]
  if (valoresDocumento.some(Boolean) && !valoresDocumento.every(Boolean))
    errores.tipo_documento =
      'Complete los tres datos del documento o déjelos vacíos.'
  if (propiedades.editando) Object.assign(errores, validarEjecucionObra(formulario))
  if (Object.keys(errores).length) return
  const datosEnvio = {
    titulo: textoObligatorio(formulario.titulo),
    monto_contratado: Number(formulario.monto_contratado),
    fecha_estimada_fin: formulario.fecha_estimada_fin || null,
    tipo_documento: textoOpcional(formulario.tipo_documento),
    numero_documento: textoOpcional(formulario.numero_documento),
    fecha_documento: formulario.fecha_documento || null,
  }
  if (!propiedades.editando) datosEnvio.id_cotizacion = Number(formulario.id_cotizacion)
  else
    Object.assign(datosEnvio, {
      estado_ejecucion: formulario.estado_ejecucion,
      fecha_inicio: formulario.fecha_inicio || null,
      fecha_fin: formulario.fecha_fin || null,
      motivo_estado: textoOpcional(formulario.motivo_estado),
    })
  emitir('guardar', datosEnvio)
}
</script>
<template>
  <form class="form-card" novalidate @submit.prevent="guardar">
    <p v-if="!editando && !cotizaciones.length" class="note">
      No hay cotizaciones aceptadas sin obra.
    </p>
    <div class="form-grid">
      <CampoFormulario
        v-if="!editando"
        label="Cotización de origen"
        required
        :error="errores.id_cotizacion"
      >
        <select v-model="formulario.id_cotizacion" @change="cambioCotizacion">
          <option value="">Seleccione…</option>
          <option
            v-for="cotizacion in cotizaciones"
            :key="cotizacion.id_cotizacion"
            :value="cotizacion.id_cotizacion"
          >
            {{ cotizacion.codigo_cotizacion }} · {{ cotizacion.titulo }}
          </option>
        </select>
      </CampoFormulario>
      <CampoFormulario label="Título" required :error="errores.titulo">
        <input v-model="formulario.titulo" />
      </CampoFormulario>
      <CampoFormulario
        label="Monto contratado"
        required
        :error="errores.monto_contratado"
      >
        <input
          v-model="formulario.monto_contratado"
          type="number"
          min="0.01"
          step="0.01"
        />
      </CampoFormulario>
      <CampoFormulario label="Fecha estimada de finalización">
        <input v-model="formulario.fecha_estimada_fin" type="date" />
      </CampoFormulario>
    </div>
    <section v-if="editando" class="form-section">
      <h2>Seguimiento de ejecución</h2>
      <CamposEjecucionObra :modelo="formulario" :errores="errores" />
    </section>
    <section class="form-section">
      <h2>Documento contractual</h2>
      <div class="form-grid">
        <CampoFormulario label="Tipo" :error="errores.tipo_documento">
          <select v-model="formulario.tipo_documento">
            <option value="">Seleccione si corresponde…</option>
            <option v-for="type in TIPOS_DOCUMENTO" :key="type">
              {{ type }}
            </option>
          </select>
        </CampoFormulario>
        <CampoFormulario label="Número">
          <input v-model="formulario.numero_documento" />
        </CampoFormulario>
        <CampoFormulario label="Fecha">
          <input v-model="formulario.fecha_documento" type="date" />
        </CampoFormulario>
      </div>
    </section>
    <div class="form-actions">
      <button class="btn btn-neutral" type="button" @click="$emit('cancelar')">
        Cancelar
      </button>
      <button
        class="btn btn-create"
        :disabled="ocupado || (!editando && !cotizaciones.length)"
      >
        {{ editando ? 'Guardar cambios' : 'Crear obra' }}
      </button>
    </div>
  </form>
</template>
