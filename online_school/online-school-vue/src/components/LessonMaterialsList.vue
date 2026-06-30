<template>
    <div>
        <a v-for="material in lesson.materials" :key="material.id" :href="material.file" target="_blank" class="small text-body-secondary d-flex align-items-center gap-2">
            <span class="text-truncate">{{ material.title }}</span>
            <component :is="material.material_type === 'file' ? File : FileText" :size="16" :color="material.material_type === 'file' ? 'red' : 'blue'" aria-hidden="true" />
        </a>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { File, FileText } from '@lucide/vue';

const props = defineProps({
    lesson: {
        type: Object,
        required: true
    }
})
</script>

<style scoped>

</style>
