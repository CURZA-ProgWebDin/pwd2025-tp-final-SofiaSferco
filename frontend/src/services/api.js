import axios from 'axios'

const urlApi = import.meta.env.VITE_API_URL?.trim()
if (!urlApi)
  throw new Error(
    'Falta configurar VITE_API_URL. Cree frontend/.env a partir de frontend/.env.example.',
  )

const api = axios.create({
  baseURL: urlApi,
  headers: { 'Content-Type': 'application/json' },
  timeout: 15000,
})

export function obtenerErrorApi(error) {
  if (error.response?.data?.error) return error.response.data.error
  if (error.code === 'ECONNABORTED')
    return 'La solicitud demoró demasiado. Intente nuevamente.'
  if (!error.response) return 'No se pudo conectar con el servidor.'
  return 'Ocurrió un error inesperado. Intente nuevamente.'
}

export default api
