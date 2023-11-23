<template>
  <section>
    <div class="flex justify-center">
      <div class="w-3/5 mr-8">
        <div class="mb-8 bg-gray-200 shadow-sm rounded-lg">
          <div
            class="w-full h-80 bg-cover bg-center opacity-50 overflow-hidden rounded-t-lg"
            :style="{
'background-image': 'url(' + 'https://image.tmdb.org/t/p/original/' + movie.backdrop_path + ')',
            }"
          ></div>

          <div class="flex p-6">
            <img
              class="border-gray-200 w-48 z-10"
              :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
            />

            <div class="w-full ml-8">
              <div class="flex justify-between">
                <div>
                  <p class="text-2xl font-bold mb-1">
                    {{ movie.title }}
                  </p>

                  <p class="text-sm text-gray-500 mb-4">{{ movie.original_title }}</p>
                </div>
              </div>
              <div class="flex items-center mb-4">
                <div class="mr-1">
                  <p>{{ movie.release_date }}</p>
                </div>
                <div class="separator mx-4"></div>
                <p class="text-base">{{ movie.runtime }} 분</p>
                
              </div>
              <div class="flex items-center mb-5">
                  <span
                    class="mr-2 bg-gray-300 py-1 px-2 rounded-full text-sm font-semibold"
                    v-for="genre in movie.genres"
                    :key="genre.id"
                  >
                    {{ genre.name }}
                  </span>
                </div>
              <div class="flex flex-col justify-between">
                <div class="flex justify-between mb-4">
                  <div class="flex items-center">
                    <StarRatingVue 
                      v-model="movie.rating_avg"
                      :disableClick="true"
                      :starSize="34"
                      :starColor="'#4263EB'"
                      :numberOfStars="5"
                      />
                    <p class="text-lg font-bold ml-1">
                      {{ Math.round(movie.rating_avg * 10) / 10 }}
                    </p>
                  </div>
                </div>
                <div class="flex justify-between space-x-4">
                  <button 
                    class="flex flex-col items-center justify-center py-2 px-6 rounded-md cursor-pointer"
                    @click="likeMovie"
                  >
                    <i :class="`fas fa-thumbs-up text-3xl transform transition-transform duration-200 hover:scale-125 ${isLike ? 'text-indigo-900 hover:text-indigo-900' : 'text-gray-500 hover:text-gray-600'}`"></i>
                    <span class="text-xs mt-1">좋아요</span>
                  </button>
                  <button 
                    class="flex flex-col items-center justify-center py-2 px-6 rounded-md cursor-pointer"
                    @click="dislikeMovie"
                  >
                    <i :class="`fas fa-thumbs-down text-3xl transform transition-transform duration-200 hover:scale-125 ${isDislike ? 'text-indigo-900 hover:text-indigo-900' : 'text-gray-500 hover:text-gray-600'}`"></i>
                    <span class="text-xs mt-1">싫어요</span>
                  </button>
                  <button
                    class="flex flex-col items-center justify-center py-2 px-6 rounded-md cursor-pointer"
                    @click="wishMovie"
                    >
                    <i :class="`fas fa-heart text-3xl transform transition-transform duration-200 hover:scale-125 ${isWish ? 'text-indigo-900 hover:text-indigo-900' : 'text-gray-500 hover:text-gray-600'}`"></i>
                    <span class="text-xs mt-1">보고싶어요</span>
                  </button>
                </div>
              </div>


            </div>
          </div>
        </div>
        <div class="p-8 bg-gray-200 mb-8 shadow-sm rounded-lg">
          <div class="border-b border-gray-400 pb-8 mb-8">
            <h2 class="text-xl font-bold mb-4">줄거리</h2>

            <p class="text-base font-light">{{ movie.overview }}</p>
          </div>

          <div v-if="movie.trailer" class="border-b border-gray-400 pb-8 mb-8">
            <h2 class="text-xl font-bold mb-4">예고편</h2>

            <iframe
              class="w-full h-80"
              encrypted-media
              picture-in-picture
              allowfullscreen
              :src="'https://www.youtube.com/embed/' + movie.trailer" 
            ></iframe>
          </div>
          <div class="border-b border-gray-400 pb-8 mb-8">
            <h2 class="text-xl font-bold mb-4">출연진</h2>
            <ActorSwiper :actors="movie.actors" />
          </div>

        </div>
        <div class="p-8 mb-8 bg-gray-200 shadow-sm rounded-lg">
          <h1 class="text-xl font-bold mb-4">리뷰</h1>
          <MovieDetailMyReview
            :review="myReview"
            @open-modal="isModalOpen=true"
          />
          
          <MovieReviewModal
            v-if="isModalOpen" :movie="movie"
            @close-modal="isModalOpen=false"
            @update-review="updateMovieData"
          />
          <MovieDetailReview :reviews="movie.review_set?.slice(0, 3)" />
          <router-link v-if="movie.review_set?.length > 3" :to="{ name: 'reviewList', params: { movieId: movie.id }}">
            리뷰 {{ movie.review_set?.length }}개 모두 보기 
            <i class="fas fa-arrow-right"></i>
          </router-link>
        </div>
        <div class="p-8 bg-gray-200 shadow-sm rounded-lg">
          <h1 class="text-xl font-bold mb-4">커뮤니티 글</h1>
          <MovieArticleList 
            :articles="movie.article_set"
          />
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import StarRatingVue from '@/components/StarRating.vue'
import ActorSwiper from '@/components/ActorSwiper.vue'
import MovieDetailReview from '@/components/MovieDetailReview.vue'
import MovieDetailMyReview from '@/components/MovieDetailMyReview.vue'
import MovieReviewModal from '@/components/MovieReviewModal.vue'
import MovieArticleList from '@/components/MovieArticleList.vue'


import axios from 'axios'
import { useRoute } from 'vue-router'
import { onMounted, ref, computed, watchEffect } from 'vue'
import { useUserStore } from '@/stores/user'

const route = useRoute()
const store = useUserStore()
const movieId = route.params.movieId

const isModalOpen = ref(false)
const movie = ref({})
const reviews =ref([])

const isLike = ref(false)
const isDislike = ref(false)
const isWish = ref(false)

const likeCnt = ref(0)
const dislikeCnt = ref(0) 

onMounted(() => {
  updateMovieData()
})

watchEffect(() => {
  isLike.value = movie.value.is_like
  isDislike.value = movie.value.is_dislike
  isWish.value = movie.value.is_wish
})


const myReview = computed(() => {
  return movie.value.review_set?.find(review => review.user.id === store.userInfo.id);
})

const updateMovieData = function() {
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/movie/${movieId}/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    movie.value = res.data
  })
  .catch((err) => console.log(err))
}


const likeMovie = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/movie/${movieId}/like/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    isLike.value = res.data.is_like
    isDislike.value = res.data.is_dislike
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
  })
  .catch((err) => {
    console.log(err)
  })
}


const dislikeMovie = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/movie/${movieId}/dislike/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    isLike.value = res.data.is_like
    isDislike.value = res.data.is_dislike
    likeCnt.value = res.data.like_cnt
    dislikeCnt.value = res.data.dislike_cnt
  })
  .catch((err) => {
    console.log(err)
  })
}

const wishMovie = function() {
  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/movie/${movieId}/wish/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    isWish.value = res.data.is_wish
  })
  .catch((err) => {
    console.log(err)
  })
}


</script>

<style scoped>
.separator {
  border-left: 2px solid gray;
  height: 1em;
}

</style>
