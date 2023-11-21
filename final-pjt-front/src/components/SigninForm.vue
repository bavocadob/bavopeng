<template>
    <div>
      <div class="h-4/5 flex flex-col justify-center md:justify-evenly items-center">
        <img @click="goMain" class="mb-5 sm:w-1/2 cursor-pointer" src="@/assets/images/Logo2.png" alt="logo">
        <form @submit.prevent="login" class="w-1/2 m-2 text-white">
          <input
            type="text"  placeholder="ID" v-model="username"
            class="w-full h-8 md:h-12 2xl:h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                  focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 
                  disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                  rounded-lg text-gray-950 text-xs md:text-lg 2xl:text-xl font-normal leading-tight"
            :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-500':usernameRequired}"
          >
          <p v-show="usernameRequired">아이디를 입력해주세요.</p>
          <input
            type="password" placeholder="PASSWORD" v-model="password"
            class="w-full h-8 md:h-12 2xl:h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                  focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 
                  disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                  rounded-lg text-gray-950 text-xs md:text-lg 2xl:text-xl font-normal leading-tight"
            :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-500':passwordRequired}"
          >
          <p v-show="passwordRequired">비밀번호를 입력해주세요.</p>
          <button class="w-full h-8 lg:h-10 2xl:h-14 my-5 border border-2 border-blue-700 bg-blue-900 hover:bg-blue-700 rounded-lg cursor-pointer
                        text-center text-white text-xs lg:text-lg 2xl:text-xl font-semibold leading-tight">
            Login
          </button>
          <p v-show="failedLogin" class="text-red-400 text-center">아이디 또는 비밀번호가 잘못되었습니다.</p>
          <p class="text-white text-center">
            회원이 아니신가요?
            <span class=" mx-2 text-blue-100 font-bold">
              <RouterLink :to="{name: 'signup'}">회원가입</RouterLink>
            </span>
          </p>
        </form>
      </div>
  </div>
</template>

<script setup>
import { useUserStore } from '../stores/user'
import { ref, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const store = useUserStore()
const router = useRouter()
const route = useRoute()

const username = ref('')
const password = ref('')
const usernameRequired = ref(false)
const passwordRequired = ref(false)
const failedLogin = ref(false)

watch(username, (inputValue) => {
  if (inputValue === '') {
    usernameRequired.value = true
  }
})

watch(password, (inputValue) => {
  if (inputValue === '') {
    passwordRequired.value = true
  }
})

const login = function () {
  if (username.value && password.value) {
  axios({
      method: 'post',
      url: `${store.API_URL}/dj-rest-auth/login/`,
      data: {
        username: username.value,
        password: password.value
      }
    })
      .then((res) => {
        // console.log(res)
        store.token = res.data.key
        return res.data.key
      })
      .then((token) => {
        store.getUserInfo(token)
      })
      .then(() => {
        router.replace({name: 'main'})
      })
      .catch((err) => {
        // console.log(err)
        failedLogin.value = true
      })
  }}
const goMain = function () {
  router.push({ name: 'main' })
}

</script>

<style scoped>

</style>