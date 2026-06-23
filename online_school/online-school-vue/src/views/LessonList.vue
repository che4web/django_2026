<script setup>
import { ref, onMounted } from 'vue'
import { Lesson, LessonMaterial } from '@/api.js'
import { useAuthStore } from '@/stores/auth.js'
import LessonFilter from '@/components/LessonFilter.vue'
import { User, Clock, Calendar } from '@lucide/vue'
import moment from 'moment'
const authStore = useAuthStore()
const LessonList = ref([])
const material = ref([])
const filter = ref({
    search: '',
    lesson_type: '',
})

const getLessonList = async () => {
    let res = await Lesson.getList(filter.value)
    console.log(res)
    LessonList.value = res.results
    let res2 = await LessonMaterial.getList()
    material.value = res2.results
}
const getFormatDate = (date) => {
    return moment(date).format('DD.MM.YYYY')
}
onMounted(() => {
    getLessonList()
})
</script>
<template>
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center">
            <h3>Уроки</h3>
            <a v-if="authStore.isTeacher" href="" class="btn btn-primary">Создать урок</a>
        </div>
        <div class="row">
            <div class="col-12">
                <LessonFilter v-model="filter" @submit="getLessonList" />
            </div>
            <template v-if="LessonList.length > 0">
                <template v-for="lesson in LessonList">
                    <div class="col-12">
                        <div class="card mb-4 shadow-sm">
                            <div class="row g-0">
                                <div class="col-12 col-md-4 col-lg-3 border-end">
                                    <div
                                        class="ratio ratio-4x3 bg-light overflow-hidden"
                                        style="border-top-left-radius: 0.375rem"
                                    >
                                        <img
                                            v-if="lesson.image"
                                            :src="lesson.image"
                                            class="w-100 h-100 object-fit-cover"
                                        />
                                        <div
                                            v-else
                                            class="d-flex align-items-center justify-content-center text-body-secondary"
                                        >
                                            Нет фото
                                        </div>
                                    </div>

                                    <div class="ps-3 pe-3 border-top">
                                        <template v-for="material in lesson.materials">
                                            <a
                                                :href="material.file"
                                                target="_blank"
                                                v-if="material.file"
                                                class="small text-body-secondary "
                                                >{{ material.title }}</a
                                            >
                                        </template>
                                    </div>
                                </div>

                                <div class="col-12 col-md-8 col-lg-9">
                                    <div class="card-body h-100 d-flex flex-column">
                                        <div
                                            class="d-flex flex-column flex-lg-row justify-content-between gap-3 mb-3"
                                        >
                                            <div>
                                                <div
                                                    class="d-flex flex-wrap align-items-center gap-2 mb-2"
                                                >
                                                    <span class="badge text-bg-primary"
                                                        >Лекция {{ lesson.position }}</span
                                                    >
                                                    <span class="badge text-bg-secondary">
                                                        {{ lesson.lesson_type_display }}
                                                    </span>
                                                </div>
                                                <h5 class="card-title mb-0">{{ lesson.title }}</h5>
                                            </div>

                                            <div class="d-flex flex-wrap gap-3 text-body-secondary">
                                                <div class="d-flex align-items-center gap-2">
                                                    <User :size="20" aria-hidden="true" />
                                                    <span class="text-body">{{
                                                        lesson.teacher_name
                                                    }}</span>
                                                </div>
                                                <div class="d-flex align-items-center gap-2">
                                                    <Clock :size="20" aria-hidden="true" />
                                                    <span class="text-body"
                                                        >{{ lesson.duration_minutes }} минут</span
                                                    >
                                                </div>
                                                <div class="d-flex align-items-center gap-2">
                                                    <Calendar :size="20" aria-hidden="true" />
                                                    <span class="text-body">{{
                                                        getFormatDate(lesson.lesson_date)
                                                    }}</span>
                                                </div>
                                            </div>
                                        </div>

                                        <p class="card-text text-body-secondary flex-grow-1">
                                            {{ lesson.description }}
                                        </p>

                                        <div class="d-flex justify-content-end gap-2 mt-3">
                                            <RouterLink
                                                class="btn btn-primary"
                                                :to="{
                                                    name: 'lesson-detail',
                                                    params: { id: lesson.id },
                                                }"
                                            >
                                                Перейти
                                            </RouterLink>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </template>
                <!-- <div class="col-4" v-for="lesson in LessonList">
                    <div class="card">
                        <div class="card-body">
                            <div class="d-flex justify-content-between">
                                <h5 class="card-title">{{ lesson.title }}</h5>
                                <div class="d-flex flex-column">
                                    <span class="badge text-bg-primary">{{
                                        lesson.lesson_type_display
                                    }}</span>
                                </div>
                            </div>
                            <p class="card-text">{{ lesson.description }}</p>
                            <p class="card-text">{{ lesson.get_lesson_type_display }}</p>
                            <RouterLink
                                class="btn btn-primary btn-sm"
                                :to="{ name: 'lesson-detail', params: { id: lesson.id } }"
                            >
                                К уроку
                            </RouterLink>
                        </div>
                    </div>
                </div> -->
            </template>
        </div>
    </div>
</template>

<style scoped></style>
