<script setup lang="ts">
import type { Player, SortColumn, SortDirection } from '../types/player'

defineProps<{
  players: Player[]
  sortColumn: SortColumn | null
  sortDirection: SortDirection
}>()

const emit = defineEmits<{
  sort: [column: SortColumn]
}>()

const columns: { key: SortColumn; label: string; format?: 'number' }[] = [
  { key: 'nombre', label: 'Nombre' },
  { key: 'equipoActual', label: 'Equipo' },
  { key: 'nacionalidad', label: 'Nacionalidad' },
  { key: 'posicion', label: 'Posición' },
  { key: 'edad', label: 'Edad' },
  { key: 'mediaJugador', label: 'Media' },
  { key: 'valor', label: 'Valor', format: 'number' },
  { key: 'precioMercado', label: 'Precio mercado', format: 'number' },
]

function formatValue(value: unknown, format?: string): string {
  if (value == null) return '—'
  if (format === 'number' && typeof value === 'number') {
    return value.toLocaleString('es-ES')
  }
  return String(value)
}
</script>

<template>
  <div class="table-wrapper">
    <table class="player-table">
      <thead>
        <tr>
          <th
            v-for="col in columns"
            :key="col.key"
            class="sortable"
            :class="{ active: sortColumn === col.key }"
            @click="emit('sort', col.key)"
          >
            <span class="th-content">
              {{ col.label }}
              <span v-if="sortColumn === col.key" class="sort-icon">
                {{ sortDirection === 'asc' ? '↑' : '↓' }}
              </span>
            </span>
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="player in players" :key="player.numero">
          <td v-for="col in columns" :key="col.key">
            {{ formatValue(player[col.key], col.format) }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.table-wrapper {
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  max-width: 100%;
}

.player-table {
  width: 100%;
  min-width: 600px;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.player-table th,
.player-table td {
  padding: 0.6rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

@media (max-width: 640px) {
  .player-table th,
  .player-table td {
    padding: 0.5rem 0.75rem;
    font-size: 0.85rem;
  }
}

.player-table th {
  font-weight: 600;
  background: var(--code-bg);
  color: var(--text);
}

.player-table th.sortable {
  cursor: pointer;
  user-select: none;
}

.player-table th.sortable:hover {
  background: var(--border);
}

.player-table th .th-content {
  white-space: nowrap;
}

.player-table th.sortable .sort-icon {
  margin-left: 0.25rem;
  color: var(--accent);
}

.player-table tbody tr:hover {
  background: var(--code-bg);
}

.player-table td:nth-child(n + 7) {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
</style>
