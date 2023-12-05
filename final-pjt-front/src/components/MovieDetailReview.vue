<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">모든 리뷰</h2>
    <VueMultiselect
      v-if="reviews?.length > 0"
      v-model="selectedOption"
      :options="sortOptions" 
      label="name"
      track-by="value"
      @select="getReview"
      :searchable="false"
      :showLabels="false"
      :optionHeight="10"
      class="mb-2"
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
import { ref } from 'vue'

const emit = defineEmits(['sortReview'])
const props = defineProps({
  reviews: {
    type: Array,
  }
})

const selectedOption = ref({ label: '좋아요 순', value: 0 })
const sortOptions = ref([
  { name: '좋아요 순', value: 0 },
  { name: '최근 작성 순', value: 1 },
  { name: '평점 높은 순', value: 2 },
  { name: '평점 낮은 순', value: 3 }
])



const getReview = function() {
  // console.log(selectedOption.value)
  if (!selectedOption.value) return
  emit('sortReview', selectedOption.value.value);
}

</script>

<style>
.multiselect__option {
  font-size: 0.82rem;
}

.multiselect__option--highlight {
  background: #BFDBFF !important;
}

</style>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
