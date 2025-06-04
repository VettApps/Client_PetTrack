<template>
  <div class="register">
    <h1>Registro</h1>
    <form @submit.prevent="handleRegister">
      <div>
        <label for="full_name">Nombre completo:</label>
        <input id="full_name" v-model="form.full_name" type="text" required>
      </div>
      <div>
        <label for="email">Email:</label>
        <input id="email" v-model="form.email" type="email" required>
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input id="password" v-model="form.password" type="password" required>
      </div>
      <div>
        <label for="role">Rol:</label>
        <select id="role" v-model="form.role" required>
          <option value="owner">Dueño de mascota</option>
          <option value="doctor">Veterinario</option>
        </select>
      </div>
      <button type="submit">Registrarse</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
    <p>¿Ya tienes cuenta? <router-link to="/login">Inicia sesión</router-link></p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useRouter } from 'vue-router'

const form = ref({
  full_name: '',
  email: '',
  password: '',
  role: 'owner'
})
const error = ref('')
const authStore = useAuthStore()
const router = useRouter()

const handleRegister = async () => {
  try {
    await authStore.register(form.value)
    router.push('/')
  } catch (err) {
    error.value = err.detail || 'Error al registrarse'
  }
}
</script>

<style scoped>
.register {
  max-width: 400px;
  margin: 0 auto;
}

form div {
  margin-bottom: 1rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
}

input, select {
  width: 100%;
  padding: 0.5rem;
  font-size: 1rem;
}

button {
  background-color: #42b983;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>