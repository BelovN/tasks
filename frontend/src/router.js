import RegisterForm from './components/RegisterForm.vue'
import LoginForm from './components/LoginForm.vue'
import WeekBoard from "./components/WeekBoard.vue";


export default [
    { path: '/', component: WeekBoard},
    { path: '/register', component: RegisterForm },
    { path: '/auth', component: LoginForm },
]
