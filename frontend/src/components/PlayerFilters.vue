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
    
    <!-- Row 1 -->
    <div class="filters-row">
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
    </div>

    <!-- Row 2 -->
    <div class="filters-row">
      <div class="filter-field">
        <span>Edad</span>
        <div class="range">
          <input
            :value="filterMinEdad"
            type="number"
            placeholder="Min"
            min="0"
            @input="emit('update:filterMinEdad', inputValue($event))"
          />
          <input
            :value="filterMaxEdad"
            type="number"
            placeholder="Max"
            min="0"
            @input="emit('update:filterMaxEdad', inputValue($event))"
          />
        </div>
      </div>

      <div class="filter-field">
        <span>Media</span>
        <div class="range">
          <input
            :value="filterMinMedia"
            type="number"
            placeholder="Min"
            min="0"
            @input="emit('update:filterMinMedia', inputValue($event))"
          />
          <input
            :value="filterMaxMedia"
            type="number"
            placeholder="Max"
            min="0"
            @input="emit('update:filterMaxMedia', inputValue($event))"
          />
        </div>
      </div>

      <!-- Spacer pushes reset right -->
      <div class="spacer"></div>

      <div class="reset-wrapper">
        <slot name="reset"></slot>
      </div>
    </div>

  </div>
</template>

<style scoped>
.filters {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.filters-row {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  align-items: flex-end;
}

.spacer {
  flex: 1;
}

.reset-wrapper {
  display: flex;
  align-items: flex-end;
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
  flex: 0 1 auto;
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
  min-width: 0;
  width: 160px;
  box-sizing: border-box;
}

@media (max-width: 640px) {
  .filter-field input,
  .filter-field select {
    min-width: 8rem;
  }
}

.filter-field input[type='search'] {
  width: 240px;
  max-width: 20rem;
}

@media (max-width: 640px) {
  .filter-field input[type='search'] {
    max-width: 100%;
    min-width: 0;
  }
}

.filter-field input[type='number'] {
  width: 70px;
  max-width: 6rem;
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

.range {
  display: flex;
  gap: 0.5rem;
}

.range input {
  width: 70px;
  text-align: center;
}
</style>
