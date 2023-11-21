import { createRouter, createWebHistory } from 'vue-router'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MainView from '@/views/MainView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import MovieView from '@/views/MovieView.vue'
import CommunityView from '@/views/CommunityView.vue'



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
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/community/:articleId',
      name: 'articleDetail',
      component: ArticleDetailView
    },
  ]
})

export default router
