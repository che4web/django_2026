<script setup>
import { ref, onMounted, computed } from 'vue';
import {useAuthStore} from '@/stores/auth.js'

const authStore = useAuthStore();
const csrfToken = computed(() => {
  const cookie = document.cookie
    .split('; ')
    .find((row) => row.startsWith('csrftoken='))
  return cookie ? decodeURIComponent(cookie.split('=')[1]) : ''
})


onMounted(()=>{
    if (!authStore.isLoaded) {
        authStore.loadCurrentUser();
    }
});
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
          <span class="text-body-secondary small">{{ authStore.displayName }}</span>
          <form v-if="authStore.isAuthenticated" method="post" action="/accounts/logout/" class="mb-0">
            <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken">
            <button type="submit" class="btn btn-outline-secondary btn-sm">Выйти</button>
          </form>
          <a v-else class="btn btn-primary btn-sm" href="/accounts/login/">Войти</a>
        </div>
      </div>
    </div>
  </nav>
</template>
