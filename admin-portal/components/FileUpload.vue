<template>
  <div class="upload-container">
    <h2>檔案上傳</h2>
    <form @submit.prevent="submit">
      <input type="file" @change="onFileChange" />
      <button type="submit">上傳</button>
    </form>
    <p v-if="status">{{ status }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const file = ref<File | null>(null)
const status = ref('')

function onFileChange(e: Event) {
  const target = e.target as HTMLInputElement
  file.value = target.files ? target.files[0] : null
}

async function submit() {
  if (!file.value) return
  const formData = new FormData()
  formData.append('file', file.value)
  try {
    const res = await fetch('/admin/upload', {
      method: 'POST',
      body: formData,
    })
    if (!res.ok) throw new Error('upload failed')
    const data = await res.json()
    status.value = `成功上傳：${data.filename}`
  } catch (err) {
    status.value = '上傳失敗'
  }
}
</script>

<style scoped>
.upload-container {
  padding: 16px;
}
form {
  display: flex;
  gap: 8px;
  align-items: center;
}
button {
  padding: 4px 12px;
}
</style>
