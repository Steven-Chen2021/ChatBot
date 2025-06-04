<template>
  <div class="prompt-container">
    <h2>系統提示設定</h2>
    <textarea v-model="prompt" rows="5" cols="40"></textarea>
    <button @click="save">儲存</button>
    <p v-if="saved">已儲存</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const prompt = ref('')
const saved = ref(false)

function save() {
  // 在真實情況下應送至後端儲存
  saved.value = true
  setTimeout(() => (saved.value = false), 2000)
}
</script>

<style scoped>
.prompt-container {
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
textarea {
  resize: vertical;
}
</style>
