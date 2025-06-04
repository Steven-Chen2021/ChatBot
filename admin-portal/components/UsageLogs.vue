<template>
  <div class="logs-container">
    <h2>使用紀錄</h2>
    <ul>
      <li v-for="log in logs" :key="log.id">{{ log.message }}</li>
    </ul>
    <p v-if="logs.length === 0">目前沒有紀錄</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'

interface Log {
  id: number
  message: string
}

const logs = ref<Log[]>([])

onMounted(async () => {
  try {
    const res = await fetch('/admin/logs')
    if (res.ok) {
      logs.value = await res.json()
    }
  } catch {
    // ignore fetch errors in demo
  }
})
</script>

<style scoped>
.logs-container {
  padding: 16px;
}
ul {
  padding-left: 20px;
}
</style>
