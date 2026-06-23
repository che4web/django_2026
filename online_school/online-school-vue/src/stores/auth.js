import { computed, ref } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore('auth', () => {
    const currentUser = ref(null);
    const isLoaded = ref(false);

    const isAuthenticated = computed(() => Boolean(currentUser.value))
    const isTeacher = computed(() => currentUser.value?.user.is_teacher)
    const displayName = computed(() => currentUser.value?.user.full_name || currentUser.value?.username)

    async function loadCurrentUser() {
        try {
            const response = await axios.get('/api/users/me/')
            currentUser.value = response.data
        }catch {
            currentUser.value = null
        }finally {
            isLoaded.value = true
        }
    }
    return { currentUser, isLoaded, isAuthenticated, isTeacher, displayName, loadCurrentUser }
})
