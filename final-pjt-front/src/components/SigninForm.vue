<template>
    <div>
      <div class="w-[400px] h-4/5 flex flex-col justify-center justify-evenly items-center">
        <img @click="goMain" class="mb-5  cursor-pointer" src="@/assets/images/Logo2.png" alt="logo">
        <form @submit.prevent="login" class="w-full m-2 text-white">
          <div class="my-2">
            <input
            type="text"  placeholder="ID" v-model="username"
            class="w-full h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
            focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 text-black 
            rounded-lg text-gray-950 text-xl font-normal leading-tight"
            :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-500':usernameRequired}"
            >
            <p v-show="usernameRequired" class="text-red-400">아이디를 입력해주세요.</p>
          </div>
          <div class="my-2">
            <input
            type="password" placeholder="PASSWORD" v-model="password" 
            class="w-full h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                  focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 text-black
                  rounded-lg text-gray-950 text-xl font-normal leading-tight"
            :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-500':passwordRequired}"
            >
            <p v-show="passwordRequired" class="text-red-400">비밀번호를 입력해주세요.</p>
          </div>
            <button class="w-full h-12 my-2 bg-blue-900 hover:bg-blue-700 rounded-lg cursor-pointer
            disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none disabled:cursor-default
            text-center text-white text-xl font-semibold leading-tight"
            :disabled="(passwordRequired || usernameRequired)" 
            >Login
          </button>
          <p v-show="failedLogin" class="text-red-400 text-center">아이디 또는 비밀번호가 잘못되었습니다.</p>
          <p class="text-white text-center cursor-default">
            회원이 아니신가요?
            <span class=" mx-2 text-slate-50 underline font-bold">
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
  } else {
    usernameRequired.value = false
  }
})

watch(password, (inputValue) => {
  if (inputValue === '') {
    passwordRequired.value = true
  } else {
    passwordRequired.value = false
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
  } else {
    if (username.value === '') {
      usernameRequired.value = true
    } if (password.value === '') {
      passwordRequired.value = true
    }
  }}
const goMain = function () {
  router.push({ name: 'main' })
}

</script>

<style scoped>

</style>