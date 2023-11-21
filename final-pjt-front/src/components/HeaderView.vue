<template>
<div>
  <h1>영화검색</h1>
  <input type="text" @input="searchMovie">
  <p v-for="movie in searchdMovies" :key="movie.id">
    {{ movie.title }}
  </p>
</div>

</template>

<script setup>
import { debounce } from 'lodash'
import { ref } from 'vue'
import axios from 'axios'


const BASE_URL = 'http://127.0.0.1:8000'
const searchdMovies = ref([])


const searchMovie = debounce(function(event) {
  const searchQuery = event.target.value
  if (searchQuery.trim()){
    axios({
      'method' : 'GET',
      'url' : `${BASE_URL}/api/v1/movie/search/${searchQuery}`,
    })
    .then((res) => searchdMovies.value = res.data)
    .catch((err) => console.log(err))
  } 
}, 300)
</script>

<style scoped>
</style>
