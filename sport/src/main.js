import { createApp } from 'vue'
import './assets/styles/style.css'
import 'swiper/css';
import 'swiper/css/pagination';
import { createHead } from '@unhead/vue/client'
import App from './App.vue'

const app = createApp(App)
const head = createHead()
app.use(head)

app.mount('#app')
