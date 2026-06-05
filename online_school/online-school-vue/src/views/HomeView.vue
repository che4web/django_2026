<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const LessonList = ref([])

const getLessonList = async () => {
    let res = await axios.get('/lessons/lesson-json/')
    LessonList.value = res.data
}
onMounted(() => {
    getLessonList()
})

</script>
<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container">
            <a class="navbar-brand">Online School</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link">Уроки</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link">Создать урок</a>
                    </li>
                </ul>
                <div class="d-flex align-items-center gap-2">
                    <!-- <span class="text-body-secondary small">Вы вошли как {{ user.username }}</span> -->
                    <form method="post" class="mb-0">
                        <button type="submit" class="btn btn-outline-secondary btn-sm">Выйти</button>
                    </form>
                    <a class="btn btn-primary btn-sm">Войти</a>
                </div>
            </div>
        </div>
    </nav>

    <div v-if="LessonList.length > 0" class="container mt-4">
        <div class="d-flex justify-content-between align-items-center">
            <h3>Уроки</h3>
            <a href="" class="btn btn-primary">Создать урок</a>
        </div>
        <div class="row">
            <form method="get" class="card card-body mb-4">
                <div class="row align-items-center">
                    <div class="col-md-4">
                        <label>Тип урока</label>
                        <select id="lesson-type" name="lesson_type" class="form-select">
                            <option value="">Все</option>
                            <option value="">
                            </option>
                        </select>
                    </div>
                    <div class="col-2">
                        <button type="submit" class="btn btn-primary">показать</button>
                        <a href="" class="btn btn-secondary">сбросить</a>
                    </div>
                </div>
            </form>

            <div class="col-4" v-for="lesson in LessonList">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{{ lesson.title }}</h5>
                        <p class="card-text">{{ lesson.description }}</p>
                        <p class="card-text">{{ lesson.get_lesson_type_display }}</p>
                        <a href="" class="btn btn-primary">К уроку</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<style></style>
