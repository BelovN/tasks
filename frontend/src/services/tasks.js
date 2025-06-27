import axios from 'axios'

const loadTasksForWeek = async (offset = 0) => {
    const start = dayjs().startOf('week').add(offset, 'week')
    const end = start.add(6, 'day')

    // Получаем все задачи за период
    const { data } = await axios.get('/api/v1/tasks/', {
        params: {
            // фильтрация по ответственному, если нужно
        }
    })

    // Фильтруем вручную задачи, попавшие в нужную неделю
    const tasksInRange = data.filter(task =>
        dayjs(task.on_date).isBetween(start.subtract(1, 'day'), end.add(1, 'day'), null, '[]')
    )

    // Раскладываем по дням недели
    return Array.from({ length: 7 }, (_, i) => {
        const day = start.add(i, 'day')
        const dayStr = day.format('YYYY-MM-DD')
        return {
            date: day,
            label: day.locale('ru').format('dddd'),
            tasks: tasksInRange.filter(t => t.on_date === dayStr)
        }
    })
}