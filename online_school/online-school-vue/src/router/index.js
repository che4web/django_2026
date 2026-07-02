import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: HomeView,
            children: [
                {
                    path: '',
                    name: 'home',
                    redirect: { name: 'lesson-list' },
                },
                {
                    path: 'lessons',
                    name: 'lesson-list',
                    component: () => import('../views/LessonList.vue'),
                },
                {
                    path: 'lessons/:id',
                    name: 'lesson-detail',
                    component: () => import('../views/LessonDetail.vue'),
                },
                {
                    path: 'lessons/:id/update',
                    name: 'lesson-form',
                    component: () => import('../views/LessonForm.vue'),
                },
                {
                    path: 'lessons/:id/test-pass',
                    name: 'lesson-test-pass',
                    component: () => import('../views/LessonTestPass.vue'),
                },
                {
                    path: 'lessons/create',
                    name: 'lesson-create',
                    component: () => import('../views/LessonCreate.vue')
                },
            ],
        },
    ],
})

export default router
