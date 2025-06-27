<template>
  <div class="auth-page">
    <div class="auth-form">
      <h2>Авторизация</h2>

      <div class="form-group">
        <label for="username">Логин</label>
        <InputText v-model="form.username" id="username" class="input" />
      </div>

      <div class="form-group">
        <label for="password">Пароль</label>
        <Password v-model="form.password" id="password" toggleMask :feedback="false" class="input" />
      </div>

      <Button label="Войти" class="submit-button" @click="loginFunc" />

      <div class="redirect-link">
        Нет аккаунта?
        <Button label="Регистрация" text severity="secondary" @click="goToRegister" class="redirect-button"/>
      </div>

      <Toast />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useToast } from 'primevue/usetoast'
import { login } from '@/services/auth.js'

const toast = useToast()
const router = useRouter()

const form = ref({
  username: '',
  password: '',
})

const loginFunc = async () => {
  try {
    await login({
      username: form.value.username,
      password: form.value.password
    })
    router.push('/')
  } catch (err) {
    const detail = err.response?.data?.detail || 'Проверьте данные'
    toast.add({ severity: 'error', summary: 'Ошибка при входе', detail: detail, life: 3000 })
  }
}

const goToRegister = () => {
  router.push('/register')
}

</script>
