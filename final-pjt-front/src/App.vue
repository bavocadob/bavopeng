<template>
  <div>
    <div class="w-screen bg-blue-950">
      <div class="w-screen bg-black bg-opacity-10">
      <nav
        v-show="!fullScreen" 
        class="w-screen h-20 fixed top-0 bg-blue-950 flex justify-between items-center z-50"
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
        </div>
        <div class="w-[540px] h-12 me-12 justify-end items-center gap-4 inline-flex">
            <form>
              <input 
                type="text" id="search" placeholder="검색"
                class="text-white text-base font-medium px-4
                      w-[340px] h-10 bg-slate-900 rounded-[100px] border border-2 border-blue-900"
              >
            </form>
            <RouterLink :to="{ name: 'signin' }">로그인</RouterLink>
            <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
            <div v-if="store.isLogin" @click="profielDropdown=!profielDropdown" class="relative">
              <div>
                <img v-if="profileImg" class="w-10 h-10 rounded-full bg-slate-50" :src="profileUrl" />
                <img v-else class="w-10 h-10 rounded-full bg-slate-50" src="./assets/images/anonymous_square.png" />
                
              </div>
              <div v-show="profielDropdown" class="absolute right-0 top-14">
                <UserProfileDropdown />
              </div>
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
  <!-- <test/> -->
  </template>


<script setup>
import UserProfileDropdown from '@/components/UserProfileDropdown.vue'
import { ref, watch, computed } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { useUserStore } from './stores/user'
// import test from './views/test.vue'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const profielDropdown = ref(false)
const profileUrl = ref(null)

const goMain = function () {
  router.push({ name: 'main' })
}

const fullScreen = computed(() => {
  const checkRoutes = ['signin', 'signup']
  return checkRoutes.includes(route.name)
})

const profileImg = computed(() => {
  profileUrl.value = store.API_URL + store.userInfo.profile.profile_img
  return store.userInfo.profile.profile_img ? true : false
})

</script>


<style scoped>

</style>
