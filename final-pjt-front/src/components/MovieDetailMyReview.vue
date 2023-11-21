<template>
  <div class="border-b border-gray-400 pb-8 mb-8">
    <h2 class="text-lg font-bold mb-4">내가 작성한 리뷰</h2>
    <div class="mb-6 p-4 bg-white shadow rounded">
      <template v-if="myReivew">
        <div class="flex justify-between items-center mb-2">
          <p class="font-bold">{{ myReivew.user.profile.nickname }}</p>
          <p class="text-sm text-gray-500">{{ formatDate(myReivew.created_at) }}</p>
        </div>
        <StarRating v-model="myReivew.rating" :disableClick="true" :starSize="16" class="mb-2"/>
        <p class="text-sm font-light line-clamp-3">{{ myReivew.content }}</p>
        <button v-if="myReivew.content.length > 120" class="text-gray-500 text-right">더보기</button>
        <div class="flex justify-end mt-2">
          <button class="text-gray-500">👍 좋아요 {{ myReivew.liked_by.length }}</button>
        </div>
      </template>
      <template v-else>
        <div class="flex flex-col items-center justify-center h-64">
          <p class="mb-4 text-sm text-gray-500">아직 리뷰를 남기지 않으셨어요.</p>
          <p class="mb-4 text-sm text-gray-500">작품에 대한 감상을 기록해보세요!</p>
          <button class="px-4 py-2 bg-blue-500 font-medium text-white rounded">리뷰 작성하기</button>
        </div>
      </template>
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

const myReivew = computed(() => {
  if (props.reviews && store.isLogin) {
    // todo : 자기 게시글만 로드
    return props.reviews
  } else {
    return undefined
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
/* 아프지마 ㅠㅠ */
</style>
