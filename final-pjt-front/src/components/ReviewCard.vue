<template>
<div class="mb-6 p-4 bg-white shadow rounded relative">
  <div v-if="store.userInfo?.id === review.user?.id" class="absolute top-16 right-4 cursor-pointer">
        <i @click="isDropdownOpen = !isDropdownOpen" class="fas fa-ellipsis-v"></i>
        <ReviewDropdown
          v-if="isDropdownOpen"
          @close-dropdown="isDropdownOpen = false"
          :review="review"
        />
  </div>

  <div class="flex justify-between items-center mb-2">
    <div class="flex items-center">
      <img v-if="review.user?.profile.profile_img"
        :src="'http://127.0.0.1:8000'+review.user?.profile.profile_img"
        class="w-8 h-8 rounded-full mr-4"
      />
      <img v-else
        src="@/assets/images/anonymous_square.png"
        class="w-8 h-8 rounded-full mr-4"
      >
      <p class="font-bold">{{ review.user.profile.nickname }}</p>
    </div>
    <p class="text-sm text-gray-500">{{ formatDate(review.created_at) }}</p>
  </div>
  <StarRating v-model="review.rating" :disableClick="true"
          :starSize="16" 
          :starColor="'#4263EB'"
          :numberOfStars="5"
          class="mb-2"/>
  <p class="text-sm font-light">{{ review.content }}</p>
  <!-- <button v-if="review.content.length > 120" class="text-gray-500 text-right">더보기</button> -->
  <div class="flex justify-end mt-2">
    <button @click="likeReview(review)" class="text-gray-500">
      <i :class="{'fas fa-heart': isLike, 'far fa-heart': !isLike}"></i>
      좋아요 {{ likeCnt }}
    </button>

  </div>
</div>
</template>

<script setup>
import StarRating from '@/components/StarRating.vue'
import { watch, ref } from 'vue'
import { useUserStore } from '@/stores/user'
import axios from 'axios'
import ReviewDropdown from '@/components/ReviewDropdown.vue'


const props = defineProps({
  review : {
    type: Object,
  }
})
const store = useUserStore()
const likeCnt = ref(props.review?.liked_by.length)
const isLike = ref(props.review?.liked_by.includes(store.userInfo.id))
const isDropdownOpen = ref(false)

watch(
  () => props.review,
  (newReview) => {
    console.log(review)
    likeCnt.value = newReview.liked_by.length;
    isLike.value = newReview.liked_by.includes(store.userInfo.id);
  }
)


const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}


const likeReview = function(review) {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/review/${review.id}/like/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res)
    likeCnt.value = res.data.like_cnt
    isLike.value = res.data.is_like
  })
  .catch((err) => console.log(err))
}

</script>

<style scoped>
</style>
