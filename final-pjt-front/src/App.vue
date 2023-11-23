<template>
  <div>
    <div class="w-screen bg-blue-950">
      <div class="w-screen bg-black bg-opacity-10">
      <nav
        v-show="!fullScreen" 
        class="w-screen h-20 fixed top-0 bg-blue-950 z-20"
      > 
        <div class="flex justify-between items-center me-8 p-4">
          <div class="ms-5 flex items-center">
            <div class="w-32 flex items-center me-4">
              <img @click="goMain" alt="main" class="cursor-pointer" src="@/assets/images/Logo2.svg" width="150" height="50" >
            </div>
            <div class="max-md:hidden flex items-center gap-4 text-center align-top text-white text-base font-semibold leading-normal">
              <RouterLink :to="{ name: 'main' }">Movie</RouterLink>
              <RouterLink :to="{ name: 'community' }">Community</RouterLink> 
            </div>
          </div>
          <div class="flex max-md:hidden justify-end items-center gap-4">
            <MovieSearchBar />
            <div v-if="store.isLogin" @click="profielDropdown=!profielDropdown" class="relative">
              <div>
                <img v-if="profileImg" class="w-10 h-10 rounded-full bg-slate-50" :src="profileUrl" />
                <img v-else class="w-10 h-10 rounded-full bg-slate-50" src="./assets/images/anonymous_square.png" />
              </div>
              <div v-show="profielDropdown" class="absolute right-0 top-14">
                <UserProfileDropdown />
              </div>
            </div>
            <div v-else class="text-white flex gap-4">
              <RouterLink :to="{ name: 'signin' }">로그인</RouterLink>
              <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
            </div>
          </div>
          <!-- 햄버거 -->
          <div @click="menuToggle=!menuToggle" class="md:hidden flex items-center">
            <button>
              <img v-show="!menuToggle" src="@/assets/images/view-list.svg" class="w-8" alt="hamberger-btn">
              <img v-show="menuToggle" src="@/assets/images/x.svg" class="w-8" alt="hamberger-btn">
            </button>
          </div>
        </div>
        <div v-show="menuToggle" class="md:hidden bg-blue-950 text-xl text-white font-semibold">
          <div class="flex flex-col border-b border-t">
            <RouterLink :to="{ name: 'main' }" class="hover:bg-blue-900 px-6 py-4">Movie</RouterLink>
            <RouterLink :to="{ name: 'community' }" class="hover:bg-blue-900 px-6 py-4">Community</RouterLink> 
          </div>
          <div v-if="!store.isLogin" class="flex flex-col border-b">
            <RouterLink :to="{ name: 'signin' }" class="hover:bg-blue-900 px-6 py-4">로그인</RouterLink>
            <RouterLink :to="{ name: 'signup' }" class="hover:bg-blue-900 px-6 py-4">회원가입</RouterLink>
          </div>
          <div v-else class="flex flex-col border-b">
            <a class="hover:hover:bg-blue-900 px-6 py-4" :href="`http://localhost:5173/profile/${store.userInfo.username}`">
              내 프로필
            </a>
            <span 
              @click="logout" class="hover:bg-blue-900 hover:cursor-pointer px-6 py-4"
            >
              로그아웃
            </span>
          </div>
        </div>
      </nav>
      <div class="min-h-screen relative">
        <div :class="{'w-9/12 mx-auto py-28': !fullScreen}">
          <RouterView />
        </div>
        <footer v-show="!fullScreen" class="w-screen h-20 absolute bottom-0 left-0 border border-black"></footer>
      </div>
      </div>
    </div>
  </div>
  </template>


<script setup>
import UserProfileDropdown from '@/components/UserProfileDropdown.vue'
import { ref, watch, computed } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { useUserStore } from './stores/user'
import MovieSearchBar from '@/components/MovieSearchBar.vue'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const profielDropdown = ref(false)
const menuToggle = ref(false)
const profileUrl = ref(null)

const goMain = function () {
  router.push({ name: 'main' })
}

const fullScreen = computed(() => {
  const checkRoutes = ['signin', 'signup', 'prefer']
  return checkRoutes.includes(route.name)
})

const profileImg = computed(() => {
  profileUrl.value = store.API_URL + store.userInfo.profile?.profile_img
  return store.userInfo.profile?.profile_img ? true : false
})

const logout = function () {
  store.logout()
}

</script>


<style scoped>

</style>
