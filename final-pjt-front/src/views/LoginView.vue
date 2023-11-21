<template>
    <div class="w-screen h-screen bg-[url('@/assets/images/loginbg.jpg')] bg-cover">
      <div class="w-screen h-screen px-10 bg-blue-950 bg-opacity-90 flex flex-col justify-center items-center">
        <div class="w-2/3 lg:w-2/5 h-4/5 flex flex-col justify-center md:justify-evenly items-center">
          <img @click="goMain" class="mb-5 w-2/3 sm:w-1/2 cursor-pointer" src="@/assets/images/Logo2.png" alt="logo">
          <form @submit.prevent="login" class="text-center m-2">
            <input
              type="text"  placeholder="ID" v-model="username"
              class="w-3/4 h-8  md:h-12 2xl:h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                    focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 
                    disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                    invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500
                    rounded-lg text-gray-950 text-xs md:text-lg 2xl:text-xl font-normal leading-tight"
            >
            <input
              type="password" placeholder="PASSWORD" v-model="password"
              class="w-3/4 h-8  md:h-12 2xl:h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                    focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 
                    disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                    invalid:border-pink-500 invalid:text-pink-600 focus:invalid:border-pink-500 focus:invalid:ring-pink-500
                    rounded-lg text-gray-950 text-xs md:text-lg 2xl:text-xl font-normal leading-tight"
            >
            <button class="w-3/4 h-8 lg:h-10 2xl:h-14 my-5 border border-2 border-blue-700 bg-blue-900 hover:bg-blue-700 rounded-lg cursor-pointer
                          text-center text-white text-xs lg:text-lg 2xl:text-xl font-semibold leading-tight">
              Login
            </button>
          </form>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/user'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}

const goMain = function () {
  router.push({ name: 'main' })
}

</script>

<style scoped>

</style>