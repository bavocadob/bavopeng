<template>
  <div class="relative">
    <div class="bg-white flex items-center">
      <i class="fas fa-search px-2 py-1"></i>
      <input 
        v-model="searchTerm" 
        @input="searchMovie"
        placeholder="Search" 
        class="w-full py-1 px-2 outline-none"
      >
    </div>
    <div class="absolute w-full mt-1 bg-white shadow" v-if="searchResults">
      <a 
        class="p-2 block hover:bg-gray-200 cursor-pointer text-sm"
        v-for="movie in searchResults"
        :key="movie.id"
        :href="`/movie/${movie.id}`"
      >
        {{ movie.title }}  
      </a>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { debounce } from 'lodash'
import { useUserStore } from '@/stores/user'

const searchTerm = ref('')
const searchResults = ref([])
const store = useUserStore()


const searchMovie = debounce(function(event) {
  if (searchTerm.value.trim()){
    axios({
      'method' : 'GET',
      'url' : `${store.API_URL}/api/v1/movie/search/${searchTerm.value}`,
    })
    .then((res) => {
      console.log(res)
      searchResults.value = res.data
    })
    .catch((err) => console.log(err))
  } else {
    searchResults.value = []
  }
}, 300)




</script>



<style scoped>
</style>
