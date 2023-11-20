<template>
    <div>
      <form @submit.prevent="login">
        <label for="username">아이디</label>
        <input type="text" id="username" v-model="username">
        <label for="password">비밀번호</label>
        <input type="password" id="password" v-model="password">
        <button>로그인</button>
      </form>
    </div>
</template>

<script setup>
import { useUserStore } from '../stores/user'
import { ref } from 'vue'

const store = useUserStore()

const username = ref(null)
const password = ref(null)

const login = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.login(payload)
}

</script>

<style scoped>

</style>