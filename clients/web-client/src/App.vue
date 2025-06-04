<template>
  <div id="app">
    <nav v-if="authStore.user">
      <router-link to="/">Home</router-link> |
      <router-link to="/pets">Mascotas</router-link> |
      <router-link to="/appointments">Citas</router-link> |
      <a href="#" @click.prevent="logout">Cerrar sesión</a>
    </nav>
    <router-view/>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

const logout = () => {
  authStore.logout()
  router.push('/login')
}

// Fetch user on app initialization
authStore.fetchUser()
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 0 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>