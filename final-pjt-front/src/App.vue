<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
  <MovieView />
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MovieView from './views/MovieView.vue'


</script>


<style scoped>

</style>
