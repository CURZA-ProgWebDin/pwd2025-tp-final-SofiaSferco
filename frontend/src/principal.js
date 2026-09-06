import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Aplicacion from './Aplicacion.vue'
import enrutador from './router/index.js'
import './assets/estilos-principales.css'

createApp(Aplicacion).use(createPinia()).use(enrutador).mount('#app')
