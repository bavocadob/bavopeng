<template>
    <div>
      <h1>SignUp</h1>
      <form @submit.prevent="signUp">
        <div>
          <label for="username">아이디</label>
          <input 
            v-model.trim="username" @keyup="validateUsername"
            type="text" id="username" class="text-slate-900" 
          >
          <p>{{ checkIdMessage }}</p>
        </div>
        <div>
          <label for="password1">비밀번호</label>
          <input 
            v-model.trim="password1" @keyup="validatePassword"
            type="password" id="password1" class="text-slate-900"
          >
          <p>{{ checkPwMessage }}</p>
        </div>
        <div>
          <label for="password2">비밀번호 확인</label>
          <input 
            v-model.trim="password2" @keyup="SamePassword"
            type="password" id="password2" class="text-slate-900"
          >
          <p>{{ checkPwMessage2 }}</p>
        </div>
        <button>회원가입</button>
      </form>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import axios from 'axios';
import { ref, watch } from 'vue'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const checkIdMessage = ref('')
const checkPwMessage = ref('')
const checkPwMessage2 = ref('')
const isValidUsername = ref(false)
const isValidPassword = ref(false)
const isValidPassword2 = ref(false)

const signUp = function () {

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  if (isValidPassword.value && isValidPassword2.value && isValidUsername.value) {
    store.signUp(payload)
  }
}

const validatePassword = function () {
    // 영어, 숫자를 포함하고 8자 이상
    const regex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$/.test(password1.value)
    if (password1.value.length > 0 && !regex) {
      checkPwMessage.value = '비밀번호는 알파벳과 숫자를 포함하고 8자 이상이어야합니다. (사용가능한 특수문자: @$!%*#?&)'
      isValidPassword.value = false
    } else {
      if (password1.value === '') {
        checkPwMessage.value = ''
        isValidPassword.value = false
      } else {
        checkPwMessage.value = '유효한 비밀번호입니다.'
        isValidPassword.value = true
      }
    }
}

const SamePassword = function () {
  if (password2.value.length > 0) {
    if (password1.value !== password2.value) {
      checkPwMessage2.value = '비밀번호가 일치하지 않습니다.'
      isValidPassword2.value = false
    } else {
      checkPwMessage2.value = '비밀번호가 일치합니다.'
      isValidPassword2.value = true
    }
  } if (password1.value == '' || password2.value == '') {
    checkPwMessage2.value = ''
    isValidPassword2.value = false
  }
} 

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

const validateUsername = function () {
  const regex  = /^[A-Za-z\d]*$/.test(username.value)
  if (!username.value) {
    checkIdMessage.value = ''
  } else if (!regex) {
    checkIdMessage.value = '알파벳과 숫자를 제외한 문자는 사용할 수 없습니다.'
  } else if (username.value.length < 4) {
    checkIdMessage.value = '4자 이상 입력해주세요.'
  } else {
    ExistsId()
  }
}

watch(password1 => {
  SamePassword()
})
</script>

<style scoped>

</style>