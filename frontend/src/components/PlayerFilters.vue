<script setup lang="ts">
defineProps<{
  searchQuery: string
  filterEquipo: string
  filterNacionalidad: string
  filterPosicion: string
  filterMinEdad: string | number
  filterMaxEdad: string | number
  filterMinMedia: string | number
  filterMaxMedia: string | number
  equipoOptions: string[]
  nacionalidadOptions: string[]
  posicionOptions: string[]
}>()

const emit = defineEmits<{
  'update:searchQuery': [value: string]
  'update:filterEquipo': [value: string]
  'update:filterNacionalidad': [value: string]
  'update:filterPosicion': [value: string]
  'update:filterMinEdad': [value: string | number]
  'update:filterMaxEdad': [value: string | number]
  'update:filterMinMedia': [value: string | number]
  'update:filterMaxMedia': [value: string | number]
}>()

function inputValue(e: Event): string {
  return (e.target as HTMLInputElement).value
}
</script>

<template>
  <div class="filters">
    <label class="filter-field">
      <span>Buscar por nombre</span>
      <input
        :value="searchQuery"
        type="search"
        placeholder="Escribir nombre..."
        autocomplete="off"
        @input="emit('update:searchQuery', inputValue($event))"
      />
    </label>
    <label class="filter-field">
      <span>Equipo</span>
      <select
        :value="filterEquipo"
        @change="emit('update:filterEquipo', inputValue($event))"
      >
        <option value="">Todos</option>
        <option v-for="opt in equipoOptions" :key="opt" :value="opt">
          {{ opt }}
        </option>
      </select>
    </label>
    <label class="filter-field">
      <span>Nacionalidad</span>
      <select
        :value="filterNacionalidad"
        @change="emit('update:filterNacionalidad', inputValue($event))"
      >
        <option value="">Todas</option>
        <option v-for="opt in nacionalidadOptions" :key="opt" :value="opt">
          {{ opt }}
        </option>
      </select>
    </label>
    <label class="filter-field">
      <span>Posición</span>
      <select
        :value="filterPosicion"
        @change="emit('update:filterPosicion', inputValue($event))"
      >
        <option value="">Todas</option>
        <option v-for="opt in posicionOptions" :key="opt" :value="opt">
          {{ opt }}
        </option>
      </select>
    </label>
    <label class="filter-field">
      <span>Edad mín</span>
      <input
        :value="filterMinEdad"
        type="number"
        placeholder="—"
        min="0"
        @input="emit('update:filterMinEdad', inputValue($event))"
      />
    </label>
    <label class="filter-field">
      <span>Edad máx</span>
      <input
        :value="filterMaxEdad"
        type="number"
        placeholder="—"
        min="0"
        @input="emit('update:filterMaxEdad', inputValue($event))"
      />
    </label>
    <label class="filter-field">
      <span>Media mín</span>
      <input
        :value="filterMinMedia"
        type="number"
        placeholder="—"
        min="0"
        @input="emit('update:filterMinMedia', inputValue($event))"
      />
    </label>
    <label class="filter-field">
      <span>Media máx</span>
      <input
        :value="filterMaxMedia"
        type="number"
        placeholder="—"
        min="0"
        @input="emit('update:filterMaxMedia', inputValue($event))"
      />
    </label>
  </div>
</template>

<style scoped>
.filters {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem 1.5rem;
  margin-bottom: 1.5rem;
}

@media (max-width: 640px) {
  .filters {
    gap: 0.75rem 1rem;
  }
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
  max-width: 100%;
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .filter-field input,
  .filter-field select {
    min-width: 8rem;
  }
}

.filter-field input[type='search'] {
  max-width: 20rem;
}

@media (max-width: 640px) {
  .filter-field input[type='search'] {
    max-width: 100%;
    min-width: 0;
  }
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
