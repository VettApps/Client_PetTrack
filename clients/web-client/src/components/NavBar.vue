<template>
  <nav>
    <router-link to="/">Inicio</router-link> |
    <router-link to="/pets">Mascotas</router-link> |
    <router-link to="/appointments">Citas</router-link> |
    <a href="#" @click.prevent="logout">Cerrar sesión</a>
  </nav>
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
</script>

<style scoped>
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