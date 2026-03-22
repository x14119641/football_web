<script setup lang="ts">
import { ref } from 'vue'
import PlayerTable from './components/PlayerTable.vue'
import type { Player } from './types/player'
import jugadoresData from './data/jugadores.json'

const players = ref<Player[]>(jugadoresData as Player[])
</script>

<template>
  <main class="page">
    <h1>Jugadores</h1>
    <PlayerTable :players="players" />
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

</style>
