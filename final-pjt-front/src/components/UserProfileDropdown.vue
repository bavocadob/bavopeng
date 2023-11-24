<template>
  <div 
    class="w-20 h-full bg-indigo-100 border rounded-lg shadow-lg text-sm font-semibold 
      outline outline-2 outline-indigo-400 outline-offset-0 overflow-hidden"
  >
    <a class="hover:bg-indigo-200 p-2 block" :href="`http://localhost:5173/profile/${store.userInfo.username}`">
      내 프로필
    </a>
    <div 
      @click="logout" class="hover:bg-indigo-200 hover:cursor-pointer p-2"
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