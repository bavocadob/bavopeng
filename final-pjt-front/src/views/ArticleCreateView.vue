<template>
  <div id="app">
    <quill-editor 
      v-model="content" 
      ref="myQuillEditor"
      :options="editorOption"
    >
    </quill-editor>
    <button @click="submit">제출</button>
  </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css';
import axios from 'axios'

let content = ref('')

let editorOption = {
  theme: 'snow',
  placeholder: '내용을 입력하세요...',
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
      ['blockquote', 'code-block'],
      [{ 'list': 'ordered'}, { 'list': 'bullet' }],
      [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults
      ['image']                                 // link and image, video
    ],
  }
}


const submit = async () => {
  try {
    await axios.post('http://localhost:8000/api/v1/', { content: content.value })
    alert('게시글이 성공적으로 업로드되었습니다.')
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
#app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}
</style>

