<template>
  <div class="pet-list">
    <h2>Mis Mascotas</h2>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="pets.length === 0">No tienes mascotas registradas</div>
    <ul v-else>
      <li v-for="pet in pets" :key="pet.id">
        {{ pet.name }} - {{ pet.species }} ({{ pet.breed }})
      </li>
    </ul>
    <button @click="showAddPet = true">Añadir Mascota</button>
    
    <div v-if="showAddPet" class="modal">
      <div class="modal-content">
        <h3>Añadir Nueva Mascota</h3>
        <form @submit.prevent="addPet">
          <div>
            <label>Nombre:</label>
            <input v-model="newPet.name" required>
          </div>
          <div>
            <label>Especie:</label>
            <input v-model="newPet.species" required>
          </div>
          <div>
            <label>Raza:</label>
            <input v-model="newPet.breed">
          </div>
          <div>
            <label>Edad:</label>
            <input v-model="newPet.age" type="number">
          </div>
          <button type="submit">Guardar</button>
          <button type="button" @click="showAddPet = false">Cancelar</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const pets = ref([])
const loading = ref(true)
const showAddPet = ref(false)
const newPet = ref({
  name: '',
  species: '',
  breed: '',
  age: null
})

const fetchPets = async () => {
  try {
    const response = await axios.get('/api/pets')
    pets.value = response.data
  } catch (error) {
    console.error('Error fetching pets:', error)
  } finally {
    loading.value = false
  }
}

const addPet = async () => {
  try {
    await axios.post('/api/pets', newPet.value)
    await fetchPets()
    showAddPet.value = false
    newPet.value = { name: '', species: '', breed: '', age: null }
  } catch (error) {
    console.error('Error adding pet:', error)
  }
}

onMounted(fetchPets)
</script>

<style scoped>
.pet-list {
  max-width: 600px;
  margin: 0 auto;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  padding: 10px;
  border-bottom: 1px solid #eee;
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 80%;
  max-width: 500px;
}

form div {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}

button {
  margin-right: 10px;
  margin-top: 10px;
}
</style>