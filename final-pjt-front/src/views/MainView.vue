<template>
<!-- <h1>영화 목록</h1> -->
<h2 class="text-3xl text-slate-100 ms-8 mb-4 font-semibold">
  이 영화는 어때요?
</h2>
<div class="bg-indigo-800 mt-4 mb-8 p-6 text-white rounded-lg">
  <RecommendMovie />
</div>
<h2 class="text-3xl text-slate-100 ms-8 mb-4 font-semibold">
  현재 상영중인 영화
</h2>
<div class="bg-indigo-800 mt-4 mb-8 p-6 text-white rounded-lg">
  <MovieSwiper :movies="nowShowing" />
</div>
<h2 class="text-3xl text-slate-100 ms-8 mb-4 font-semibold">
  개봉 예정 영화
</h2>
<div class="bg-indigo-800 mt-4 mb-8 p-6 text-white rounded-lg">
  <MovieSwiper :movies="upcoming" />
</div>
</template>

<script setup>
import RecommendMovie from '@/components/RecommendMovie.vue'
import MovieSwiper from '@/components/MovieSwiper.vue'
import axios from 'axios'
import { ref, onMounted } from 'vue'

const BASE_URL = 'http://127.0.0.1:8000'
const nowShowing = ref([])
const upcoming = ref([])


onMounted(() => {
  const target = [
    {
      url : 'now-showing',
      data : nowShowing,
    },
    {
      url : 'upcoming',
      data : upcoming,
    },
  ]

  target.forEach((item) => {
    axios({
      'method' : 'GET',
      'url' : `${BASE_URL}/api/v1/movie/${item.url}/`
    })
    .then((res) => item.data.value=res.data)
    .catch((err) => console.log(err))
  })
  
  


})


</script>

<style scoped>
</style>
