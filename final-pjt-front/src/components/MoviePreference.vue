<template>
  <div class="w-3/5 mx-auto">
    <div class="my-20 text-white text-center">
      <h1
        class="text-4xl font-bold"
      >당신의 취향을 알려주세요!</h1>
      <h3>취향을 반영하여 영화를 추천해드립니다.</h3>
    </div>
    <div class="grid grid-cols-4 gap-10 my-10">
      <MoviePrefernceCard
        v-for="movie in movies"
        :movie="movie"
        :key="movie.id"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import MoviePrefernceCard from '@/components/MoviePrefernceCard.vue'
import axios from 'axios'

const movieList = [157336, 155, 122906, 872585, 150540, 27205, 138843, 176, 313369, 5123, 361743, 299534, 68718, 916224, 4935, 129, 198663, 11658, 496243, 1165656]
const movies = ref([])
axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/api/v1/movie/simple/',
    params: {
      'id': movieList
    }
  })
    .then((res) => {
      // console.log(res)
      movies.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
</script>

<style scoped>

</style>