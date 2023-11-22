<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">모든 리뷰</h2>
    <VueMultiselect 
      v-model="selectedOption" 
      :options="sortOptions" 
      label="name" 
      track-by="name" 
      @input="sortReviews"
    />

    <ReviewCard v-if="reviews?.length" v-for="review in reviews" :key="review.id" :review="review" />

    <div v-else class="flex flex-col items-center justify-center" >
      <i class="fas fa-exclamation-circle text-3xl mb-4"></i>
      <p class="text-lg font-bold mb-2">작성된 리뷰가 없습니다.</p>
      <p class="text-base text-gray-500">이 작품의 첫 리뷰를 작성해보세요!</p>
    </div>
  </div>
  
</template>

<script setup>
import ReviewCard from '@/components/ReviewCard.vue'
import VueMultiselect from 'vue-multiselect'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import { computed, ref } from 'vue'

const store = useUserStore()
const route = useRoute()
const movieId = route.params.movieId

const props = defineProps({
  reviews: {
    type: Array,
  }
})

const selectedOption = ref('')
const sortOptions = [
  { name: '좋아요 순', method: 'sortLikes' },
  { name: '최근 작성 순', method: 'sortRecent' },
  { name: '평점 높은 순', method: 'sortHighRating' },
  { name: '평점 낮은 순', method: 'sortLowRating' }
]

const sortReviews = function() {
  console.log('정렬하자')
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
