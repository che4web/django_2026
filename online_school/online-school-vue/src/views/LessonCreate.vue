<script setup>
import { ref, onMounted } from 'vue'
import { User, LessonTypes, Lesson } from '@/api.js'
import toFormData from '@/assets/form.js'
import { useRouter } from 'vue-router'
const router = useRouter()
const form = ref({
    title: '',
    description: '',
    teacher: '',
    duration_minutes: '',
    lesson_date: '',
    position: '',
    is_published: true,
    lesson_type: 'theory',
    image: null,
})
const teachers = ref([])
const getTeachers = async () => {
    const response = await User.getTeacher()
    teachers.value = response
}
const lessonTypes = ref([])
const getLessonTypes = async () => {
    const response = await LessonTypes.getList()
    lessonTypes.value = response
}
const setFile = (event, target, field) => {
    target[field] = event.target.files[0] || null
}
const saveLesson = async () => {
    const response = await Lesson.save(toFormData(form.value))
    router.push({ name: 'lesson-detail', params: { id: response.id } })
}
onMounted(() => {
    getTeachers()
    getLessonTypes()
})
</script>
<template>
    <div class="container mt-4">
        <h1>Создание урока</h1>
        <form @submit.prevent="saveLesson">
            <div class="card">
                <div class="card-body">
                    <h5>Основная информация</h5>
                    <div class="row">
                        <div class="col-12">
                            <label for="title" class="form-label">Название</label>
                            <input type="text" class="form-control" id="title" v-model="form.title">
                        </div>
                        <div class="col-12">
                            <label for="description" class="form-label">Описание</label>
                            <textarea class="form-control" id="description" v-model="form.description"></textarea>
                        </div>
                        <div class="col-12">
                            <label for="teacher" class="form-label">Преподаватель</label>
                            <select class="form-control" id="teacher" v-model="form.teacher">
                                <option v-for="teacher in teachers" :value="teacher.id">{{ teacher.name }}</option>
                            </select>
                        </div>
                        <div class="col-12">
                            <label for="lesson_type" class="form-label">Тип урока</label>
                            <select class="form-control" id="lesson_type" v-model="form.lesson_type">
                                <option v-for="lessonType in lessonTypes" :value="lessonType.value">{{ lessonType.label }}</option>
                            </select>
                        </div>
                        <div class="col-12">
                            <label for="duration_minutes" class="form-label">Длительность в минутах</label>
                            <input type="number" class="form-control" id="duration_minutes" v-model="form.duration_minutes">
                        </div>
                        <div class="col-12">
                            <label for="lesson_date" class="form-label">Дата урока</label>
                            <input type="date" class="form-control" id="lesson_date" v-model="form.lesson_date">
                        </div>
                        <div class="col-12">
                            <label for="position" class="form-label">Позиция</label>
                            <input type="number" class="form-control" id="position" v-model="form.position">
                        </div>
                        <div class="col-12">
                            <label for="image" class="form-label">Превью урока</label>
                            <input type="file" class="form-control" id="image" @change="setFile($event, form, 'image')">
                        </div>
                        <div class="col-12">
                            <label for="is_published" class="form-label">Опубликован</label>
                            <input type="checkbox" class="form-check-input" id="is_published" v-model="form.is_published">
                        </div>
                        <div class="col-12">
                            <button class="btn btn-primary" type="submit">Сохранить</button>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</template>

<style scoped>

</style>
