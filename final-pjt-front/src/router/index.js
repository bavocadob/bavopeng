import { createRouter, createWebHistory } from 'vue-router'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleEditView from '@/views/ArticleEditView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import MainView from '@/views/MainView.vue'
import UserView from '@/views/UserView.vue'
// import MovieView from '@/views/MovieView.vue'
import CommunityView from '@/views/CommunityView.vue'
import MovieReviewListView from '@/views/MovieReviewListView.vue'
import ProfileView from '@/views/ProfileView.vue'
import FollowView from '@/views/FollowView.vue'

import { useUserStore } from '@/stores/user'



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
      component: UserView,
      meta: { notRequiresAuth: true }
    },
    {
      path: '/signin',
      name: 'signin',
      component: UserView,
      meta: { notRequiresAuth: true }
    },
    // {
    //   path: '/movie',
    //   name: 'movieView',
    //   component: MovieView
    // },
    {
      path: '/article/create',
      name: 'articleCreate',
      component: ArticleCreateView,
      meta: { requiresAuth: true }
    },
    {
      path: '/community/:articleId/edit',
      name: 'articleEdit',
      component: ArticleEditView,
      meta: { requiresAuth: true }
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
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/profile/:username/modify',
      name: 'profileModify',
      component: ProfileView,
      meta: { requiresAuth: true }
    },
    {
      path: '/prefer',
      name: 'prefer',
      component: UserView,
      meta: { requiresAuth: true }
    },
    {
      path: '/follow/:id',
      name: 'following',
      component: FollowView
    },
    {
      path: '/follow/:id',
      name: 'follower',
      component: FollowView
    },
  ]
})


router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const store = useUserStore()
    // 로그인이 필요한 페이지에 로그인하지 않고 들어간 경우 로그인 페이지로 이동
    if (store.token == null) {
      next({
        name: 'signin',
      })
    } else {
      next()
    }
  } else if (to.matched.some(record => record.meta.notRequiresAuth)) {
    const store = useUserStore()
    if (store.token !== null) {
      next({
        name: 'main',
      })
    } else {
      next()
    }
  } else {
    next()
  }


})

export default router
