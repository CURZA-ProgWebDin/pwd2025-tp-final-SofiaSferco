import api from './api.js'
export default {
  listar: (params = {}) => api.get('/obras', { params }),
  obtener: (id) => api.get(`/obras/${id}`),
  crear: (data) => api.post('/obras', data),
  actualizar: (id, data) => api.put(`/obras/${id}`, data),
  actualizarEjecucion: (id, data) => api.patch(`/obras/${id}`, data),
  eliminar: (id) => api.delete(`/obras/${id}`),
}
