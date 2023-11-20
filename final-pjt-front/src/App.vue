<template>
  <header>
    <HeaderView />
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink :to="{ name : 'articleCreate'}">ArticleCreate</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
  <!-- <MovieView /> -->
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MovieView from './views/MovieView.vue'
import HeaderView from '@/components/HeaderView.vue'

</script>


<style scoped>

</style>
