<template>
    <form method="get" class="card card-body mb-4" @submit.prevent="getLessonList">
        <div class="row align-items-end">
            <div class="col-md-4">
                <label>Название урока</label>
                <input
                    type="text"
                    v-model="filter.search"
                    name="search"
                    class="form-control"
                    placeholder="Название урока"
                />
            </div>
            <div class="col-md-4">
                <label>Тип урока</label>
                <select
                    v-model="filter.lesson_type"
                    id="lesson-type"
                    name="lesson_type"
                    class="form-select"
                >
                    <option value="">Все</option>
                    <option v-for="type in lessonTypes" :value="type.value" :key="type.value">
                        {{ type.label }}
                    </option>
                </select>
            </div>
            <div class="col-3">
                <button type="submit" class="btn btn-primary">показать</button>
                <button type="button" class="btn btn-secondary ms-1" @click="resetFilter">
                    сбросить
                </button>
            </div>
        </div>
    </form>
</template>

<script setup>
import {ref, onMounted, watch} from 'vue'
import { LessonTypes } from '@/api.js'

const emit = defineEmits(['submit'])
const filter = defineModel({ type: Object, required: true })
const lessonTypes = ref([])
const getLessonTypes = async () => {
    lessonTypes.value = await LessonTypes.getList()
}
const resetFilter = () => {
    filter.value = {
        search: '',
        lesson_type: ''
    }
    emit('submit')
}
onMounted(() => {
    getLessonTypes()
})
watch(filter.value, () => {
    emit('submit'), { deep: true }
})
</script>

<style scoped></style>
