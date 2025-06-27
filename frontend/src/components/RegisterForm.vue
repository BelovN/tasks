<template>
  <div class="auth-page">
    <div class="auth-form">
      <h2>Регистрация</h2>

      <div class="form-group">
        <label for="username">Логин</label>
        <InputText v-model="form.username" id="username" class="input" />
      </div>

      <div class="form-group">
        <label for="password">Пароль</label>
        <Password v-model="form.password" id="password" toggleMask :feedback="false" class="input" />
      </div>

      <div class="form-group">
        <label for="confirm">Повторите пароль</label>
        <Password v-model="form.confirm" id="confirm" toggleMask :feedback="false" class="input" />
      </div>

      <Button label="Зарегистрироваться" class="submit-button" @click="registerFunc" />

      <div class="redirect-link">
        Уже есть аккаунт?
        <Button label="Вход" text severity="secondary" @click="goToAuth" class="redirect-button"/>
      </div>

      <Toast />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useToast } from 'primevue/usetoast'
import { useRouter } from 'vue-router'
import { register } from '@/services/auth.js'

const router = useRouter()


const toast = useToast()

const form = ref({
  username: '',
  password: '',
  confirm: ''
})

const registerFunc = async () => {
  if (form.value.password !== form.value.confirm) {
    toast.add({ severity: 'warn', summary: 'Ошибка', detail: 'Пароли не совпадают', life: 3000 })
    return
  }
  try {
    await register({
      username: form.value.username,
      password: form.value.password,
      confirm: form.value.confirm}
    )
    toast.add({ severity: 'success', summary: 'Успех', detail: 'Регистрация прошла успешно', life: 3000 })
    router.push('/')

  } catch (err) {
    const detail = err.response?.data?.detail || 'Проверьте данные'
    toast.add({ severity: 'error', summary: 'Ошибка при входе', detail: detail, life: 3000 })
  }
}

const goToAuth = () => {
  router.push('/auth')
}
</script>
