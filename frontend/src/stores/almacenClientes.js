import { defineStore } from 'pinia'
import servicioClientes from '../services/servicioClientes.js'
import { usarEstadoRecurso } from './estadoRecurso.js'
export const usarAlmacenClientes = defineStore('clientes', () =>
  usarEstadoRecurso(servicioClientes),
)
