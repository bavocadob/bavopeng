<template>
  <div>
    <div class="pb-8">
      <table v-if="articles.length > 0">
        <thead class="bg-gray-200">
          <tr>
            <th class="py-2 px-4" style="width: 4rem">번호</th>
            <th class="py-2 px-4">제목</th>
            <th class="py-2 px-4" style="width: 10rem">글쓴이</th>
            <th class="py-2 px-4" style="width: 6rem">작성일</th>
            <th class="py-2 px-4" style="width: 4rem">추천</th>
          </tr>
        </thead>
        <tbody v-for="article in articles" :key="article.id" class="bg-white">
          <tr>
            <td class="py-2 px-4">{{ article.id }}</td>
            <router-link
              :to="{
                name: 'articleDetail',
                params: {
                  articleId: article.id,
                },
              }"
            >
              <td class="py-2 px-4 hover:text-blue-500">
                {{ article.title }}                
                <span v-if="article.comment_cnt" class="text-red-500">[{{ article.comment_cnt }}]</span>
                <i v-if="article.has_image" class="fas fa-image text-green-700"></i>
              </td>
            </router-link>
            <td class="py-2 px-4">
              <!-- todo: 라우터 링크 -> 프로필 -->
                {{
                  article.user.profile.nickname
                }}
              <!-- 라우터 링크 -> 프로필  -->
            </td>
            <td class="py-2 px-4">{{ formatDate(article.created_at) }}</td>
            <td class="py-2 px-4">{{ article.liked_cnt }}</td>
          </tr>
        </tbody>
      </table>
      <div class="flex flex-col items-center justify-center bg-gray-100 py-60 px-4 rounded" v-else>
        <i class="fas fa-exclamation-circle text-3xl mb-4"></i>
        <p class="text-lg text-gray-500">아직 작성된 게시글이 없습니다.</p>
      </div>
    </div>

    <div class="text-zinc-300">
      <Paging 
        :pageData="pageData"
        @change-page="changePage"
        :textColor="'text-white'"
        :textCurrentColor="'text-white'"
      />
    </div>

    <div class="mt-4">
      <CommunitySearch />
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect, watch, onMounted } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute, useRouter } from 'vue-router'
import Paging from '@/components/Paging.vue'
import CommunitySearch from '@/components/CommunitySearch.vue'
import axios from 'axios'


const store = useUserStore()
const route = useRoute()
const router = useRouter()
const articles = ref([])

const pageData = ref({
  maxPage : 1 ,
  currentPage : 1,
  pageInterval : 10,
})



watchEffect(() => {
  pageData.value.currentPage = !isNaN(route.query.page) ? Number(route.query.page) : 1;
})


onMounted(() => {
  getArticles()
})

const getArticles = function() {
  const params = {};
  if (route.query.query) {
    params.query = route.query.query;
  }
  if (route.query.querytype) {
    params.querytype = route.query.querytype;
  }
  axios({
    method : 'GET',
    url : `${store.API_URL}/api/v1/article/pages/${pageData.value.currentPage}/`,
    params: params,
  })
  .then((res) => {
    articles.value = res.data.results
    pageData.value.maxPage = res.data.num_pages
  })
  .catch((err) => console.log(err))
}


const formatDate = (dateStr) => {
  const date = new Date(dateStr)
  const year = date.getFullYear()
  const month = ("0" + (date.getMonth() + 1)).slice(-2)
  const day = ("0" + date.getDate()).slice(-2)
  
  return `${year}-${month}-${day}`
}

const changePage = function(page) {
  const hasQuery = route.query.query !== undefined && route.query.query !== null
  const hasQueryType = route.query.querytype !== undefined && route.query.querytype !== null

  let routeObj = {
    name : 'community',
    query : {
      page : page,
    }
  }
  if (hasQuery) {
    routeObj.query.query = route.query.query
  }
  if (hasQueryType) {
    routeObj.query.querytype = route.query.querytype
  }

  router.push(routeObj);
}

watch(() => route.query, (newValue) => {
  getArticles()
})


</script>

<style scoped>
table {
  box-shadow: 0px 1px 2px 1px rgba(0, 0, 0, 0.1), 0px 1px 2px 1px rgba(0, 0, 0, 0.06);
  border-radius: 8px;
  overflow: hidden;
  width: 100%;
}

th {
  padding: 0.5rem;
  text-align: center;
  font-size: 14px;
  font-weight: 500;
}

td {
  padding: 0.5rem;
  font-size: 14px;
  text-align: center;
}
</style>