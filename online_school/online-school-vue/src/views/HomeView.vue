<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { Lesson, LessonMaterial } from "@/api.js"
import NavBar from "@/components/NavBar.vue"

const LessonList = ref([])
const material = ref([])
const search = ref('')

const getLessonList = async () => {
  let res = await Lesson.getList({ search: search.value })
  console.log(res)
  LessonList.value = res.results
  let res2 = await LessonMaterial.getList()
  material.value = res2.results
}
onMounted(() => {
  getLessonList()
})

</script>
<template>
  <NavBar />
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


<style scoped></style>
