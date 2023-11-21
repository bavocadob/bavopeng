<template>
  <swiper
    :slides-per-view="7"
    :space-between="10"
  >
    <swiper-slide v-for="actor in actors" :key="actor.id">
      <ActorCard :actor="actor"></ActorCard>
    </swiper-slide>

  </swiper>
</template>

<script setup>
import { ref } from 'vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import 'swiper/swiper-bundle.css'
import ActorCard from '@/components/ActorCard.vue'

const props = defineProps({
  actors: {
    type: Array,
  }
})

</script>
