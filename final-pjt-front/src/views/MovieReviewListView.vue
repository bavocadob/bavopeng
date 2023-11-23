<template>
<div class="flex justify-center">
  <div class="w-3/5 mr-8">
    <div class="p-8 bg-gray-200 shadow-sm rounded-lg">
      <MovieDetailReview
        :reviews="reviews"
        @sortReview="sortReview"
      />

      <Paging 
        :pageData="pageData"
        @change-page="changePage"
      />
    </div>
  </div>
</div>
</template>

<script setup>
import axios from 'axios'
import { useRoute } from 'vue-router'
import { onMounted, ref } from 'vue'
import MovieDetailReview from '@/components/MovieDetailReview.vue'
import Paging from '@/components/Paging.vue'
import { useUserStore } from '@/stores/user'

const store = useUserStore()
const route = useRoute()
const movieId = route.params.movieId
const reviews = ref([])
const sortOption = ref(0)

const pageData = ref({
  maxPage : 1,
  currentPage : 1,
  pageInterval : 10,
})


onMounted(() => {
  getReivews()
})

const getReivews = function() {
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/movie/${movieId}/reviews/${pageData.value.currentPage}/`,
    params : {
      sort_by : sortOption.value
    }
  })
  .then((res) => {
    reviews.value = res.data.results
    pageData.value.maxPage = res.data.num_pages
    pageData.value.currentPage = res.data.current_page
  })
  .catch((err) => console.log(err)) 
}


const sortReview = function(option) {
  sortOption.value = option
  pageData.value.currentPage = 1
  getReivews()
}


const changePage = function(page) {
  pageData.value.currentPage = page
  getReivews()
}



</script>

<style scoped>
</style>
