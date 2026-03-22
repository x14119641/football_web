# Development Notes

## Data processing
- Excel data is converted to JSON using python script with pandas
- Column names are manually mapped to camelCase for consistency across the frontend
- Numeric values are cleaned and normalized (e.g removing commas and converting to proper number types)


# Frontend
- Vue 3 + Vite
- Data is loaded from static JSON file
- Filtering is done client-side for simplicity and performance

Decisions
- Chose JSON instead of parsing Excel directly in the frontend to simplify data handling
- Separated data processing from frontend logic to improve maintanability
- Avoided using backend to keep the project simple and compatible with free static hosting services

