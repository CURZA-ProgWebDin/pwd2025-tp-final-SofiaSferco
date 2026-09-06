import { defineStore } from 'pinia'
import servicioCotizaciones from '../services/servicioCotizaciones.js'
import { usarEstadoRecurso } from './estadoRecurso.js'
export const usarAlmacenCotizaciones = defineStore('cotizaciones', () =>
  usarEstadoRecurso(servicioCotizaciones),
)
