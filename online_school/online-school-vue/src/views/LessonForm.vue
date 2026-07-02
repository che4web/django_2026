<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { Lesson } from '@/api.js'
import { ChevronLeft, Calendar, User, Clock } from '@lucide/vue'
import moment from 'moment'
import LessonMaterialsList from '@/components/LessonMaterialsList.vue'
const route = useRoute()
const router = useRouter()

const lesson = ref({})
const getLesson = async () => {
  lesson.value = await Lesson.getById(route.params.id)
}
const goBack = () => {
  router.push({ name: 'lesson-list' })
}
const getFormatDate = (date) => {
  return moment(date).format('DD.MM.YYYY')
}
const errors = ref({})
const save = async () => {
  console.log("save")
  try {
    lesson.value = await Lesson.save(lesson.value)
    router.push({ name: "lesson-detail", params: { id: lesson.value.id } })
  } catch (e) {
    errors.value = e.response.data
    console.log(e.response.data)
  }
}
onMounted(getLesson)
</script>
<template>

  <div class="container mt-4">
    <h1> Редактирование урока {{ lesson?.id }}</h1>
    <div class="row">
      <div class="alert alert-danger" v-if="errors.title">{{ errors.title }} </div>
      <div class="col-2"><label> Название урока</label></div>
      <div class="col-10"><input class="form-control" v-model="lesson.title"></div>
    </div>
    <div class="row">
      <div class="col-2"><label> Опубликован</label></div>
      <div class="col-10"><input v-model="lesson.is_published" type="checkbox"></div>
    </div>
    <button class="btn btn-primary" @click="save"> сохранить </button>
  </div>
</template>
