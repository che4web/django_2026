<template>
    <div class="container mt-4" v-if="lessonTest">
        <h1>Пройти тест {{ lessonTest.title }}</h1>
        <div v-for="question, index in lessonTest.questions" :key="question.id">
            <div>{{ index + 1 }}. {{ question.text }}</div>
            <div v-for="answer in question.answers" :key="answer.id">
                <input type="radio" :value="answer.id" v-model="selectedAnswer">
                <label>{{ answer.text }}</label>
            </div>
        </div>
        <button class="btn btn-primary" @click="submitTest">Отправить тест</button>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { LessonTestPublic } from '@/api.js'
const route = useRoute()
const testId = route.params.id
const lessonTest = ref(null)
const getLessonTest = async () => {
    const response = await LessonTestPublic.getById(testId)
    lessonTest.value = response
}
onMounted(getLessonTest)
</script>

<style scoped>

</style>
