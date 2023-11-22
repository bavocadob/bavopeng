<template>
  <div class="flex items-center justify-center mt-8">
    <button
      class="p-2"
      @click="goToPrevPage"
      :disabled="currentPage === 1"
    >
      <i class="fas fa-chevron-left"></i>
    </button>
    <button
      v-for="page in pages"
      :key="page"
      class="p-2"
      :class="[{ 'font-bold underline decoration-indigo-500/30 decoration-2': page === currentPage },
                page === currentPage ? props.textCurrentColor : props.textColor
    ]"
      @click="goToPage(page)"
    >
      {{ page }}
    </button>
    <button
      class="p-2"
      @click="goToNextPage"
      :disabled="currentPage === maxPage"
    >
      <i class="fas fa-chevron-right"></i>
    </button>
  </div>
</template>

<script setup>
import { ref, computed, watchEffect } from 'vue'

const props = defineProps({
  pageData: Object,
  textColor : {
    type : String,
    default : ''
  },
  textCurrentColor : {
    type : String,
    default : 'text-blue-900'
  }
})
const emit = defineEmits(["changePage"])


const currentPage = ref(props.pageData.currentPage)
const maxPage = ref(props.pageData.maxPage)
const pageInterval = ref(props.pageData.pageInterval)

const startPage = computed(() => {
  let start = currentPage.value - Math.floor(pageInterval.value / 2)
  return Math.max(start, 1)
})

const endPage = computed(() => {
  let end = startPage.value + pageInterval.value - 1
  return Math.min(end, maxPage.value)
})

const pages = computed(() => {
  let pages = [];
  for (let i = startPage.value; i <= endPage.value; i++) {
    pages.push(i)
  }
  return pages
})

const goToPage = (page) => {
  currentPage.value = page
  emit('changePage', page)
}

const goToPrevPage = () => {
  if (currentPage.value > 1) {
    goToPage(currentPage.value - 1)
  }
}

const goToNextPage = () => {
  if (currentPage.value < maxPage.value) {
    goToPage(currentPage.value + 1)
  }
}


watchEffect(() => {
  currentPage.value = props.pageData.currentPage;
  maxPage.value = props.pageData.maxPage;
  pageInterval.value = props.pageData.pageInterval;
})

</script>

<style scoped>
button {
  border: none;
  margin: 0 5px;
  transition: background-color 0.3s ease;
}
button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
