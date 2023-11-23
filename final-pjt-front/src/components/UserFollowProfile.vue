<template>
    <div>
      <div class="flex flex-wrap items-center bg-gray-200 m-4 p-8 rounded-md">
        <img 
          v-if="isProfile" :src="user.profile.profile_img" alt="Profile Image" 
          class="w-20 h-20 object-cover rounded-full border-2 border-gray-200 outline outline-indigo-600 outline-offset-2"
        />
        <img 
          v-else src="@/assets/images/anonymous_square.png" alt="Profile Image" 
          class="w-20 h-20 object-cover rounded-full border-2 border-gray-200 outline outline-indigo-600 outline-offset-2"
          />
        <p 
          class="text-2xl font-semibold ms-10"
        >{{ user.profile.nickname }}</p>
      </div>
    </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  user: {
    type: Object
  }
})

const isProfile = computed(() => {
  return props.user.profile.profile_img ? true : false
})

</script>

<style scoped>

</style>