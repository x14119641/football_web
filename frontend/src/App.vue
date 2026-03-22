<script setup lang="ts">
import { ref, computed } from 'vue'
import PlayerTable from './components/PlayerTable.vue'
import type { Player } from './types/player'
import jugadoresData from './data/jugadores.json'

const players = ref<Player[]>(jugadoresData as Player[])
const searchQuery = ref('')

const filteredPlayers = computed(() => {
  const q = searchQuery.value.trim().toLowerCase()
  if (!q) return players.value
  return players.value.filter((p) => {
    const nombre = p.nombre ?? ''
    return String(nombre).toLowerCase().includes(q)
  })
})
</script>

<template>
  <main class="page">
    <h1>Jugadores</h1>
    <label class="search-field">
      <span>Buscar por nombre</span>
      <input
        v-model="searchQuery"
        type="search"
        placeholder="Escribir nombre..."
        autocomplete="off"
      />
    </label>
    <PlayerTable :players="filteredPlayers" />
  </main>
</template>

<style scoped>
.page {
  padding: 2rem;
  text-align: left;
}

.page h1 {
  margin-top: 0;
  margin-bottom: 1.5rem;
}

.search-field {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  margin-bottom: 1.25rem;
}

.search-field span {
  font-size: 0.85rem;
  color: var(--text);
}

.search-field input {
  max-width: 20rem;
  padding: 0.5rem 0.75rem;
  font-size: 1rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text-h);
}

.search-field input:focus {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.search-field input::placeholder {
  color: var(--text);
  opacity: 0.7;
}

</style>
