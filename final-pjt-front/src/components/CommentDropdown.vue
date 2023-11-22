<template>
  <div class="absolute right-2 w-16 bg-white shadow rounded-md border border-gray-200 z-10">
    <div class="text-sm">
      <!-- <button @click="editComment(article)" class="block w-full px-2 py-2 border-b border-gray-200">수정</button> -->
      <button @click="deleteComment" class="block w-full px-2 py-2">삭제</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useArticleStore } from '@/stores/article'
import { useUserStore } from '@/stores/user'

import axios from 'axios'

const route = useRoute()
const router = useRouter()
const store = useArticleStore()
const userStore = useUserStore() 

const props = defineProps({
  commentId: {
    type:Number
  }
})

const emit = defineEmits(['reloadComment'])

const editComment = (article) => {
  // router.push({ name: 'CommunityEdit', params: { article } });
};

const deleteComment = function() {
  axios({
    method : 'DELETE',
    url : `${store.API_URL}/api/v1/comment/${props.commentId}/`,
    headers : {
      Authorization : `token ${userStore.token}`
    }
  })
  .then((res) => {
    store.toggleReloadComment()
  })
  .catch((err) => console.log(err)) 
}

</script>

<style scoped>

</style>