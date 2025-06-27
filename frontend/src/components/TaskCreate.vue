<script setup>
import { ref, watch } from 'vue'

const emit = defineEmits(['close', 'create', 'update'])

const props = defineProps({
  task: Object, // задача для редактирования (если есть)
  mode: {
    type: String,
    default: 'create' // 'create' или 'edit'
  },
  defaultDate: String
})

const task = ref({
  title: '',
  description: '',
  responsible: '',
  on_date: '',
  is_done: false,
  comments: []
})

// следим за props и инициализируем task
watch(
    () => [props.task, props.mode, props.defaultDate],
    () => {
      if (props.mode === 'edit' && props.task) {
        task.value = { ...props.task }
      } else {
        task.value = {
          title: '',
          description: '',
          responsible: '',
          on_date: props.defaultDate || '',
          is_done: false,
          comments: []
        }
      }
    },
    { immediate: true }
)

const submit = () => {
  if (!task.value.title.trim()) return
  const payload = { ...task.value }
  if (props.mode === 'edit') {
    emit('update', payload)
  } else {
    emit('create', payload)
  }
  emit('close')
}
</script>

<template>
  <div class="modal-overlay" @click.self="emit('close')">
    <div class="modal">
      <h3>{{ mode === 'edit' ? 'Редактировать задачу' : 'Новая задача' }}</h3>
      <div class="form">
        <input v-model="task.title" placeholder="Название" />
        <input v-model="task.description" placeholder="Описание" />
        <input v-model="task.responsible" placeholder="Ответственный" />
        <input type="date" v-model="task.on_date" />
      </div>

      <div class="actions">
        <button @click="submit">{{ mode === 'edit' ? 'Сохранить' : 'Создать' }}</button>
        <button @click="emit('close')">Отмена</button>
      </div>
    </div>
  </div>
</template>
