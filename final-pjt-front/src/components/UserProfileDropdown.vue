<template>
  <div 
    class="w-48 h-full px-4 bg-white border rounded-lg shadow-lg text-xl 
      outline outline-1 outline-slate-400 outline-offset-1"
  >
    <div class="hover:bg-slate-200 py-4">
      <RouterLink :to="{name: 'profile', params: {username: store.userInfo.username}}">
        <p>내 프로필</p>
      </RouterLink>
    </div>
    <div 
      @click="logout" class="hover:bg-slate-200 py-4"
    >
      로그아웃
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const logout = function () {
  store.logout()
}

</script>

<style scoped>

</style>