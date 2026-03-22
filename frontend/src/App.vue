<script setup lang="ts">
import { ref, computed } from 'vue'
import PlayerFilters from './components/PlayerFilters.vue'
import PlayerTable from './components/PlayerTable.vue'
import type { Player, SortColumn, SortDirection } from './types/player'
import jugadoresData from './data/jugadores.json'

// Data
const players = ref<Player[]>(jugadoresData as Player[])

// Filter state
const searchQuery = ref('')
const filterEquipo = ref('')
const filterNacionalidad = ref('')
const filterPosicion = ref('')
const filterMinEdad = ref('')
const filterMaxEdad = ref('')
const filterMinMedia = ref('')
const filterMaxMedia = ref('')

// Sort state
const sortColumn = ref<SortColumn | null>(null)
const sortDirection = ref<SortDirection>('asc')

function uniqueSorted(values: (string | null)[]): string[] {
  const set = new Set(
    values.map((v) => String(v ?? '').trim()).filter(Boolean)
  )
  return [...set].sort()
}

function parseOptionalNumber(value: string | number): number | null {
  const str = String(value ?? '').trim()
  if (str === '') return null
  const num = Number(str)
  return Number.isNaN(num) ? null : num
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

  const searchTerm = searchQuery.value.trim().toLowerCase()
  if (searchTerm) {
    result = result.filter((p) => {
      const nombre = p.nombre ?? ''
      return String(nombre).toLowerCase().includes(searchTerm)
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

  const minEdad = parseOptionalNumber(filterMinEdad.value)
  if (minEdad != null) {
    result = result.filter((p) => (p.edad ?? 0) >= minEdad)
  }
  const maxEdad = parseOptionalNumber(filterMaxEdad.value)
  if (maxEdad != null) {
    result = result.filter((p) => (p.edad ?? 0) <= maxEdad)
  }
  const minMedia = parseOptionalNumber(filterMinMedia.value)
  if (minMedia != null) {
    result = result.filter((p) => (p.mediaJugador ?? 0) >= minMedia)
  }
  const maxMedia = parseOptionalNumber(filterMaxMedia.value)
  if (maxMedia != null) {
    result = result.filter((p) => (p.mediaJugador ?? 0) <= maxMedia)
  }

  return result
})

const sortedPlayers = computed(() => {
  const list = [...filteredPlayers.value]
  const column = sortColumn.value
  const direction = sortDirection.value
  if (!column) return list

  return list.sort((a, b) => {
    const aVal = a[column]
    const bVal = b[column]
    const isNumeric =
      typeof aVal === 'number' || typeof bVal === 'number'

    if (isNumeric) {
      const numA = Number(aVal ?? 0)
      const numB = Number(bVal ?? 0)
      return direction === 'asc' ? numA - numB : numB - numA
    }

    const strA = String(aVal ?? '')
    const strB = String(bVal ?? '')
    const cmp = strA.localeCompare(strB, 'es')
    return direction === 'asc' ? cmp : -cmp
  })
})

function handleSort(column: SortColumn) {
  if (sortColumn.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortColumn.value = column
    sortDirection.value = 'asc'
  }
}

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
    <PlayerTable
      :players="sortedPlayers"
      :sort-column="sortColumn"
      :sort-direction="sortDirection"
      @sort="handleSort"
    />
  </main>
</template>

<style scoped>
.page {
  padding: 2rem;
  text-align: left;
  max-width: 100%;
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .page {
    padding: 1rem;
  }
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
