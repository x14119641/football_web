/**
 * Player data structure matching jugadores.json
 */
export interface Player {
  numero: number
  nombre: string
  equipoActual: string
  nacionalidad: string
  posicion: string
  edad: number
  mediaJugador: number
  valor: number
  precioMercado: number
  [key: string]: unknown // Allow additional fields from JSON
}

/** Columns that can be sorted */
export type SortColumn =
  | 'nombre'
  | 'equipoActual'
  | 'nacionalidad'
  | 'posicion'
  | 'edad'
  | 'mediaJugador'
  | 'valor'
  | 'precioMercado'

export type SortDirection = 'asc' | 'desc'
