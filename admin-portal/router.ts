import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  { path: '/prompts', component: () => import('./components/PromptConfig.vue') },
  { path: '/upload', component: () => import('./components/FileUpload.vue') },
  { path: '/files', component: () => import('./components/FileManagement.vue') },
  { path: '/logs', component: () => import('./components/UsageLogs.vue') },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})
