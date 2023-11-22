<template>
<div class="flex justify-center">
  <div class="w-3/5 mr-8">
    <div class="p-8 bg-gray-200 shadow-sm rounded-lg">
      <MovieDetailReview :reviews="reviews" />
    </div>
  </div>
</div>
</template>

<script setup>
import axios from 'axios'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import MovieDetailReview from '@/components/MovieDetailReview.vue'


const route = useRoute()
const movieId = route.params.movieId
const reviews = ref([])

const pageData = ref({
  maxPage : 1 ,
  currentPage : 1,
  pageInterval : 10,
})


onMounted(() => {
  axios({
    method : 'GET',
    url : `http://127.0.0.1:8000/api/v1/movie/${movieId}/reviews/${pageData.value.currentPage}/`,
  })
  .then((res) => {
    console.log(res)
    reviews.value = res.data.results
    pageData.value.maxPage = res.data.num_pages
    pageData.value.currentPage = res.data.currentPage

  })
  .catch((err) => console.log(err))
})


</script>

<style scoped>
</style>
