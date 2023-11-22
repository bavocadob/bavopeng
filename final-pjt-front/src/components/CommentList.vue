<template>
  <div>
    <Comment
      v-for="comment in comments"
      :key="comment.id"
      :comment="comment"
      @reload-comment="getComments"
    />
    <Paging 
      :pageData="pageData"
      @change-page="changePage"
    />
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref, onMounted, watch } from 'vue'
import { useArticleStore } from '@/stores/article'
import { useRoute } from 'vue-router'
import Comment from '@/components/Comment.vue'
import Paging from '@/components/Paging.vue'


const store = useArticleStore()
const route = useRoute()
const comments = ref([])

const pageData = ref({
  maxPage : 1 ,
  currentPage : 1,
  pageInterval : 5,
})

onMounted(() => {
  getComments()

})


const getComments = function() {
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/article/${route.params.articleId}/comment/${pageData.value.currentPage}/`
  })
  .then((res) => {
    comments.value = res.data.results
    pageData.value.maxPage = res.data.num_pages
    pageData.value.currentPage = res.data.current_page
  })
  .catch((err) => console.log(err))

}

const changePage = function(page) {
  pageData.value.currentPage = page
  getComments()
}


watch(() => store.reloadComment, (newValue) => {
  if (store.reloadComment){
    getComments()
    store.toggleReloadComment()
  }
})

</script>

<style scoped>
</style>
