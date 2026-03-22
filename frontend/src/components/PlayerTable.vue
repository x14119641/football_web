<script setup lang="ts">
import type { Player } from '../types/player'

defineProps<{
  players: Player[]
}>()

const columns: { key: keyof Player; label: string; format?: 'number' }[] = [
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
          <th v-for="col in columns" :key="col.key">
            {{ col.label }}
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
}

.player-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.player-table th,
.player-table td {
  padding: 0.6rem 1rem;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

.player-table th {
  font-weight: 600;
  background: var(--code-bg);
  color: var(--text);
}

.player-table tbody tr:hover {
  background: var(--code-bg);
}

.player-table td:nth-child(n + 7) {
  text-align: right;
  font-variant-numeric: tabular-nums;
}
</style>
