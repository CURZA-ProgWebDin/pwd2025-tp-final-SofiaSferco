import api from './api.js'
export default {
  listar: (params = {}) => api.get('/facturas', { params }),
  obtener: (id) => api.get(`/facturas/${id}`),
  crear: (data) => api.post('/facturas', data),
  actualizar: (id, data) => api.put(`/facturas/${id}`, data),
  eliminar: (id) => api.delete(`/facturas/${id}`),
}
