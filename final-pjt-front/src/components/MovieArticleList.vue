<template>
  <div class="swiper-container">
    <Swiper :slidesPerView="3" :spaceBetween="50" :pagination="{ clickable: true }" :breakpoints="breakpoints">
      <SwiperSlide v-for="(article, index) in articles" :key="index" class="grid grid-cols-1 gap-1 py-8 px-4">
        <router-link
          :to="{
            name: 'articleDetail',
            params: {
              articleId: article.id,
            },
          }"
        >
          <div class="w-full h-40 overflow-hidden rounded-lg mb-4">
            <img :src="getImage(article)" alt="Thumbnail" class="w-full h-full object-cover">
          </div>
          <div class="text-lg font-bold mb-2 line-clamp-1">{{ article.title }}</div>
          <div class="text-sm line-clamp-1">{{ article.content }}</div>
        </router-link>
      </SwiperSlide>
      
    </Swiper>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import 'swiper/css';

defineProps({
  articles: {
    type: Array,
  },
});

const breakpoints = {
  320: {
    slidesPerView: 1,
    spaceBetween: 20
  },
  768: {
    slidesPerView: 2,
    spaceBetween: 30
  },
  1240: {
    slidesPerView: 3,
    spaceBetween: 40
  },
};

const getImage = (article) => {
  if (article.first_img) return article.first_img;
  const canvas = document.createElement('canvas')
  const ctx = canvas.getContext('2d')
  ctx.fillStyle = '#ddd'
  ctx.fillRect(0, 0, canvas.width, canvas.height)
  ctx.font = '50px Arial'
  ctx.fillStyle = '#666'
  ctx.fillText(article.title.slice(0, 6), canvas.width / 4, canvas.height / 2)
  return canvas.toDataURL('image/png')
}

</script>

<style scoped>
.swiper-container {
  width: 100%;
  height: 100%;
}

.line-clamp-1 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 1;
  overflow: hidden;
}
</style>
