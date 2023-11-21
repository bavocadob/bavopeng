<template>
  <div class="absolute right-2 w-16 bg-white shadow rounded-md border border-gray-200">
    <div class="text-sm">
      <button @click="editArticle(article)" class="block w-full px-2 py-2 border-b border-gray-200">수정</button>
      <button @click="deleteArticle()" class="block w-full px-2 py-2">삭제</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const articleId = ref(route.params.id);

const editArticle = (article) => {
  // router.push({ name: 'CommunityEdit', params: { article } });
};

const deleteArticle = function() {

}
</script>

<style scoped>

</style>