<template>
  <div class="flex justify-between items-center border-b relative">
    <div>
      <div class="absolute top-4 right-0 cursor-pointer" @click="$emit('close')">
        <!-- 삭제버튼 아이콘 -->
      </div>

      <div class="flex items-center mt-4 mb-5">

        <div class="flex items-center ml-4">
          <img
            v-if="store.userInfo.profile.profile_img"
            :src="store.userInfo.profile.profile_img"
            class="w-8 h-8 rounded-full mr-4"
          />
          <img
            v-else
            src="@/assets/images/anonymous.png"
            class="w-8 h-8 rounded-full mr-4"
          />
          <div>
            <p class="font-bold">{{ store.userInfo.profile.nickname }}</p>
            <p class="text-sm text-gray-500">{{ formatDate(article.created_at) }}</p>
          </div>
        </div>
      </div>

      <p class="text-sm font-light mb-6">
        {{ comment.content }}
      </p>
    </div>
    <div></div>
  </div>
</template>


<script setup>

</script>

<style scoped>

</style>