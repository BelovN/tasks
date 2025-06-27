<template>
  <div class="container">
    <div class="header">
      <button @click="prevWeek">&lt;</button>
      <h2>{{ currentWeekRange }}</h2>
      <button @click="nextWeek">&gt;</button>
    </div>

    <div class="board">
      <div class="day-column" v-for="(day, index) in week" :key="index">
        <div class="day-header">
          <div class="top-row">
            <div class="date">{{ formatDate(day.date) }}</div>
            <button class="add-task-button" @click="openCreateModal(day.date)">+</button>
          </div>
          <div class="label">{{ day.label }}</div>
        </div>

        <div class="tasks">
          <TaskCard
              v-for="(task, i) in day.tasks"
              :key="i"
              :task="task"
              @click="openTaskModal(task, index)"
              @done="() => markTaskAsDone(day, i)"
          />
        </div>
      </div>
    </div>

    <TaskDetail
        v-if="isModalVisible"
        :task="selectedTask"
        :comments="selectedTask?.comments || []"
        @close="closeTaskModal"
        @save="saveTaskChanges"
        @delete="deleteTask"
        @edit="editTask"
    />

    <TaskCreate
        v-if="isAddModalVisible"
        :default-date="createDate"
        :task="taskToEdit"
        :mode="createMode"
        @close="closeCreateModal"
        @create="createTask"
        @update="updateTask"
    />
  </div>
</template>

<script setup>
import TaskCard from '@/components/TaskCard.vue'
import TaskDetail from '@/components/TaskDetail.vue'
import TaskCreate from '@/components/TaskCreate.vue'
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import dayjs from 'dayjs'
import isBetween from 'dayjs/plugin/isBetween'

dayjs.extend(isBetween)

const week = ref([])
const currentOffset = ref(0)

const loadTasksForWeek = async (offset = 0) => {
  const start = dayjs().startOf('week').add(offset, 'week')
  const end = start.add(6, 'day')

  const { data } = await axios.get('http://localhost:8000/api/v1/tasks/', {
    params: { week: start.format('YYYY-MM-DD') }
  })

  return Array.from({ length: 7 }, (_, i) => {
    const day = start.add(i, 'day')
    const dayStr = day.format('YYYY-MM-DD')
    return {
      date: day,
      label: day.locale('ru').format('dddd'),
      tasks: data.filter(t => t.on_date === dayStr)
    }
  })
}

const refreshWeek = async () => {
  week.value = await loadTasksForWeek(currentOffset.value)
}
onMounted(refreshWeek)

const nextWeek = async () => {
  currentOffset.value++
  await refreshWeek()
}
const prevWeek = async () => {
  currentOffset.value--
  await refreshWeek()
}

const formatDate = (date) => date.format('DD.MM.YYYY')

const currentWeekRange = computed(() => {
  if (week.value.length === 0) return ''
  const start = week.value[0].date.format('DD.MM')
  const end = week.value[6].date.format('DD.MM')
  return `${start} – ${end}`
})

const markTaskAsDone = (day, taskIndex) => {
  day.tasks.splice(taskIndex, 1)
}

const selectedTask = ref(null)
const selectedDayIndex = ref(null)
const isModalVisible = ref(false)

const openTaskModal = (task, dayIndex) => {
  selectedTask.value = task
  selectedDayIndex.value = dayIndex
  isModalVisible.value = true
}
const closeTaskModal = () => {
  selectedTask.value = null
  selectedDayIndex.value = null
  isModalVisible.value = false
}
const saveTaskChanges = (updatedTask) => {
  if (selectedDayIndex.value !== null) {
    const tasks = week.value[selectedDayIndex.value].tasks
    const index = tasks.findIndex(t => t.id === updatedTask.id)
    if (index !== -1) tasks[index] = { ...updatedTask }
  }
  closeTaskModal()
}
const deleteTask = () => {
  if (selectedDayIndex.value !== null) {
    const tasks = week.value[selectedDayIndex.value].tasks
    const index = tasks.findIndex(t => t === selectedTask.value)
    if (index !== -1) tasks.splice(index, 1)
  }
  closeTaskModal()
}

const isAddModalVisible = ref(false)
const createDate = ref('')
const createMode = ref('create')
const taskToEdit = ref(null)

const openCreateModal = (dateObj) => {
  createDate.value = dayjs(dateObj).format('YYYY-MM-DD')
  createMode.value = 'create'
  taskToEdit.value = null
  isAddModalVisible.value = true
}
const closeCreateModal = () => {
  isAddModalVisible.value = false
  createMode.value = 'create'
  taskToEdit.value = null
}

const createTask = (task) => {
  const dayIndex = week.value.findIndex(day => day.date.format('YYYY-MM-DD') === task.on_date)
  if (dayIndex !== -1) {
    week.value[dayIndex].tasks.push(task)
  }
}

const editTask = (task) => {
  createMode.value = 'edit'
  taskToEdit.value = { ...task }
  isAddModalVisible.value = true
}

const updateTask = (updatedTask) => {
  const dayIndex = week.value.findIndex(d =>
      d.tasks.some(t => t.id === updatedTask.id)
  )
  if (dayIndex !== -1) {
    const taskIndex = week.value[dayIndex].tasks.findIndex(t => t.id === updatedTask.id)
    if (taskIndex !== -1) {
      week.value[dayIndex].tasks[taskIndex] = { ...updatedTask }
    }
  }
  closeCreateModal()
  closeTaskModal()
}
</script>
