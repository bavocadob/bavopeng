<template>
  <section>
    <div class="header flex justify-between items-center mb-10">
      <div>
        <h1 class="text-4xl font-bold text-white">Community</h1>
        <p class="text-lg text-white mt-2">
          커뮤니티 공간에서 자유롭게 이야기를 나눠보세요
        </p>
      </div>
  
      <div>
        <button @click="createArticle" class="bg-yellow-500 hover:bg-yellow-600 text-white font-medium py-2 px-4 rounded">
          글쓰기
        </button>
      </div>
    </div>
    <Board />
  </section>
  </template>
  

<script setup>
import Board from '@/components/Board.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const router = useRouter()

const createArticle = function() {
  console.log(router)
  if (store.token) {
    router.push({
      name : 'articleCreate'
    })
  } else {
    router.push({
      name : 'loginView'
    })
  }
}


</script>

<style scoped>
</style>
