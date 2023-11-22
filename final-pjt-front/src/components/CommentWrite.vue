<template>
  <div>
    <p class="mb-2 text-lg font-bold">Comment</p>
    <div class="flex items-center mt-4 mb-8">
      <input
        class="w-full bg-gray-200 rounded-full py-3 px-6 mr-2 outline-none"
        type="text"
        v-model.trim="content"
        @keyup.enter="createComment"
        :placeholder="
          isLogin ? '댓글을 입력하세요.' : '댓글을 입력하려면 로그인하세요.'
        "
        :disabled="!isLogin"
      />
    </div>
  </div>
</template>

<script setup>
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'
import { ref } from 'vue'

import axios from 'axios'


const store = useUserStore()
const route = useRoute()
const router = useRouter()

const isLogin = store.isLogin
const content = ref('')


const createComment = function() {
  const data = {
    content : content.value,
  }

  axios({
    method : 'POST',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/comment/`,
    data,
    headers : {
      Authorization : `token ${store.token}`
    }
  })
  .then((res) => {
    console.log(res)
    router.push({
      name: 'articleDetail',
      params: {
        articleId: route.params.articleId
      },
    })
  })
  .catch((err) => console.log(err))

}


</script>


<style scoped>

</style>

