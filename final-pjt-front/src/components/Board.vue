<template>
  <div>
    <div class="border-b border-gray-400 pb-8 mb-8">
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
            <!-- todo : 라우터 링크 -> 게시글 -->
              <td class="py-2 px-4 hover:text-blue-500">
                {{ article.title }}
                <span class="text-red-500">[{{ article.comment_cnt }}]</span>
              </td>
            <!-- todo : 라우터 링크 -->
            <td class="py-2 px-4">
              <!-- todo: 라우터 링크 -> 프로필 -->
                <!-- {{
                  store.userinfo.profile.nickname
                }} -->
              <!-- 라우터 링크 -> 프로필  -->
            </td>
            <td class="py-2 px-4">{{ article.created_at }}</td>
            <td class="py-2 px-4">{{ article.likes_count }}</td>
          </tr>
        </tbody>
      </table>
      <div class="flex items-center justify-center" v-else>
        <i class="fas fa-exclamation-circle text-3xl mb-4"></i>
        <p class="text-lg text-gray-500">아직 작성된 게시글이 없습니다.</p>
      </div>
    </div>

    <div class="mt-4">
      <!-- todo : 페이지 -->
    </div>

    <div class="mt-4">
      <!-- todo : 검색창 -->
    </div>
  </div>
</template>

<script setup>
import { ref, watchEffect } from 'vue'
import { useUserStore } from '@/stores/user'
import { useRoute } from 'vue-router'
import axios from 'axios'


const store = useUserStore()
const route = useRoute()
const articles = ref([])

const page = ref(1);
watchEffect(() => {
  page.value = route.query.page ? Number(route.query.page) : 1;
  console.log(page.value)
  // todo : axios로 게시글 목록 받아와야함
});



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