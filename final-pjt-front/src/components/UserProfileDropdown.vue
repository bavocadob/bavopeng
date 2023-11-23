<template>
  <div 
    class="w-48 h-full bg-white border rounded-lg shadow-lg text-xl 
      outline outline-1 outline-slate-400 outline-offset-1"
  >
    <a class="hover:bg-slate-200 p-4 block" :href="`http://localhost:5173/profile/${store.userInfo.username}`">
      내 프로필
    </a>
    <div 
      @click="logout" class="hover:bg-slate-200 hover:cursor-pointer p-4"
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