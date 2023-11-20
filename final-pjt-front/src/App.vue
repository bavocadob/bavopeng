<template>
  <div>
    <div class="w-screen bg-blue-950">
      <nav
        v-show="route.name !== 'loginView'" 
        class="w-screen h-20 cursor-pointer flex justify-between items-center"
      >
        <div class="w-[500px] ms-5 flex justify-around items-center">
          <img @click="goMain" alt="" src="@/assets/images/Logo2.svg" width="150" height="50" >
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            <RouterLink :to="{ name: 'movieView' }">Movie</RouterLink>
          </div>
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            Coummunity
            <!-- <RouterLink>Community</RouterLink> -->
          </div>
          <div class="text-center align-top text-white text-base font-semibold leading-normal">
            Wishlist
            <!-- <RouterLink>Wishlist</RouterLink> -->
          </div>
          <button @click="logout">로그아웃</button>
        </div>
        <div class="w-[540px] h-12 me-7 justify-end items-center gap-4 inline-flex">
            <form>
              <input 
                type="text" id="search" placeholder="검색"
                class="text-white text-base font-medium px-4
                      w-[340px] h-10 bg-slate-900 rounded-[100px] border border-2 border-blue-900"
              >
            </form>
            <RouterLink :to="{ name: 'loginView' }">로그인</RouterLink>
            <RouterLink :to="{ name: 'signUpView' }">회원가입</RouterLink>
            <img class="w-[50px] h-[50px] left-[1150px] top-0 rounded-full" src="https://via.placeholder.com/50x50" />
        </div>
      </nav>
      <div class="w-11/12 mx-auto mt-5 mb-20">
        <RouterView />
      </div>
      <footer class="w-screen h-20 bottom-0 border border-black"></footer>
    </div>
  </div>
  <!-- <test/> -->
  </template>


<script setup>
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { useUserStore } from './stores/user'
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

</script>


<style scoped>

</style>
