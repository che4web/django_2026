<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Lesson, LessonMaterial, LessonTypes } from "@/api.js"
import NavBar from "@/components/NavBar.vue"
import {useAuthStore} from '@/stores/auth.js'
const authStore = useAuthStore();
const LessonList = ref([])
const material = ref([])
const search = ref('')

const lessonType = ref('')
const lessonTypes = ref([])
const getLessonTypes = async () => {
    lessonTypes.value = await LessonTypes.getList()
}

const getLessonList = async () => {
    let res = await Lesson.getList({ search: search.value, lesson_type: lessonType.value })
    console.log(res)
    LessonList.value = res.results
    let res2 = await LessonMaterial.getList()
    material.value = res2.results
}
onMounted(() => {
    getLessonList()
    getLessonTypes()
})

</script>
<template>
    <NavBar />
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center">
            <h3>Уроки</h3>
            <a v-if="authStore.isTeacher" href="" class="btn btn-primary" >Создать урок</a>
        </div>
        <div class="row">
            <form method="get" class="card card-body mb-4" @submit.prevent="getLessonList">
                <div class="row align-items-center">
                    <div class="col-md-4">
                        <label>Тип урока</label>
                        <select v-model="lessonType" id="lesson-type" name="lesson_type" class="form-select">
                            <option value="">Все</option>
                            <option v-for="type in lessonTypes" :value="type.value" :key="type.value"> {{ type.label }}
                            </option>
                        </select>
                    </div>
                    <div class="col-2">
                        <button type="submit" class="btn btn-primary">показать</button>
                        <a href="" class="btn btn-secondary">сбросить</a>
                    </div>
                </div>
            </form>
            <template v-if="LessonList.length > 0">

                <div class="col-4" v-for="lesson in LessonList">
                    <div class="card">
                        <div class="card-body">
                            <div class="d-flex justify-content-between ">
                                <h5 class="card-title">{{ lesson.title }}</h5>
                                <div class="d-flex flex-column">
                                    <span class="badge text-bg-primary">{{ lesson.lesson_type_display }}</span>

                                </div>
                            </div>
                            <p class="card-text">{{ lesson.description }}</p>
                            <p class="card-text">{{ lesson.get_lesson_type_display }}</p>
                            <RouterLink class="btn btn-primary btn-sm" :to="{name: 'lesson-detail', params: {id: lesson.id}}">
                                К уроку
                            </RouterLink>
                        </div>
                    </div>
                </div>
            </template>
        </div>
    </div>
</template>


<style scoped></style>
