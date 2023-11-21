<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">모든 리뷰</h2>
    <div v-for="review in filteredReview" :key="review.id" class="mb-6 p-4 bg-white shadow rounded">
      <div class="flex justify-between items-center mb-2">
        <p class="font-bold">{{ review.user.profile.nickname }}</p>
        <p class="text-sm text-gray-500">{{ formatDate(review.created_at) }}</p>
      </div>
      <StarRating v-model="review.rating" :disableClick="true" :starSize="16" class="mb-2"/>
      <p class="text-sm font-light line-clamp-3">{{ review.content }}</p>
      <button v-if="review.content.length > 120" class="text-gray-500 text-right">더보기</button>
      <div class="flex justify-end mt-2">
        <button class="text-gray-500">👍 좋아요 {{ review.liked_by.length }}</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import StarRating from './StarRating.vue';
import { computed } from 'vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()

const props = defineProps({
  reviews: {
    type: Array,
  }
})

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}

const filteredReview = computed(() => {
  if (props.reviews && store.isLogin) {
    // todo : 자기 게시글 제외하고 로드
    return props.reviews
  } else {
    return props.reviews
  }

})

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
