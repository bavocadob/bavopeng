<template>
  <div class="p-2 bg-gray-200 flex flex-col items-center gap-2">
    <img class="h-full"
      v-if="movie.poster_path"
      :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`"
    />
    <div>
      <p class="text-center">
        {{ movie.title }}
      </p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  movie : {
    type: Object,
  }
})

</script>

<style scoped>

</style>