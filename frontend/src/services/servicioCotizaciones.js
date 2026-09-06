import api from './api.js'
export default {
  listar: (params = {}) => api.get('/cotizaciones', { params }),
  obtener: (id) => api.get(`/cotizaciones/${id}`),
  crear: (data) => api.post('/cotizaciones', data),
  actualizar: (id, data) => api.put(`/cotizaciones/${id}`, data),
  eliminar: (id) => api.delete(`/cotizaciones/${id}`),
}
