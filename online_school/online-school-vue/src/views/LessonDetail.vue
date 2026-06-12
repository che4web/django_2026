<script setup>
import { ref, onMounted } from 'vue'
import NavBar from "@/components/NavBar.vue"
import { useRoute } from 'vue-router'
import { Lesson } from "@/api.js"
const route = useRoute()

const lesson = ref(null)
const getLesson = async () => {
    lesson.value = await Lesson.getById(route.params.id)
}
onMounted(getLesson)
</script>

<template>
    <NavBar />
    <div class="container mt-4">
        <div class="d-flex align-items-center justify-content-between mb-4 mt-4" v-if="lesson">
        <div>
            <h1 class="h3">{{ lesson.title }}</h1>
            <p class="text-body-secondary">{{ lesson.description }}</p>
        </div>
    </div>
    </div>
</template>
