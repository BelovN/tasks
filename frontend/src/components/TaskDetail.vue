<template>
  <div class="modal-overlay" @click.self="close">
    <div class="modal">
      <h3>{{ task.title }}</h3>
      <p><strong>Описание:</strong></p>
      <p class="wrapped-text">{{ task.description }}</p>
      <p><strong>Ответственный:</strong> {{ task.responsible }}</p>
      <p><strong>Дата:</strong> {{ task.on_date }}</p>
      <p><strong>Выполнено:</strong> {{ task.is_done ? 'Да' : 'Нет' }}</p>

      <div class="comments">
        <h4>Комментарии</h4>
        <ul class="comment-list">
          <li v-for="(c, i) in task.comments || []" :key="i">{{ c }}</li>
        </ul>
        <div class="comment-form">
          <input
              v-model="newComment"
              @keydown.enter.prevent="addComment"
              placeholder="Добавить комментарий"
          />
          <button @click="addComment">Добавить</button>
        </div>
      </div>

      <div class="actions">
        <button @click="emit('edit', task)">Редактировать</button>
        <button @click="emit('delete', task)">Удалить</button>
        <button @click="toggleDone">
          {{ task.is_done ? 'Восстановить' : 'Завершить' }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({ task: Object })
const task = props.task

const emit = defineEmits(['close', 'edit', 'delete'])

const newComment = ref('')

const addComment = () => {
  if (newComment.value.trim()) {
    if (!task.comments) task.comments = []
    task.comments.push(newComment.value.trim())
    newComment.value = ''
  }
}

const toggleDone = () => {
  task.is_done = !task.is_done
}

const close = () => emit('close')
</script>
