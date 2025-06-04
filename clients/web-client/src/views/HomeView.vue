<template>
  <div class="home">
    <h1>Bienvenido, {{ authStore.user?.full_name }}</h1>
    <p>Rol: {{ authStore.user?.role }}</p>
    <div v-if="authStore.user?.role === 'owner'">
      <h2>Acciones para dueños</h2>
      <!-- Contenido específico para dueños -->
    </div>
    <div v-else-if="authStore.user?.role === 'doctor'">
      <h2>Acciones para veterinarios</h2>
      <!-- Contenido específico para veterinarios -->
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>