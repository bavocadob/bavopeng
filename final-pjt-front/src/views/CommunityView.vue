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
        <button @click="createArticle" class="bg-yellow-500 hover:bg-yellow-600 text-white font-medium py-2 px-4 rounded">
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
