import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import Aura from '@primeuix/themes/aura';
import InputText from 'primevue/inputtext'
import Password from 'primevue/password'
import Button from 'primevue/button'
import ToastService from 'primevue/toastservice'
import Toast from 'primevue/toast'
import { createRouter, createWebHistory } from 'vue-router'
import routes from './router'

const app = createApp(App);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    }
});
app.use(ToastService)

app.component('InputText', InputText)
app.component('Password', Password)
app.component('Button', Button)
app.component('Toast', Toast)
app.use(createRouter({ history: createWebHistory(), routes }))
app.mount('#app')
