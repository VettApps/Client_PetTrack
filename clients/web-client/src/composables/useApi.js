import axios from 'axios'
import { useAuthStore } from '@/stores/auth'

export default function useApi() {
  const authStore = useAuthStore()
  
  const api = axios.create({
    baseURL: '/api'
  })
  
  // Add request interceptor to include token
  api.interceptors.request.use(config => {
    if (authStore.token) {
      config.headers.Authorization = `Bearer ${authStore.token}`
    }
    return config
  }, error => {
    return Promise.reject(error)
  })
  
  // Add response interceptor to handle 401 errors
  api.interceptors.response.use(response => response, error => {
    if (error.response?.status === 401) {
      authStore.logout()
    }
    return Promise.reject(error)
  })
  
  return {
    api
  }
}