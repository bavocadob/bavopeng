<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">모든 리뷰</h2>
    <ReviewCard v-if="filteredReview?.length" v-for="review in filteredReview" :key="review.id" :review="review" />

    <div v-else class="flex flex-col items-center justify-center" >
      <i class="fas fa-exclamation-circle text-3xl mb-4"></i>
      <p class="text-lg font-bold mb-2">작성된 리뷰가 없습니다.</p>
      <p class="text-base text-gray-500">이 작품의 첫 리뷰를 작성해보세요!</p>
    </div>
  </div>
</template>

<script setup>
import ReviewCard from '@/components/ReviewCard.vue'
import { useUserStore } from '@/stores/user'
import { computed } from 'vue'

const store = useUserStore()

const props = defineProps({
  reviews: {
    type: Array,
  }
})

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
