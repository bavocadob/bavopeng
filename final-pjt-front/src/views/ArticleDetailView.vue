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
              <router-link
                v-if="article.user?.username"
                :to="{
                  name: 'profile',
                  params: {
                    username: article.user?.username,
                  },
                }"
              >
            <div class="flex items-center">
              <img v-if="article.user?.profile.profile_img"
                :src="article.user?.profile.profile_img"
                class="w-8 h-8 rounded-full mr-4"
              />
              <img v-else
                src="@/assets/images/anonymous_square.png"
                class="w-8 h-8 rounded-full mr-4"
              >
              <div>
                <p class="font-bold">{{ article.user?.profile.nickname }}</p>
                <p class="text-sm text-gray-500">{{ formatDate(article.created_at) }}</p>
              </div>
            </div>
            </router-link>
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

          <!-- 태그된 영화 -->
          <div v-if="article.ref_movie != null" class="mb-5 mt-3">
            <router-link
              :to="{
                name: 'movieDetail',
                params: {
                  movieId: article.ref_movie.id,
                },
              }"
            >
              <div
                class="flex justify-between items-center p-3 mb-2 bg-gray-100 rounded-lg"
              >
                <div class="flex items-center">
                  <img
                    :src="`https://image.tmdb.org/t/p/original${article.ref_movie.poster_path}`"
                    alt="poster"
                    class="w-12 mr-3"
                  >
                  <div>
                    <div class="text-base">{{ article.ref_movie.title }}</div>
                    <div class="text-sm">{{ article.ref_movie.release_date?.slice(0, 4) }}</div>
                    <div class="flex">
                      <StarRating
                        v-model="article.ref_movie.rating_avg"
                        :disableClick="true"
                        :starSize="14"
                        :starColor="'#4263EB'"
                        :numberOfStars="5"
                      />
                      <span class="text-sm ml-2">{{ Math.round(article.ref_movie.rating_avg * 10) / 10 }}</span>
                    </div>
                  </div>
                </div>
              </div>
           </router-link>
          </div> 
          <!-- 태그된 영화 -->

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
          <CommentList />

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
import CommentList from '@/components/CommentList.vue'
import StarRating from '@/components/StarRating.vue'

const store = useUserStore()
const route = useRoute()


const article = ref({})
const likeCnt = ref(0)
const dislikeCnt = ref(0)
const commentCnt = ref(0)
const isLike = ref(false)
const isDislike = ref(false)
const isDropdownOpen = ref(false)


onMounted(() => {
  const headers = {};
  if (store.token) {
    headers.Authorization = `token ${store.token}`;
  }
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}`,
    headers : headers
  })
  .then((res) => {
    article.value = res.data
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
    commentCnt.value = res.data.comment_cnt
    isLike.value = res.data.is_like
    isDislike.value = res.data.is_dislike
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
    // console.log(res)
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
    // console.log(res)
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