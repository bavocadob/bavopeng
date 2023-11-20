<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink :to="{ name: 'main' }">main</RouterLink> | 
        <RouterLink :to="{ name: 'signUpView' }">회원가입</RouterLink> | 
        <RouterLink :to="{ name: 'loginView' }">로그인</RouterLink> | 
        <button @click="logout">로그아웃</button>
      </nav>
    </div>
  </header>
  <RouterView />
  <!-- <MovieView /> -->
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useUserStore } from './stores/user'
import MovieView from './views/MovieView.vue'

const store = useUserStore()
const logout = function () {
  store.logout()
}

</script>


<style scoped>

</style>
