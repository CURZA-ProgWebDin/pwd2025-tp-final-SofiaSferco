import api from './api.js'
export default {
  listar: () => api.get('/pagos'),
  obtener: (id) => api.get(`/pagos/${id}`),
  crear: (data) => api.post('/pagos', data),
  eliminar: (id) => api.delete(`/pagos/${id}`),
}
