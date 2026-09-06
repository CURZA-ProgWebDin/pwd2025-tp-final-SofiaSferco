import { defineStore } from 'pinia'
import servicioFacturas from '../services/servicioFacturas.js'
import { usarEstadoRecurso } from './estadoRecurso.js'
export const usarAlmacenFacturas = defineStore('facturas', () =>
  usarEstadoRecurso(servicioFacturas),
)
