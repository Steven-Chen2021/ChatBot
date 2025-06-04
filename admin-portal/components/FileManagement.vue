<template>
  <div class="files-container">
    <h2>檔案管理</h2>
    <ul>
      <li v-for="name in files" :key="name">{{ name }}</li>
    </ul>
    <p v-if="files.length === 0">尚無檔案</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

const files = ref<string[]>([])

onMounted(async () => {
  try {
    const res = await fetch('/admin/files')
    if (res.ok) {
      files.value = await res.json()
    }
  } catch {
    // ignore fetch errors in demo
  }
})
</script>

<style scoped>
.files-container {
  padding: 16px;
}
</style>
