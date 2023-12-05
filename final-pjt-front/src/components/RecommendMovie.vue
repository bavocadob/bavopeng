<template>
  <div v-if="!store.isLogin">
    <div class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900 flex flex-col items-center justify-center text-center">
      <i class="fas fa-film text-gray-400 text-6xl mb-4"></i>
      <h2 class="text-lg text-blue-200 mb-4">로그인 후 영화를 추천받아 보세요!</h2>
      <router-link
          :to="{
            name: 'signin',
          }" 
          class="bg-blue-950 text-white rounded px-4 py-2 hover:bg-blue-800">로그인 하러 가기
      </router-link>
    </div>
  </div>
  <div v-else class="grid rounded-lg lg:grid-cols-3 gap-4">
    <!-- 장르기반 -->
    <div v-if="genreRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900">
      <div class="flex items-start justify-between">
        <img v-if="genreRecommend.recommend.poster_path" @click="goDetail(genreRecommend.recommend.id)" 
          :src="`https://image.tmdb.org/t/p/original${genreRecommend.recommend.poster_path}`" 
          class="w-2/5 rounded cursor-pointer" />
        <img v-else @click="goDetail(genreRecommend.recommend.id)" src="@/assets/images/noPoster.png" alt="noposter"
          class="w-2/5 rounded cursor-pointer" >
        <div class="ml-4 flex flex-col justify-between h-full">
          <div>
            <div class="flex items-center justify-between gap-1">
              <h2 class="text-lg text-blue-200">{{ genreRecommend.recommend.title }}</h2>
              <div class="flex items-center">
                <i class="fas fa-star text-sm text-yellow-400"></i>
                <span class="ml-1 text-sm">{{ Math.round(genreRecommend.recommend.rating_avg * 10) / 10 }}</span>
              </div>
            </div>
            <p class="text-blue-300 text-sm">{{ genreRecommend.recommend.release_date }}</p>
          </div>
          <p class="mt-4 text-sm text-blue-100"><span class="font-bold text-base">{{ genreRecommend.target }}</span> 장르를 좋아하신다면 이 영화도 추천드려요!</p>
        </div>
      </div>
    </div>
    <div v-else="!genreRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900 flex flex-col items-center justify-center text-center">
      <i class="fas fa-film text-gray-400 text-6xl mb-4"></i>
      <h2 class="text-lg text-blue-200 mb-4">아직 선호하는 장르가 없으시군요?</h2>
      <router-link
          :to="{
            name: 'prefer',
          }" 
          class="bg-blue-950 text-white rounded px-4 py-2 hover:bg-blue-800">영화 찾으러 가기
      </router-link>
    </div>
    <!-- 장르기반 -->
    <!-- 좋아요기반 -->
    <div v-if="likeRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900">
      <div class="flex items-start justify-between">
        <img v-if="likeRecommend.recommend.poster_path" @click="goDetail(likeRecommend.recommend.id)" 
          :src="`https://image.tmdb.org/t/p/original${likeRecommend.recommend.poster_path}`"
          class="w-2/5 rounded cursor-pointer" />
        <img v-else @click="goDetail(likeRecommend.recommend.id)" src="@/assets/images/noPoster.png" alt="noposter"
          class="w-2/5 rounded cursor-pointer" >
        <div class="ml-4 flex flex-col justify-between h-full">
          <div>
            <div class="flex items-center justify-between gap-1">
              <h2 class="text-lg text-blue-200">{{ likeRecommend.recommend.title }}</h2>
              <div class="flex items-center">
                <i class="fas fa-star text-sm text-yellow-400"></i>
                <span class="ml-1 text-sm">{{ Math.round(likeRecommend.recommend.rating_avg * 10) / 10 }}</span>
              </div>
            </div>
            <p class="text-blue-300 text-sm">{{ likeRecommend.recommend.release_date }}</p>
          </div>
          <p class="mt-4 text-sm text-blue-100"><span class="font-bold text-base">{{ likeRecommend.target.title }}</span> 영화를 좋아하신다면 이 영화는 어때요?</p>
        </div>
      </div>
    </div>
    <div v-else="!likeRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900 flex flex-col items-center justify-center text-center">
      <i class="fas fa-film text-gray-400 text-6xl mb-4"></i>
      <h2 class="text-lg text-blue-200 mb-4">아직 선호하는 영화가 없으시군요?</h2>
      <router-link
          :to="{
            name: 'prefer',
          }" 
          class="bg-blue-950 text-white rounded px-4 py-2 hover:bg-blue-800">영화 찾으러 가기
      </router-link>
    </div>
    <!-- 좋아요기반 -->

    <!-- 보고싶어요기반 -->
    <div v-if="wishRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900">
      <div class="flex items-start justify-between">
        <img v-if="wishRecommend.recommend.poster_path" @click="goDetail(wishRecommend.recommend.id)"
          :src="`https://image.tmdb.org/t/p/original${wishRecommend.recommend.poster_path}`"
          class="w-2/5 rounded cursor-pointer" />
        <img v-else @click="goDetail(wishRecommend.recommend.id)" src="@/assets/images/noPoster.png" alt="noposter"
          class="w-2/5 rounded cursor-pointer" >
        <div class="ml-4 flex flex-col justify-between h-full">
          <div>
            <div class="flex items-center justify-between gap-1">
              <h2 class="text-lg text-blue-200">{{ wishRecommend.recommend.title }}</h2>
              <div class="flex items-center">
                <i class="fas fa-star text-sm text-yellow-400"></i>
                <span class="ml-1 text-sm">{{ Math.round(wishRecommend.recommend.rating_avg * 10) / 10 }}</span>
              </div>
            </div>
            <p class="text-blue-300 text-sm">{{ wishRecommend.recommend.release_date }}</p>
          </div>
          <p class="mt-4 text-sm text-blue-100"><span class="font-bold text-base">{{ wishRecommend.target.title }}</span> 영화를 보고 싶으시다면 이 영화도 관심 있으실거에요!</p>
        </div>
      </div>
    </div>
    <div v-else="!wishRecommend" class="shadow-lg rounded p-4 text-white bg-gradient-to-br from-blue-950 to-blue-900 flex flex-col items-center justify-center text-center">
      <i class="fas fa-film text-gray-400 text-6xl mb-4"></i>
      <h2 class="text-lg text-blue-200 mb-4">아직 보고싶은 영화가 없으시군요?</h2>
      <p class="text-lg text-blue-200 mb-4">보고싶은 영화를 담아보세요.</p>
    </div>
    <!-- 보고싶어요기반 -->

  </div>
</template>


<script setup>
import { useUserStore } from '@/stores/user'
import axios from 'axios';
import { onMounted, ref } from 'vue';
import router from '../router';

const store = useUserStore()

const genreRecommend = ref(null)
const likeRecommend = ref(null)
const wishRecommend = ref(null)

onMounted(() => {
  if (!store.token) {
    return
  }

  getLikeRecommend()
  getGenreRecommend()
  getWishRecommend()
})

const getLikeRecommend = function() {
  axios({
    method : 'GET',
    url  : `${store.API_URL}/api/v1/recommends/movie/`,
    headers: {
      Authorization: `Token ${store.token}`
    } 
  })
  .then((res) => {
    likeRecommend.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}


const getGenreRecommend = function() {
  axios({
    method : 'GET',
    url  : `${store.API_URL}/api/v1/recommends/genre/`,
    headers: {
      Authorization: `Token ${store.token}`
    } 
  })
  .then((res) => {
    genreRecommend.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}


const getWishRecommend = function() {
  axios({
    method : 'GET',
    url  : `${store.API_URL}/api/v1/recommends/wish/`,
    headers: {
      Authorization: `Token ${store.token}`
    } 
  })
  .then((res) => {
    wishRecommend.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}

const goDetail = function (movieId) {
  router.push({name: 'movieDetail', params: {movieId: movieId}})
}


</script>


<style scoped>

</style>