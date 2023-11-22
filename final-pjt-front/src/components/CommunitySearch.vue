<template>
  <div class="flex justify-center mb-32">
    <VueMultiselect
      v-model="querytype"
      :options="options"
      :searchable="false"
      :allow-empty="false"
      :showLabels="false"
      :optionHeight="20"
      placeholder="검색타입"
      class="w-28 ml-1 text-sm rounded-lg "
      label="label"
      trackBy="value"
    />
    <input @keyup.enter="search" type="text" v-model="query" class="ml-1 p-2 text-sm rounded-lg bg-gray-200 text-gray-700 border border-gray-300" />
    
    <div @click="search" class="ml-1 p-2 text-sm rounded-lg bg-red-500 text-white border border-red-500 hover:bg-red-600 cursor-pointer">검색</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import VueMultiselect from 'vue-multiselect'

const router = useRouter()

const querytype = ref({ label: '제목', value: 1 })
const options = ref([
  { label: '제목', value: 1 },
  { label: '내용', value: 2 },
  { label: '제목+내용', value: 3 }
])
const query = ref('')

const search = function() {
  console.log(querytype.value.value)
  console.log(query.value)
  router.push({
    name : 'community',
    query : {
      page : 1,
      querytype : querytype.value.value,
      query : query.value
    }
  })
} 

</script>
<style src="vue-multiselect/dist/vue-multiselect.css"></style>
<style>
  .multiselect__single {
    font-size: 0.8rem;
  }
</style>
<style scoped>

</style>
