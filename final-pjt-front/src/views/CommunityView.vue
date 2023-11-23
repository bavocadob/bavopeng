<template>
  <section>
    <div class="header flex justify-between items-center mb-10">
      <div>
        <h1 class="text-4xl font-bold text-white">Community</h1>
        <p class="text-lg text-white mt-2">
          지금부터 서로 죽여라
        </p>
      </div>
  
      <div>
        <button @click="createArticle" class="bg-blue-900 text-white font-medium py-2 px-4 rounded shadow-lg border border-blue-800 transition-colors duration-200">
          글쓰기
        </button>
      </div>
    </div>
    <CommunityBody />
  </section>
  </template>
  

<script setup>
import CommunityBody from '@/components/CommunityBody.vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const router = useRouter()

const createArticle = function() {
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
