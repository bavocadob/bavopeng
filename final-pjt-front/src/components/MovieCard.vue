<template>


<router-link
    :to="{
      name: 'movieDetail',
      params: {
        movieId: movie.id,
      },
    }"
  >
  <div class="card">
    <img
          v-if="movie.poster_path"
          class="movie-image"
          :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
        />
    <div class="card-inner">
      <p class="movie-title text-white">
        {{ movie.title }}
      </p>
    </div>
  </div>
</router-link>
</template>

<script setup>
defineProps({
  movie : {
    type: Object,
  }
})

</script>

<style scoped>

.movie-image {
  width: 100%;
  height: 18rem;
}

</style>
