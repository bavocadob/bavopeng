<template>
    <div class="mx-auto">
      <h1 class="text-4xl font-semibold text-white">프로필</h1>
      <div class="my-8 p-8 h-full bg-gray-200 grid grid-cols-3 gap-4 rounded-lg">
        <div class="my-14 bg-white shadow-md col-span-2">
          <UserProfile :profileInfo="profileInfo" />
        </div>
        <div class="my-14 px-2 bg-white shadow-md flex flex-col justify-center">
          <div class="flex">
            <span class="my-4 mx-2 font-semibold">최근 리뷰</span>
            <!-- <img src="@/assets/images/chevron-right.svg" alt="화살표"> -->
          </div>
          <ReviewCard @click="goMovie(review.movie)"
            v-for="review in reviews" :key="review.id" :review="review"
            class="border"
          />
        </div>
      </div>
      <div class="my-14 h-full bg-gray-200 flex flex-col items-center rounded-lg">
        <div class="my-8">
          <h2 class="text-2xl my-4">좋아하는 영화</h2>
          <div class="bg-blue-950 rounded-lg">
            <div class="w-[1100px] my-18 bg-black bg-opacity-50 p-8 rounded-lg shadow-md">
              <MovieSwiper :movies="likeMovies" />
            </div>
          </div>
        </div>
        <div class="mb-12">
          <h2 class="text-2xl m-4">보고싶은 영화</h2>
          <div class="bg-blue-950 rounded-lg">
            <div class="w-[1100px] my-18 bg-black bg-opacity-50 p-8 rounded-lg shadow-md">
              <MovieSwiper :movies="wishMovies" />
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
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

axios({
  method: 'get',
  url: `http://127.0.0.1:8000/api/v1/profile/${username}/`,
})
  .then((res) => {
    console.log(res.data)
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
      followers: data.user.followers
    }
    likeMovies.value = data.user.liked_movies
    wishMovies.value = data.user.wished_movies
    reviews.value = data.user.review_set.sort((a, b) => b.id - a.id).slice(0, 2)
  })
  .catch((err) => {
    console.log(err)
  })

  const goMovie = function (movieId) {
    router.push({name:'movieDetail', params:{movieId}})
  }
  
</script>

<style scoped>

</style>