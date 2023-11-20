<template>
  <div class="editor mx-auto my-10 p-5 bg-white shadow-md rounded-lg max-w-3xl">
    <input
      type="text"
      v-model="title"
      class="editor-title w-full p-3 mb-5 text-lg text-gray-900 placeholder-gray-500 border-b-2 border-gray-200 outline-none"
      placeholder="제목을 입력하세요."
    />
    <QuillEditor 
      v-model:content="content" contentType="html"
      :modules="modules"
      :toolbar="toolbar"
      class="h-96 border-gray-200 border rounded-lg"
    >
    </QuillEditor>

    <div class="mt-5 flex justify-end">
      <button class="bg-blue-500 hover:bg-blue-500 hover:opacity-90 text-white py-2 px-5 rounded-lg transition duration-200 ease-in-out" @click="submit">
        글 쓰기
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { QuillEditor } from '@vueup/vue-quill';
import '@vueup/vue-quill/dist/vue-quill.snow.css'
import ImageUploader from 'quill-image-uploader';

import axios from 'axios'

const title = ref('')
const content = ref('');

const modules = {
        name: 'imageUploader',
        module: ImageUploader,
        options: {
          upload: file => {
            return new Promise((resolve, reject) => {
              const formData = new FormData();
              formData.append("image", file);
              axios(
                {
                  method: "POST",
                  data: formData,
                  url: 'http://127.0.0.1:8000/api/v1/article/image/'
                }
              )
                .then(response => response.data)
                .then(result => {
                  console.log(result);
                  resolve(result.url);
                })
                .catch(error => {
                  reject("Upload failed");
                  console.error("Error:", error);
                });
            });
            }
          }
  }


const toolbar = [
      ['bold', 'italic', 'underline', 'strike'],
      ['blockquote', 'code-block'],
      [{ 'list': 'ordered' }, { 'list': 'bullet' }],
      [{ 'color': [] }, { 'background': [] }],
      ['image']
    ]

const submit = async () => {
  try {
    console.log(content.value)
    console.log(title.value)
    
  } catch (error) {
    console.error(error)
  }
}


</script>

<style scoped>

</style>

