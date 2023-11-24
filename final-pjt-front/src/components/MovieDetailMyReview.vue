<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">내가 작성한 리뷰</h2>
    <ReviewCard v-if="review != null" :review="review" />
    <div v-else class="flex flex-col items-center justify-center h-64">
        <p class="mb-4 text-sm text-gray-500">아직 리뷰를 남기지 않으셨어요.</p>
        <p class="mb-4 text-sm text-gray-500">작품에 대한 감상을 기록해보세요!</p>
        <button @click="openModal" class="px-4 py-2 bg-blue-900 font-medium text-white rounded">리뷰 작성하기</button>
    </div>
  </div>
</template>

<script setup>
import ReviewCard from '@/components/ReviewCard.vue'
import { useUserStore } from '@/stores/user'
import { useRouter } from 'vue-router';
const store = useUserStore()
const emit = defineEmits(['openModal'])
const router = useRouter()

const props = defineProps({
  review: {
    type: Object,
  }
})

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}

const openModal = function() {  
  if (store.token) {
    emit('openModal')
  } else {
    router.push({
      name : 'signin'
    })
  }
}

</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
