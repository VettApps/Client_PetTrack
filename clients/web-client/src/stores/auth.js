import { defineStore } from 'pinia'
import axios from 'axios'
import router from '../router'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    token: localStorage.getItem('token') || null,
    returnUrl: null
  }),
  actions: {
    async login(email, password) {
      try {
        const response = await axios.post('/api/token', {
          username: email,
          password: password
        })
        
        this.token = response.data.access_token
        localStorage.setItem('token', this.token)
        
        // Get user info
        const userResponse = await axios.get('/api/users/me', {
          headers: { Authorization: `Bearer ${this.token}` }
        })
        
        this.user = userResponse.data
        router.push(this.returnUrl || '/')
      } catch (error) {
        throw error.response?.data || error
      }
    },
    async register(userData) {
      try {
        await axios.post('/api/register', userData)
        await this.login(userData.email, userData.password)
      } catch (error) {
        throw error.response?.data || error
      }
    },
    logout() {
      this.user = null
      this.token = null
      localStorage.removeItem('token')
      router.push('/login')
    },
    async fetchUser() {
      if (this.token) {
        try {
          const response = await axios.get('/api/users/me', {
            headers: { Authorization: `Bearer ${this.token}` }
          })
          this.user = response.data
        } catch (error) {
          this.logout()
        }
      }
    }
  }
})