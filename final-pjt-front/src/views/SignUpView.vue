<template>
    <div>
      <h1>SignUp</h1>
      <form @submit.prevent="signUp">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model.trim="username">
        <label for="password1">비밀번호</label>
        <input type="password" id="password1" v-model.trim="password1">
        <label for="password2">비밀번호 확인</label>
        <input type="password" id="password2" v-model.trim="password2">
        <p v-if="password1 !== password2">비밀번호가 일치하지 않습니다.</p>
        <button>회원가입</button>
      </form>
    </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const store = useUserStore()
const router = useRouter()

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value
  }
  store.signUp(payload)
}

</script>

<style scoped>

</style>