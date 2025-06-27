<template>
  <div :class="['task', { done: task.is_done }]">
    <div class="content">
      <div class="title">
        {{ task.title.length > 20 ? task.title.slice(0, 40) + '…' : task.title }}
      </div>
      <div class="description">
        {{ task.description.length > 40 ? task.description.slice(0, 40) + '…' : task.description }}
      </div>
      <div class="responsible">👤 {{ task.responsible }}</div>
    </div>
  </div>
</template>

<script setup>
defineProps({ task: Object })
const emit = defineEmits(['done'])
const toggleDone = () => emit('done')
</script>
