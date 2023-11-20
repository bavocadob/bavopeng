import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/signup',
      name: 'signUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'loginView',
      component: LoginView
    },
  ]
})

export default router
