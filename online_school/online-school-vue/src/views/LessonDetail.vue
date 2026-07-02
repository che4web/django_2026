<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Lesson } from '@/api.js'
import { ChevronLeft, Calendar, User, Clock } from '@lucide/vue'
import moment from 'moment'
import LessonMaterialsList from '@/components/LessonMaterialsList.vue'
const route = useRoute()
const router = useRouter()

const lesson = ref(null)
const getLesson = async () => {
    lesson.value = await Lesson.getById(route.params.id)
}
const goBack = () => {
    router.push({ name: 'lesson-list' })
}
const getFormatDate = (date) => {
    return moment(date).format('DD.MM.YYYY')
}
onMounted(getLesson)

const deleteLessen = async () => {
    await Lesson.delete(lesson.value)
    router.push({ name: 'lesson-list' })
}
</script>

<template>
    <div class="container mt-4" v-if="lesson">
        <div class="d-flex align-items-center mb-4">
            <button
                class="btn btn-outline-secondary d-flex align-items-center gap-2"
                @click="goBack"
            >
                <ChevronLeft :size="20" />
                Назад
            </button>
            <router-link
                class="btn btn-primary"
                tag="button"
                :to="{ name: 'lesson-form', params: { id: lesson.id } }"
            >
                редактирован
            </router-link>
            <button class="btn btn-danger" @click="deleteLessen">удалить</button>
        </div>
        <div
            class="d-flex flex-column flex-lg-row justify-content-between gap-3 mb-3"
            v-if="lesson"
        >
            <div>
                <div class="d-flex flex-wrap alignt-items-center gap-2 mb-3">
                    <span class="badge text-bg-primary">{{ lesson.lesson_type_display }}</span>
                </div>
                <h1 class="h3 mb-0">{{ lesson.title }}</h1>
            </div>
            <div class="d-flex align-items-center gap-2 text-body-secondary">
                <Calendar :size="20" aria-hidden="true" />
                <span class="text-body">{{ getFormatDate(lesson.lesson_date) }}</span>
            </div>
        </div>
        <div class="d-flex flex-wrap gap-3 text-body-secondary mb-4" v-if="lesson">
            <div class="d-flex align-items-center gap-2">
                <User :size="20" aria-hidden="true" />
                <span>{{ lesson.teacher_name }}</span>
            </div>
            <div class="d-flex align-items-center gap-2">
                <Clock :size="20" aria-hidden="true" />
                <span>{{ lesson.duration_minutes }} минут</span>
            </div>
        </div>
        <div class="row mb-4">
            <div class="col-12">
                <div class="card h-100">
                    <div class="ratio ratio-16x9 bg-body-tertiary" v-if="lesson.videos">
                        <video :src="lesson.videos[0]?.file" class="w-100 h-100" controls></video>
                    </div>
                    <div v-else>видео нет</div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h4 mb-3">Материалы</h2>
                        <LessonMaterialsList :lesson="lesson" />
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h4 mb-3">Описание</h2>
                        <div>{{ lesson.description }}</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-12">
                <div class="card mb-4">
                    <div class="card-body">
                        <h2 class="h4 mb-3">Тесты</h2>
                        <div v-for="test in lesson.tests" :key="test.id">
                            <div class="d-flex justify-content-between">
                                <h3 class="h5 mb-3">{{ test.title }}</h3>
                                <button
                                    class="btn btn-primary"
                                    @click="
                                        router.push({
                                            name: 'lesson-test-pass',
                                            params: { id: test.id },
                                        })
                                    "
                                >
                                    Пройти тест
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
