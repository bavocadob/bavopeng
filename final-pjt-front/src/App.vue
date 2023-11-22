<template>
  <div>
    <div class="w-screen bg-blue-950">
      <div class="w-screen bg-black bg-opacity-10">
      <nav
        v-show="!fullScreen" 
        class="w-screen h-20 fixed top-0 bg-blue-950 flex justify-between items-center z-20"
      >
        <div class="w-[500px] ms-5 flex justify-around items-center">
          <img @click="goMain" alt="main" class="cursor-pointer" src="@/assets/images/Logo2.svg" width="150" height="50" >
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            <RouterLink :to="{ name: 'movieView' }">Movie</RouterLink>
          </div>
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            <RouterLink :to="{ name: 'community' }">Community</RouterLink> 
          </div>
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            Wishlist
            <!-- <RouterLink>Wishlist</RouterLink> -->
          </div>
          <button @click="logout">로그아웃</button>
        </div>
        <div class="w-[540px] h-12 me-12 justify-end items-center gap-4 inline-flex">
            <MovieSearchBar />
            <RouterLink :to="{ name: 'signin' }">로그인</RouterLink>
            <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
            <img class="w-[50px] h-[50px] left-[1150px] top-0 rounded-full" src="https://via.placeholder.com/50x50" />
            <RouterLink :to="{name: 'profile', params: {username: 'test01'}}">프로필</RouterLink>
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
  <!-- <test/> -->
  </template>


<script setup>
import { ref, watch, computed } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { useUserStore } from './stores/user'
import MovieSearchBar from '@/components/MovieSearchBar.vue'
import test from './views/test.vue'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const goMain = function () {
  router.push({ name: 'main' })
}

const logout = function () {
  store.logout()
}

const fullScreen = computed(() => {
  const checkRoutes = ['signin', 'signup']
  return checkRoutes.includes(route.name)
})

</script>


<style scoped>

</style>
