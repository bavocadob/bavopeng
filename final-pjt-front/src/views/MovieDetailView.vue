<template>
  <section>
    <div class="flex">
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

              <div class="flex items-center mb-20">
                <div class="mr-4">
                  <p>{{ movie.release_date }}</p>
                </div>
                <div class="separator mx-4"></div>
                <p class="text-lg mr-4">{{ movie.runtime }} 분</p>
                <div class="separator mx-4"></div>
                <div class="flex items-center">
                  <span
                    class="mr-2 bg-gray-300 py-1 px-2 rounded-full text-sm font-semibold"
                    v-for="genre in movie.genres"
                    :key="genre.id"
                  >
                    {{ genre.name }}
                  </span>
                </div>
              </div>

              <div class="flex justify-between">
                <div class="flex items-center">
               <StarRatingVue v-model="movie.rating_avg" :disableClick="true" :starSize="34" />

                  <p class="text-lg font-bold ml-1">
                    {{ Math.round(movie.rating_avg * 10) / 10 }}
                  </p>
                </div>

                <div class="flex items-center font-semibold bg-blue-500 border border-blue-500 text-white py-2 px-6 rounded-md cursor-pointer hover:bg-blue-600">
                  리뷰 쓰기
                </div>
              </div>

            </div>
          </div>
        </div>
        <div class="p-8 bg-gray-200 mb-8 shadow-sm rounded-lg">
          <div class="border-b border-gray-400 pb-8 mb-8">
            <h2 class="text-xl font-bold mb-4">줄거리</h2>

            <p class="text-lg font-light">{{ movie.overview }}</p>
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
        <div class="p-8 bg-gray-200 shadow-sm rounded-lg">
          <h1 class="text-xl font-bold mb-4">리뷰</h1>
          <MovieDetailMyReview />
          <MovieDetailReview :reviews="movie.review_set" />
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


import axios from 'axios'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'

const route = useRoute()
const movieId = route.params.movieId
const movie = ref({})


onMounted(() => {
  axios({
    method : 'GET',
    url : `http://127.0.0.1:8000/api/v1/movie/${movieId}/`
  })
  .then((res) => {
    console.log(res.data)
    movie.value = res.data
  })
  .catch((err) => console.log(err))
})



</script>

<style scoped>
.separator {
  border-left: 2px solid gray;
  height: 1em;
}

</style>
