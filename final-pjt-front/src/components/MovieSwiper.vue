<template>
  <div>
    <div>
      <swiper
        :slides-per-view="6"
        :space-between="30"
        :breakpoints="breakpoints"
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


const breakpoints = {
  320: {
    slidesPerView: 1,
    spaceBetween: 20
  },
  480: {
    slidesPerView: 2,
    spaceBetween: 20
  },
  720: {
    slidesPerView: 3,
    spaceBetween: 30
  },
  960: {
    slidesPerView: 4,
    spaceBetween: 30
  },
  1200: {
    slidesPerView: 5,
    spaceBetween: 30
  },
  1920: {
    slidesPerView: 6,
    spaceBetween: 30
  }
};

</script>

<style scoped>


</style>
