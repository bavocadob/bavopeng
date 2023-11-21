import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
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
  ]
})

export default router
