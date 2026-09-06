<script setup>
import { onMounted, reactive, ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useRoute, useRouter } from 'vue-router'
import EncabezadoPagina from '../../components/EncabezadoPagina.vue'
import AlertaAplicacion from '../../components/AlertaAplicacion.vue'
import EstadoCarga from '../../components/EstadoCarga.vue'
import EstadoVacio from '../../components/EstadoVacio.vue'
import DialogoConfirmacion from '../../components/DialogoConfirmacion.vue'
import InsigniaEstado from '../../components/InsigniaEstado.vue'
import CamposEjecucionObra from '../../components/CamposEjecucionObra.vue'
import { usarAlmacenObras } from '../../stores/almacenObras.js'
import {
  mostrarValor,
  formatearMoneda,
  formatearFecha,
} from '../../utils/formateadores.js'
import { textoOpcional, validarEjecucionObra } from '../../utils/formularios.js'
const almacen = usarAlmacenObras()
const { elementos, cargando, cargado, error } = storeToRefs(almacen)
const ruta = useRoute()
const enrutador = useRouter()
const eliminando = ref(null)
const seguimiento = ref(null)
const confirmarSeguimiento = ref(false)
const erroresLocales = reactive({})
const exito = ref(String(ruta.query.message || ''))
const ejecucion = reactive({
  estado_ejecucion: '',
  fecha_inicio: '',
  fecha_fin: '',
  motivo_estado: '',
})
function cargar() {
  almacen.obtenerTodos().catch(() => {})
}
onMounted(cargar)
function abrirSeguimiento(obra) {
  seguimiento.value = obra
  Object.assign(ejecucion, {
    estado_ejecucion: obra.estado_ejecucion,
    fecha_inicio: obra.fecha_inicio || '',
    fecha_fin: obra.fecha_fin || '',
    motivo_estado: obra.motivo_estado || '',
  })
  Object.keys(erroresLocales).forEach((k) => delete erroresLocales[k])
}
function solicitarSeguimiento() {
  Object.keys(erroresLocales).forEach((k) => delete erroresLocales[k])
  Object.assign(erroresLocales, validarEjecucionObra(ejecucion))
  if (!Object.keys(erroresLocales).length) confirmarSeguimiento.value = true
}
async function guardarSeguimiento() {
  try {
    const resultado = await almacen.actualizarEjecucion(seguimiento.value.id_obra, {
      estado_ejecucion: ejecucion.estado_ejecucion,
      fecha_inicio: ejecucion.fecha_inicio || null,
      fecha_fin: ejecucion.fecha_fin || null,
      motivo_estado: textoOpcional(ejecucion.motivo_estado),
    })
    confirmarSeguimiento.value = false
    seguimiento.value = null
    exito.value = resultado.message
    await almacen.obtenerTodos()
  } catch {
    confirmarSeguimiento.value = false
  }
}
async function eliminar() {
  try {
    const resultado = await almacen.eliminar(eliminando.value.id_obra)
    eliminando.value = null
    exito.value = resultado.message
    await almacen.obtenerTodos()
  } catch {
    eliminando.value = null
  }
}
function cerrarExito() {
  exito.value = ''
  if (ruta.query.message) enrutador.replace({ query: {} })
}
</script>
<template>
  <div>
    <EncabezadoPagina
      titulo="Obras"
      descripcion="Seguimiento operativo, facturación y cobro."
    >
      <RouterLink class="btn btn-create" to="/obras/nueva">
        Crear obra
      </RouterLink>
    </EncabezadoPagina>
    <AlertaAplicacion :mensaje="exito" tipo="success" @cerrar="cerrarExito" />
    <AlertaAplicacion :mensaje="error" @cerrar="almacen.limpiarError" />
    <EstadoCarga v-if="cargando && !elementos.length" />
    <EstadoVacio
      v-else-if="!cargado && !elementos.length"
      titulo="No se pudieron cargar las obras"
    >
      <button class="btn btn-primary" @click="cargar">Reintentar</button>
    </EstadoVacio>
    <EstadoVacio v-else-if="!elementos.length" titulo="No hay obras" />
    <div v-else class="obra-list">
      <article v-for="obra in elementos" :key="obra.id_obra" class="obra-card">
        <header class="obra-header">
          <div class="obra-header-main">
            <div class="obra-header-metadata">
              <strong class="obra-code">{{ obra.codigo_obra }}</strong>
              <span class="obra-document">
                Documento: {{ mostrarValor(obra.tipo_documento) }} ·
                {{ mostrarValor(obra.numero_documento) }}
              </span>
            </div>
            <h2>{{ obra.titulo }}</h2>
            <p>{{ obra.razon_social }} · {{ obra.codigo_cotizacion }}</p>
          </div>
          <div class="obra-status">
            <InsigniaEstado :valor="obra.estado_ejecucion" />
          </div>
        </header>
        <div class="money-grid">
          <div>
            <small>Contratado</small>
            <strong>{{ formatearMoneda(obra.monto_contratado) }}</strong>
          </div>
          <div>
            <small>Facturado</small>
            <strong>{{ formatearMoneda(obra.total_facturado) }}</strong>
          </div>
          <div>
            <small>Por facturar</small>
            <strong>{{ formatearMoneda(obra.saldo_por_facturar) }}</strong>
          </div>
          <div>
            <small>Cobrado</small>
            <strong>{{ formatearMoneda(obra.total_cobrado) }}</strong>
          </div>
          <div>
            <small>Por cobrar</small>
            <strong>{{ formatearMoneda(obra.saldo_por_cobrar) }}</strong>
          </div>
        </div>
        <div class="details">
          <p>
            <strong>Facturación:</strong>
            <InsigniaEstado :valor="obra.estado_facturacion" />
          </p>
          <p>
            <strong>Inicio:</strong>
            {{ formatearFecha(obra.fecha_inicio) }}
          </p>
          <p>
            <strong>Fin real:</strong>
            {{ formatearFecha(obra.fecha_fin) }}
          </p>
          <p>
            <strong>Cobro:</strong>
            <InsigniaEstado :valor="obra.estado_cobro" />
          </p>
          <p>
            <strong>Fin estimado:</strong>
            {{ formatearFecha(obra.fecha_estimada_fin) }}
          </p>
          <p>
            <strong>Motivo:</strong>
            {{ mostrarValor(obra.motivo_estado) }}
          </p>
        </div>
        <footer>
          <button class="btn btn-small btn-primary" @click="abrirSeguimiento(obra)">
            Actualizar ejecución
          </button>
          <template v-if="!obra.tiene_facturas">
            <RouterLink
              class="btn btn-small btn-primary"
              :to="`/obras/${obra.id_obra}/editar`"
            >
              Editar
            </RouterLink>
            <button class="btn btn-small btn-danger" @click="eliminando = obra">
              Eliminar
            </button>
          </template>
          <small v-else class="obra-blocked-message">
            Datos generales bloqueados por facturas
          </small>
        </footer>
      </article>
    </div>
    <Teleport to="body">
      <div
        v-if="seguimiento"
        class="dialog-backdrop"
        @click.self="seguimiento = null"
      >
        <section class="dialog wide">
          <h2>Actualizar ejecución</h2>
          <CamposEjecucionObra :modelo="ejecucion" :errores="erroresLocales" />
          <div class="form-actions">
            <button class="btn btn-neutral" @click="seguimiento = null">
              Cancelar
            </button>
            <button class="btn btn-primary" @click="solicitarSeguimiento">
              Revisar cambio
            </button>
          </div>
        </section>
      </div>
    </Teleport>
    <DialogoConfirmacion
      :abierto="confirmarSeguimiento"
      titulo="Confirmar cambio de estado"
      mensaje="¿Confirma que desea cambiar el estado de la obra?"
      texto-confirmacion="Guardar"
      :ocupado="cargando"
      @cancelar="confirmarSeguimiento = false"
      @confirmar="guardarSeguimiento"
    />
    <DialogoConfirmacion
      :abierto="!!eliminando"
      peligro
      titulo="Eliminar obra"
      :mensaje="`¿Confirma que desea eliminar ${eliminando?.codigo_obra}?`"
      texto-confirmacion="Eliminar"
      :ocupado="cargando"
      @cancelar="eliminando = null"
      @confirmar="eliminar"
    />
  </div>
</template>
