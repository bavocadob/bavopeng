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
import { useRoute, useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import axios from 'axios';

const store = useUserStore()
const route = useRoute();
const router = useRouter();
const articleId = ref(route.params.articleId);

const editArticle = (article) => {
  // router.push({ name: 'CommunityEdit', params: { article } })
  router.push({
    name : 'articleEdit',
    params : {
      articleId : articleId.value
    }
  })
};

const deleteArticle = function() {
  axios({
    method : 'DELETE',
    url : `${store.API_URL}/api/v1/article/${articleId.value}/`,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    router.push({
      name: 'community'
    })
  })
  .catch((err) => {
    console.log(err)
  })
}
</script>

<style scoped>

</style>