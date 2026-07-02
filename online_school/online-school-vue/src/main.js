import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from 'axios'
import 'bootstrap/dist/css/bootstrap.css'
import App from './App.vue'
import router from './router'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

const app = createApp(App)
app.use(createPinia())
app.use(router)

app.mount('#app')
