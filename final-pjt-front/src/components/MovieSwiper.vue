<template>
  <div>
    <div>
      <swiper
        :slides-per-view="6"
        :space-between="30"
      >
        <swiper-slide v-for="movie in movies" :key="movie.id">
          <MovieCard :movie="movie"/>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue'
import MovieCard from './MovieCard.vue'
import 'swiper/css'

defineProps({
  movies : {
    type:Array,
  }
})


</script>

<style scoped>


</style>
