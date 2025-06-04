<template>
  <nav class="nav">
    <router-link to="/prompts">提示設定</router-link> |
    <router-link to="/upload">檔案上傳</router-link> |
    <router-link to="/files">檔案管理</router-link> |
    <router-link to="/logs">使用紀錄</router-link>
  </nav>
  <router-view />
</template>

<script setup></script>

<style scoped>
.nav {
  padding: 8px;
  background: #f3f3f3;
  display: flex;
  gap: 8px;
}
</style>
