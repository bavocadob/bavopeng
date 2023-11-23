<template>
    <div class="mx-auto">
      <h1 class="text-4xl font-semibold text-white">프로필</h1>
      <div class="my-8 p-8 h-full bg-gray-200 grid grid-cols-12 gap-4 rounded-lg">
        <div class="my-14 bg-white shadow-md col-span-8">
          <UserProfile :profileInfo="profileInfo" />
        </div>
        <div class="my-14 px-2 bg-white shadow-md col-span-4 flex flex-col justify-center">
          <span class="my-4 mx-2 font-semibold">최근 리뷰</span>
          <div class="p-2">
            <div v-if="reviewsExists"  class="scroll-container h-[360px] snap-x">
              <ReviewCard @click="goMovie(review.movie)"
                v-for="review in reviews" :key="review.id" :review="review"
                class="border snap-center"
              />
            </div>
            <div class="h-[360px]">
              <p class="mt-20 text-center text-sm text-gray-500">아직 작성한 리뷰가 없어요.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="my-14 pt-4 h-full bg-gray-200 flex flex-col items-center rounded-lg">
        <div class="my-8 w-[1100px] border-b border-gray-400 pb-6 px-4">
          <h2 class="text-2xl my-4 text-center font-semibold">좋아하는 영화</h2>
          <div v-if="likedMovieExists" class="bg-blue-950 rounded-lg">
            <div class="my-18 bg-black bg-opacity-50 p-8 rounded-lg shadow-md">
              <MovieSwiper :movies="likeMovies" />
            </div>
          </div>
          <div v-else class="flex flex-col items-center justify-center h-64">
            <p class="mb-4 text-sm text-gray-500">아직 좋아요한 영화가 없어요.</p>
            <p class="mb-4 text-sm text-gray-500">작품에 대한 감상을 기록해보세요!</p>
            <button @click="goMain" class="px-4 py-2 bg-blue-900 font-medium text-white rounded">영화 찾아보기</button>
          </div>
        </div>
        <div class="mb-8 w-[1100px] p-4">
          <h2 class="text-2xl my-4 text-center font-semibold">보고싶은 영화</h2>
          <div v-if="wishedMovieExists" class="bg-blue-950 rounded-lg">
            <div class="my-18 bg-black bg-opacity-50 p-8 rounded-lg shadow-md">
              <MovieSwiper :movies="wishMovies" />
            </div>
          </div>
          <div v-else class="flex flex-col items-center justify-center h-64">
            <p class="mb-4 text-sm text-gray-500">아직 보고싶은 영화를 기록하지 않으셨어요.</p>
            <p class="mb-4 text-sm text-gray-500">작품에 대한 감상을 기록해보세요!</p>
            <button @click="goMain" class="px-4 py-2 bg-blue-900 font-medium text-white rounded">영화 찾아보기</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '../stores/user'
import UserProfile from '@/components/UserProfile.vue'
import ReviewCard from '@/components/ReviewCard.vue'
import MovieSwiper from '@/components/MovieSwiper.vue'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useUserStore()

const username = route.params.username
const profileInfo = ref({})
const likeMovies = ref([])
const wishMovies = ref([])
const reviews = ref([])

const reviewsExists = computed(() => {
  return reviews.value.length > 0 ? true : false
})

const likedMovieExists = computed(() => {
    return likeMovies.value.length > 0 ? true : false
  })

const wishedMovieExists = computed(() => {
    return wishMovies.value.length > 0 ? true : false
  })
  

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/profile/${username}/`,
  headers: {
    Authorization: `Token ${store.token}`
  }
})
  .then((res) => {
    // console.log(res.data)
    const data = res.data
    profileInfo.value = {
      username,
      id: data.user.id,
      nickname: data.nickname,
      profile_img: data.profile_img,
      introduce: data.introduce,
      followingsCnt: data.user.followings_cnt,
      followersCnt: data.user.followers_cnt,
      genresLike: data.user.genres_like,
      isFollowing: data.user.is_following,
      followers: data.user.followers
    }
    likeMovies.value = data.user.liked_movies
    wishMovies.value = data.user.wished_movies
    reviews.value = data.user.review_set.sort((a, b) => b.id - a.id)
  })
  .catch((err) => {
    console.log(err)
  })

const goMovie = function (movieId) {
  router.push({name:'movieDetail', params:{movieId}})
}

const goMain = function () {
  router.push({name: 'main'})
}


</script>

<style scoped>
.scroll-container {
  overflow-y: scroll; /* 세로 스크롤 활성화 */
  scrollbar-width: thin; /* 스크롤바 너비 */
  scrollbar-color: #4F46E5 #E5E7EB; /* 스크롤바 색상 */
}

/* 스크롤바 트랙 스타일링 */
.scroll-container::-webkit-scrollbar {
  width: 6px; /* 스크롤바 너비 */
}

/* 스크롤바 색상 및 모양 */
.scroll-container::-webkit-scrollbar-thumb {
  background-color: #3f4ed8; /* 스크롤바 색상 */
  border-radius: 3px; /* 스크롤바 모양 */
}

/* 스크롤바 트랙 배경색 */
.scroll-container::-webkit-scrollbar-track {
  background-color: #E5E7EB;
}

</style>