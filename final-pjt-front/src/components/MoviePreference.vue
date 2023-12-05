<template>
  <div class="w-3/5 mx-auto flex flex-col items-center">
    <div class="mt-28 my-12 text-white text-center">
      <h1
        class="text-4xl font-bold mb-4"
      >당신의 취향을 알려주세요!</h1>
      <h3 class="text-xl">5개 이상의 영화를 골라주세요.<br>취향을 반영하여 영화를 추천해드립니다.</h3>
    </div>
    <div class="grid grid-cols-4 max-md:grid-cols-2 max-xl:grid-cols-3 gap-12 mb-14">
      <MoviePrefernceCard
        @click="likeMovie(movie.id)"
        v-for="movie in movies"
        :movie="movie"
        :key="movie.id"
        class="rounded-md"
        :class="{'outline outline-4  outline-offset-4 outline-indigo-400':movie.is_like}"
      />
    </div>
    <div
      @click="goMain"
      class="my-12 px-4 py-2 text-xl font-semibold text-white fixed top-0 right-8 rounded-md bg-gray-400 cursor-default"
      :class="{'hover:cursor-pointer bg-indigo-500 hover:bg-indigo-800': likeCount > 4}"
    >내 취향의 영화 보러가기
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import MoviePrefernceCard from '@/components/MoviePrefernceCard.vue'
import axios from 'axios'

const router = useRouter()
const store = useUserStore()

const movieList = [157336, 155, 122906, 872585, 150540, 27205, 138843, 176, 313369, 5123, 361743, 299534, 68718, 916224, 4935, 129, 198663, 11658, 496243, 1165656, 572164, 567646, 291549, 508642, 75656, 228150, 91073, 38, 152601, 207703, 575264, 8966, 673, 385687, 509, 301528]
const movies = ref([])
const likeCount = ref(0)

axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/movie/simple/',
    headers: {
      Authorization: `Token ${store.token}`
    },
    params: {
      'id': movieList
    }
  })
    .then((res) => {
      movies.value = res.data
      movies.value.forEach(movie => {
        if (movie.is_like) {
          likeCount.value += 1
        }})
    })
    .catch((err) => {
      console.log(err)
    })

const likeMovie = function (id) {
  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/movie/${id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      const targetMovie = movies.value.find(movie => movie.id === res.data.movie_id)
      targetMovie.is_like = !targetMovie.is_like
      if (targetMovie.is_like) {
        likeCount.value += 1
      } else {
        likeCount.value -= 1
      }
    })
    .catch((err) => {
      console.log(err)
    })
}

const goMain = function () {
  if ( likeCount.value > 4 ) {
    router.replace({name: 'main'})
  }
}
</script>

<style scoped>

</style>