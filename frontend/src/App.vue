<script setup lang="ts">
import { ref, computed } from 'vue'
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
</script>

<template>
  <main class="page">
    <h1>Jugadores</h1>
    <div class="filters">
      <label class="filter-field">
        <span>Buscar por nombre</span>
        <input
          v-model="searchQuery"
          type="search"
          placeholder="Escribir nombre..."
          autocomplete="off"
        />
      </label>
      <label class="filter-field">
        <span>Equipo</span>
        <select v-model="filterEquipo">
          <option value="">Todos</option>
          <option v-for="opt in equipoOptions" :key="opt" :value="opt">
            {{ opt }}
          </option>
        </select>
      </label>
      <label class="filter-field">
        <span>Nacionalidad</span>
        <select v-model="filterNacionalidad">
          <option value="">Todos</option>
          <option v-for="opt in nacionalidadOptions" :key="opt" :value="opt">
            {{ opt }}
          </option>
        </select>
      </label>
      <label class="filter-field">
        <span>Posición</span>
        <select v-model="filterPosicion">
          <option value="">Todos</option>
          <option v-for="opt in posicionOptions" :key="opt" :value="opt">
            {{ opt }}
          </option>
        </select>
      </label>
      <label class="filter-field">
        <span>Edad mín</span>
        <input v-model="filterMinEdad" type="number" placeholder="—" min="0" />
      </label>
      <label class="filter-field">
        <span>Edad máx</span>
        <input v-model="filterMaxEdad" type="number" placeholder="—" min="0" />
      </label>
      <label class="filter-field">
        <span>Media mín</span>
        <input v-model="filterMinMedia" type="number" placeholder="—" min="0" />
      </label>
      <label class="filter-field">
        <span>Media máx</span>
        <input v-model="filterMaxMedia" type="number" placeholder="—" min="0" />
      </label>
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

.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 1.5rem;
  margin-bottom: 1.5rem;
}

.filter-field {
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.filter-field span {
  font-size: 0.85rem;
  color: var(--text);
}

.filter-field input,
.filter-field select {
  padding: 0.5rem 0.75rem;
  font-size: 1rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg);
  color: var(--text-h);
  min-width: 10rem;
}

.filter-field input[type='search'] {
  max-width: 20rem;
}

.filter-field input[type='number'] {
  width: 5rem;
  min-width: 5rem;
}

.filter-field input:focus,
.filter-field select:focus {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

.filter-field input::placeholder {
  color: var(--text);
  opacity: 0.7;
}

</style>
