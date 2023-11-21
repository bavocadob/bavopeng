import { createRouter, createWebHistory } from 'vue-router'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MainView from '@/views/MainView.vue'
import UserView from '@/views/UserView.vue'
import MovieView from '@/views/MovieView.vue'
import ProfileView from '@/views/ProfileView.vue'


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
      name: 'signup',
      component: UserView
    },
    {
      path: '/signin',
      name: 'signin',
      component: UserView
    },
    {
      path: '/movie',
      name: 'movieView',
      component: MovieView
    },
    {
      path: '/article/create',
      name: 'articleCreate',
      component: ArticleCreateView
    },
    {
      path: '/movie/:movieId',
      name: 'movieDetail',
      component: MovieDetailView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView
    },
  ]
})

export default router
