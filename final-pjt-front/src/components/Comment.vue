<template>
  <div class="flex justify-between items-center border-b relative">
    <div>
      <div @click="isDropdownOpen = !isDropdownOpen" class="absolute top-6 right-0 cursor-pointer">
        <i class="fas fa-ellipsis-v"></i>
        <CommentDropdown
          v-if="isDropdownOpen"
          @close-dropdown="isDropdownOpen = false"
          :commentId="comment.id"
        />
      </div>
      <div class="absolute top-14 right-6 cursor-pointer rounded-md border border-gray-200 px-3 py-1"
            @click="likeComment">
            <i :class="{'fas fa-heart text-red-400': isLike, 'far fa-heart text-red-400': !isLike}"></i>
        <span class="pl-2 ">{{ likeCnt }}</span>
      </div>

      <div class="flex items-center mt-4 mb-5">

        <div class="flex items-center ml-4">
          <img
            v-if="comment.user?.profile.profile_img"
            :src="comment.user?.profile.profile_img"
            class="w-8 h-8 rounded-full mr-4"
          />
          <img
            v-else
            src="@/assets/images/anonymous_square.png"
            class="w-8 h-8 rounded-full mr-4"
          />
          <div>
            <p class="font-bold">{{ comment.user?.profile.nickname }}</p>
            <p class="text-sm text-gray-500">{{ formatDate(comment.created_at) }}</p>
          </div>
        </div>
      </div>

      <p class="text-sm font-light mb-6">
        {{ comment.content }}
      </p>
    </div>
  </div>
</template>



<script setup>
import axios from 'axios'
import { ref, watchEffect } from 'vue'
import { useUserStore } from '@/stores/user'
import CommentDropdown from '@/components/CommentDropdown.vue'

const props = defineProps({
  comment : {
    type : Object,
  }
})

const comment = props.comment
const isLike = ref(false)
const likeCnt = ref(0)
const store = useUserStore()
const isDropdownOpen = ref(false)

watchEffect(() => {
  isLike.value = props.comment.liked_by.some(user => user.id === store.userInfo?.id)
  likeCnt.value = props.comment?.liked_cnt
})

const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}

const likeComment = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/comment/${comment.id}/like/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    isLike.value = res.data.is_like
    likeCnt.value = res.data.like_cnt
  })
  .catch((err) => console.log(err))
}


</script>

<style scoped>

</style>