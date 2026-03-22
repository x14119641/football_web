# Liguilla Web
Aplicación web desarrollada con Vue 3 para visualizar, filtrar y explorar jugadores a partir de los datos importados desde Excel y convertidos a JSON


## Objetivo
Permitir al usuario explorar y analizar jugadores de forma rápida mediante:
- Búsqueda por nombre
- Filtros por equipo, nacionalidad y posicion
- Filtros por rangos (edad y media)
- Ordenación por columnas
- Visualización clara en tabla
 

## Data Flow
1. Se parte de un Excel "master" original 
2. Se limpia manualmente (columnas innecesarias, nombres)
3. Un script Python convierte el Excel a JSON
4. El frontend (Vue) carga el JSON y aplica:
   - Filtros
   - Ordenación
   - Renderizado en tabla
  
## Stack
- Vue 3
- Vite
- Typescript
- Python (pandas para conversión de Excel a JSON)


## Ejecutar localmente
```bash
npm install
npm run dev
```

## Funcionalidades actuales
- Tabla de jugadores
- Búsqueda por texto (nombre)
- Filtros por múltiples campos
- Filtros por rango (edad y media)
- Ordenación por columnas
- Reset de filtros
- Contador de resultados


## Decisiones de diseño
- Se utiliza JSON en lugar de Excel en el frontend para simplificar el parsing
- El procesamiento de datos se separa del frontend
- No se utiliza backend para mantener la aplicación simple y fácilmente desplegable.
- Se evita la paginación para priorizar la exploración continua de datos.


## Mejoras futuras
- Filtros más avanzados
- Integración con APIs externas (ej.: Sofifa) para ampliar información de jugadores.