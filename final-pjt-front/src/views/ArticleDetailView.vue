<template>
  <section class="container mx-auto px-4">
    <div class="flex">
      <div class="w-full space-y-4">
        <div class="bg-white shadow rounded-lg p-6">
          <div class="flex justify-between items-start mb-4">
            <h2 class="text-xl font-bold">{{ article.title }}</h2>
            <div v-if="article.user?.id === store.userInfo?.id" class="relative">
              <button @click="isDropdownOpen = !isDropdownOpen" class="focus:outline-none">
                <i class="fas fa-ellipsis-v"></i>
              </button>
              <transition name="fade">
                <CommunityDropdown
                  v-if="isDropdownOpen"
                  @close-dropdown="isDropdownOpen = false"
                  class="absolute right-0 mt-2"
                />
              </transition>
            </div>
          </div>
          
          <div class="border border-t-0 border-r-0 border-l-0 my-4"></div>

          <div class="flex justify-between items-center mb-6">
            <div class="flex items-center">
              <img v-if="store.userInfo.profile.profile_img"
                :src="store.userInfo.profile.profile_img"
                class="w-8 h-8 rounded-full mr-4"
              />
              <img v-else
                src="@/assets/images/anonymous.png"
                class="w-8 h-8 rounded-full mr-4"
              >
              <div>
                <p class="font-bold">{{ store.userInfo.profile.nickname }}</p>
                <p class="text-sm text-gray-500">{{ formatDate(article.created_at) }}</p>
              </div>
            </div>
            <div class="flex">
              <div class="flex items-center mr-6">
                <i class="fas fa-heart text-red-500 mr-2"></i>
                <p>{{ likeCnt }}</p>
              </div>
              <div class="flex items-center">
                <i class="fas fa-comment text-blue-500 mr-2"></i>
                <p>{{ commentCnt }}</p>
              </div>
            </div>
          </div>
          <div v-html="article.content" class="mb-6"></div>
          <div class="flex justify-center">
            <button
              class="bg-white border border-gray-200 flex items-center px-4 py-2 rounded mr-2"
              @click="likeArticle"
            >
              <i :class="isLike ? 'fas fa-thumbs-up text-red-500' : 'far fa-thumbs-up text-red-500'" class="mr-2"></i>
              <span class="text-red-600">{{ likeCnt }}</span>
            </button>
            <button
              class="bg-white border border-gray-200 flex items-center px-4 py-2 rounded"
              @click="dislikeArticle"
            >
              <i :class="isDislike ? 'fas fa-thumbs-down text-blue-500' : 'far fa-thumbs-down text-blue-500'" class="mr-2"></i>
              <span class="text-blue-600">{{ dislikeCnt }}</span>
            </button>
          </div>


        </div>
        <!-- 코멘트 -->
        <div class="bg-white shadow rounded-lg p-6">
          <CommentWrite />

          <!-- <Comment
            v-for="comment in comments"
            :key="comment.id"
            :commentId="comment.id"
          /> -->
        </div>
        <!--  -->
      </div>
    </div>
  </section>
</template>




<script setup>
import axios from 'axios'
import { ref, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import CommunityDropdown from '@/components/CommunityDropdown.vue'
import CommentWrite from '@/components/CommentWrite.vue'

const store = useUserStore()
const route = useRoute()


const article = ref({})
const likeCnt = ref(0)
const dislikeCnt = ref(0)
const commentCnt = ref(0)
const comments = ref([])
const isLike = ref(true)
const isDislike = ref(false)
const isDropdownOpen = ref(false)


onMounted(() => {
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}`
  })
  .then((res) => {
    console.log(res)
    article.value = res.data
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
    commentCnt.value = res.data.comment_cnt
    // TODO: 밑에 두개 완성하기
    // isLike.value
    // isDislike.value
  })
  .catch((err) => console.log(err))
})


const likeArticle = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/like/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res)
    isLike.value = res.data.is_like
    isDislike.value = res.data.is_dislike
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
  })
  .catch((err) => console.log(err))
}


const dislikeArticle = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/dislike/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res)
    isLike.value = res.data.is_like
    isDislike.value = res.data.is_dislike
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
  })
  .catch((err) => console.log(err))
}


const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}

</script>

<style scoped>

</style>