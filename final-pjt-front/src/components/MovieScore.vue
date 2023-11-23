<template>
  <div>
    <div v-if="totalCnt === 0" class="text-sm mb-2">
      아직 유저들의 평가가 없어요
    </div>
    <div v-else class="flex justify-between text-sm mb-2">
      <div>별로에요 {{ dislikeRatio }}%</div>
      <div>좋아요 {{ likeRatio }}%</div>
    </div>
    <div 
      class="h-4 rounded overflow-hidden relative"
      :class="{ 'bg-gray-300': totalCnt === 0, 'bg-blue-500': totalCnt !== 0 }"
    >
      <div 
        v-if="totalCnt !== 0" 
        :style="{width: dislikeRatio + '%'}" 
        class="absolute h-full bg-red-500"
      ></div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  likeCnt: {
    type: Number,
    required: true
  },
  dislikeCnt: {
    type: Number,
    required: true
  }
})

const totalCnt = computed(() => props.likeCnt + props.dislikeCnt)
const likeRatio = computed(() => totalCnt.value ? Math.round((props.likeCnt / totalCnt.value) * 100) : 0)
const dislikeRatio = computed(() => totalCnt.value ? Math.round((props.dislikeCnt / totalCnt.value) * 100) : 0)
</script>

<style scoped>
</style>
