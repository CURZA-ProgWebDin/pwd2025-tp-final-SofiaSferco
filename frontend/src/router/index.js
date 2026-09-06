import { createRouter, createWebHistory } from 'vue-router'

const rutas = [
  {
    path: '/',
    name: 'inicio',
    component: () => import('../views/VistaInicio.vue'),
  },
  {
    path: '/clientes',
    name: 'clientes',
    component: () => import('../views/clientes/VistaListaClientes.vue'),
  },
  {
    path: '/clientes/nuevo',
    name: 'cliente-crear',
    component: () => import('../views/clientes/VistaCrearCliente.vue'),
  },
  {
    path: '/clientes/:id/editar',
    name: 'cliente-editar',
    component: () => import('../views/clientes/VistaEditarCliente.vue'),
  },
  {
    path: '/cotizaciones',
    name: 'cotizaciones',
    component: () => import('../views/cotizaciones/VistaListaCotizaciones.vue'),
  },
  {
    path: '/cotizaciones/nueva',
    name: 'cotizacion-crear',
    component: () => import('../views/cotizaciones/VistaCrearCotizacion.vue'),
  },
  {
    path: '/cotizaciones/:id/editar',
    name: 'cotizacion-editar',
    component: () => import('../views/cotizaciones/VistaEditarCotizacion.vue'),
  },
  {
    path: '/obras',
    name: 'obras',
    component: () => import('../views/obras/VistaListaObras.vue'),
  },
  {
    path: '/obras/nueva',
    name: 'obra-crear',
    component: () => import('../views/obras/VistaCrearObra.vue'),
  },
  {
    path: '/obras/:id/editar',
    name: 'obra-editar',
    component: () => import('../views/obras/VistaEditarObra.vue'),
  },
  {
    path: '/facturas',
    name: 'facturas',
    component: () => import('../views/facturas/VistaListaFacturas.vue'),
  },
  {
    path: '/facturas/nueva',
    name: 'factura-crear',
    component: () => import('../views/facturas/VistaCrearFactura.vue'),
  },
  {
    path: '/facturas/:id/editar',
    name: 'factura-editar',
    component: () => import('../views/facturas/VistaEditarFactura.vue'),
  },
  {
    path: '/pagos',
    name: 'pagos',
    component: () => import('../views/pagos/VistaListaPagos.vue'),
  },
  {
    path: '/pagos/nuevo',
    name: 'pago-crear',
    component: () => import('../views/pagos/VistaCrearPago.vue'),
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'no-encontrada',
    component: () => import('../views/VistaNoEncontrada.vue'),
  },
]

export default createRouter({
  history: createWebHistory(),
  routes: rutas,
  scrollBehavior: () => ({ top: 0 }),
})
