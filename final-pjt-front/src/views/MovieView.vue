<template>
<h1>영화 목록</h1>

<p>현재 상영중인 영화</p>
<MovieSwiper :movies="nowShowing" />
<p>개봉 예정 영화</p>
<MovieSwiper :movies="upcoming" />
</template>

<script setup>
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
