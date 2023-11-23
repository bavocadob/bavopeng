<template>
    <div>
      <div class="w-[800px] h-[600px] bg-blue-200 bg-opacity-20 rounded-lg overflow-hidden">
        <div class="w-full h-full bg-white bg-opacity-70 grid grid-rows-5 grid-flow-col gap-2">
          <div class="w-80 row-span-5 flex flex-col justify-center items-center">
            <div class="">
              <h1 class="text-5xl text-center font-semibold text-blue-950">Welcome!</h1>
              <img @click="goMain" src="@/assets/images/Logo.png" alt="logo" class="w-60 my-10 cursor-pointer">
            </div>
          </div>
          <div class="w-96 row-span-4 flex flex-col justify-end">
            <!-- <div class="basis-1/4 text-2xl"> -->
            <!-- </div> -->
            <form @submit.prevent="signUp">
              <div class="flex flex-col my-2">
                <label for="username" class="font-semibold">아이디</label>
                <input
                  type="text" id="username" placeholder="ID" v-model="username"
                  class="h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                        focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 text-black 
                        rounded-lg text-gray-950 text-xl font-normal leading-tight"
                        :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-200':!isValidUsername}"
                >
                <p class="text-emerald-700" :class="{'text-pink-700':!isValidUsername}">{{ checkIdMessage }}</p>
              </div>
              <div class="flex flex-col my-2">
                <label for="password1" class="font-semibold">비밀번호</label>
                <input
                  type="password" id="password1" placeholder="PASSWORD" v-model="password1" 
                  class="h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                        focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 text-black
                        rounded-lg text-gray-950 text-xl font-normal leading-tight"
                        :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-200':!isValidPassword1}"
                >
                <p class="text-emerald-700" :class="{'text-pink-700':!isValidPassword1}">{{ checkPwMessage1 }}</p>
              </div>
              <div class="flex flex-col my-2">
                <label for="password2" class="font-semibold">비밀번호 확인</label>
                <input
                  type="password" id="password2" placeholder="PASSWORD" v-model="password2"
                  class="h-12 px-4 py-2.5 my-2 bg-blue-50 border border-2 border-slate-300 
                        focus:outline-none focus:border-blue-700 focus:ring-2 focus:ring-blue-200 text-black
                        disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none
                        rounded-lg text-gray-950 text-xl font-normal leading-tight"
                  :class="{'border-pink-500 text-pink-600 focus:border-pink-500 focus:ring-pink-200':!isValidPassword2}"
                >
                <p class="text-emerald-700" :class="{'text-pink-700':!isValidPassword2}">{{ checkPwMessage2 }}</p>
              </div>
              <button :disabled="!validate" 
                class="w-full h-12 my-1 bg-blue-900 hover:bg-blue-700 rounded-lg cursor-pointer
                text-center text-white text-xl font-semibold leading-tight
                disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none disabled:cursor-default"
              >
                시작하기
              </button>
            </form>
          </div>
          <p class="text-center cursor-default">
            아이디가 있으신가요? 
            <span class=" mx-2 text-blue-950 underline font-bold">
              <RouterLink :to="{name: 'signin'}">로그인 하기</RouterLink>
            </span>
          </p>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import { computed, ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const checkIdMessage = ref('')
const checkPwMessage1 = ref('')
const checkPwMessage2 = ref('')
const isValidUsername = ref(true)
const isValidPassword1 = ref(true)
const isValidPassword2 = ref(true)

const validate = computed(() => {
  const isvalid = isValidPassword1.value && isValidPassword2.value && isValidUsername.value
  const info = username.value && password1.value && password2.value
  return isvalid && info  ? true : false
})

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  if (validate) {
    store.signUp(payload)
  }
}

watch(password1, (inputValue) => {
  const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/.test(inputValue)
  if (inputValue === '') {
    checkPwMessage1.value = '비밀번호를 입력해주세요.'
    isValidPassword1.value = false
  } else {
    if ((password2.value !== '') && (isValidPassword2.value === true)) {
      checkPwMessage2.value = '비밀번호가 일치하지 않습니다.'
      isValidPassword2.value = false
    }
    if (inputValue.includes(' ')) {
      checkPwMessage1.value = '비밀번호는 공백을 포함할 수 없습니다.'
      isValidPassword1.value = false
    } else if (!regex) {
      checkPwMessage1.value = '비밀번호는 알파벳과 숫자를 포함하고 8자 이상이어야합니다. (사용가능한 특수문자: @$!%*#?&)'
      isValidPassword1.value = false
    } else {
      checkPwMessage1.value = '유효한 비밀번호입니다.'
      isValidPassword1.value = true
      if ((inputValue === password2.value) && (isValidPassword2.value === false)) {
        checkPwMessage2.value = '비밀번호가 일치합니다.'
        isValidPassword2.value = true
      }
    }
  }
})

watch(password2, (inputValue) => {
  const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/.test(password1.value)
  if (!regex) {
    checkPwMessage2.value = '유효한 비밀번호를 입력해주세요.'
    isValidPassword2.value = false
    isValidPassword1.value = false
    if (password1.value === '') {
      checkPwMessage1.value = '비밀번호를 입력해주세요.'
    }
  } else if (inputValue === '') {
    checkPwMessage2.value = '비밀번호를 확인해주세요'
    isValidPassword2.value = false
  } else if (inputValue === password1.value) {
    checkPwMessage2.value = '비밀번호가 일치합니다.'
    isValidPassword2.value = true
  } else {
    checkPwMessage2.value = '비밀번호가 일치하지 않습니다.'
    isValidPassword2.value = false
  }
})

const ExistsId = function () {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/username/',
    params: {
      username: username.value
    }
  })
    .then((res) => {
      // console.log(res.data.result)
      if (res.data.result) {
        checkIdMessage.value = '이미 존재하는 아이디입니다.'
        isValidUsername.value = false
      } else {
        checkIdMessage.value = '사용가능한 아이디입니다.'
        isValidUsername.value = true
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

watch (username, (inputValue) => {
  const regex  = /^[A-Za-z\d_]*$/.test(inputValue)
  if (inputValue === '') {
    checkIdMessage.value = '아이디를 입력해주세요.'
    isValidUsername.value = false
  } else if (inputValue.includes(' ')) {
    checkIdMessage.value = '아이디는 공백을 포함할 수 없습니다.'
    isValidUsername.value = false
  } else if (!regex) {
    checkIdMessage.value = '아이디는 알파벳과 숫자만 사용가능합니다.'
    isValidUsername.value = false
  } else if (username.value.length < 4) {
    checkIdMessage.value = '4자 이상 입력해주세요.'
    isValidUsername.value = false
  } else {
    ExistsId()
  }
})

const goMain = function () {
  router.push({ name: 'main' })
}

</script>

<style scoped>

</style>