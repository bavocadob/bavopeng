<template>
  <div class="absolute right-2 w-16 bg-white shadow rounded-md border border-gray-200">
    <div class="text-sm">
      <button @click="isModalOpen=true" class="block w-full px-2 py-2 border-b border-gray-200">수정</button>
      <button @click="deleteReview" class="block w-full px-2 py-2">삭제</button>
    </div>
    <MovieReviewEditModal
        v-if="isModalOpen" :review="review"
        @close-modal="isModalOpen=false"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import MovieReviewEditModal from '@/components/MovieReviewEditModal.vue'


const store = useUserStore()
const isModalOpen = ref(false)

const props = defineProps({
  review : {
    type : Object,
  }
})


const deleteReview = function() {
  axios({
    method : 'DELETE',
    url : `${store.API_URL}/api/v1/review/${props.review.id}/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    location.reload()
  })
  .catch((err) => {
    console.log(err)
  })
}
</script>

<style scoped>

</style>