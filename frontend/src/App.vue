<script setup lang="ts">
import { ref, computed } from 'vue'
import PlayerFilters from './components/PlayerFilters.vue'
import PlayerTable from './components/PlayerTable.vue'
import type { Player } from './types/player'
import jugadoresData from './data/jugadores.json'

const players = ref<Player[]>(jugadoresData as Player[])
const searchQuery = ref('')
const filterEquipo = ref('')
const filterNacionalidad = ref('')
const filterPosicion = ref('')
const filterMinEdad = ref('')
const filterMaxEdad = ref('')
const filterMinMedia = ref('')
const filterMaxMedia = ref('')

function uniqueSorted(values: (string | null)[]): string[] {
  const set = new Set(
    values.map((v) => String(v ?? '').trim()).filter(Boolean)
  )
  return [...set].sort()
}

const equipoOptions = computed(() =>
  uniqueSorted(players.value.map((p) => p.equipoActual))
)
const nacionalidadOptions = computed(() =>
  uniqueSorted(players.value.map((p) => p.nacionalidad))
)
const posicionOptions = computed(() =>
  uniqueSorted(players.value.map((p) => p.posicion))
)

const filteredPlayers = computed(() => {
  let result = players.value

  const q = searchQuery.value.trim().toLowerCase()
  if (q) {
    result = result.filter((p) => {
      const nombre = p.nombre ?? ''
      return String(nombre).toLowerCase().includes(q)
    })
  }

  if (filterEquipo.value) {
    result = result.filter((p) => (p.equipoActual ?? '') === filterEquipo.value)
  }
  if (filterNacionalidad.value) {
    result = result.filter(
      (p) => (p.nacionalidad ?? '') === filterNacionalidad.value
    )
  }
  if (filterPosicion.value) {
    result = result.filter((p) => (p.posicion ?? '') === filterPosicion.value)
  }

  const minEdadStr = String(filterMinEdad.value ?? '').trim()
  if (minEdadStr !== '') {
    const minEdad = Number(minEdadStr)
    if (!Number.isNaN(minEdad)) {
      result = result.filter((p) => (p.edad ?? 0) >= minEdad)
    }
  }
  const maxEdadStr = String(filterMaxEdad.value ?? '').trim()
  if (maxEdadStr !== '') {
    const maxEdad = Number(maxEdadStr)
    if (!Number.isNaN(maxEdad)) {
      result = result.filter((p) => (p.edad ?? 0) <= maxEdad)
    }
  }
  const minMediaStr = String(filterMinMedia.value ?? '').trim()
  if (minMediaStr !== '') {
    const minMedia = Number(minMediaStr)
    if (!Number.isNaN(minMedia)) {
      result = result.filter((p) => (p.mediaJugador ?? 0) >= minMedia)
    }
  }
  const maxMediaStr = String(filterMaxMedia.value ?? '').trim()
  if (maxMediaStr !== '') {
    const maxMedia = Number(maxMediaStr)
    if (!Number.isNaN(maxMedia)) {
      result = result.filter((p) => (p.mediaJugador ?? 0) <= maxMedia)
    }
  }

  return result
})

function resetFilters() {
  searchQuery.value = ''
  filterEquipo.value = ''
  filterNacionalidad.value = ''
  filterPosicion.value = ''
  filterMinEdad.value = ''
  filterMaxEdad.value = ''
  filterMinMedia.value = ''
  filterMaxMedia.value = ''
}
</script>

<template>
  <main class="page">
    <h1>Jugadores</h1>
    <div class="filters-section">
      <PlayerFilters
      v-model:search-query="searchQuery"
      v-model:filter-equipo="filterEquipo"
      v-model:filter-nacionalidad="filterNacionalidad"
      v-model:filter-posicion="filterPosicion"
      v-model:filter-min-edad="filterMinEdad"
      v-model:filter-max-edad="filterMaxEdad"
      v-model:filter-min-media="filterMinMedia"
      v-model:filter-max-media="filterMaxMedia"
      :equipo-options="equipoOptions"
      :nacionalidad-options="nacionalidadOptions"
      :posicion-options="posicionOptions"
      />
      <button type="button" class="reset-btn" @click="resetFilters">
        Reset filters
      </button>
    </div>
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

.filters-section {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.reset-btn {
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text-h);
  cursor: pointer;
}

.reset-btn:hover {
  background: var(--code-bg);
}

.reset-btn:focus {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
</style>
