import { createRouter, createWebHistory } from 'vue-router'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MainView from '@/views/MainView.vue'
import UserView from '@/views/UserView.vue'
import MovieView from '@/views/MovieView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MovieReviewListView from '@/views/MovieReviewListView.vue'
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
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/community/:articleId',
      name: 'articleDetail',
      component: ArticleDetailView
    },
    {
      path: '/movie/:movieId/reviews',
      name: 'reviewList',
      component: MovieReviewListView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView
    },
    {
      path: '/profile/:username/modify',
      name: 'profileModify',
      component: ProfileView
    },
    {
      path: '/prefer',
      name: 'prefer',
      component: UserView
    },
  ]
})

export default router
