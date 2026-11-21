FullRadar v1.0

FullRadar is a weather forecast application featuring a Python backend built from scratch, offering smart weather warnings, city favorites, and multi-language support. It focuses on providing useful insights that traditional weather applications don't prioritize.

 Features

- Smart Weather Insights: Automated warnings for rain, high wind speeds, heat stress, low temperatures, and low humidity.
- Activity Recommendations: Tailored advice on whether it's safe to run or go to the gym based on current meteorological conditions.
- Favorite Cities: Save, load, and manage your favorite locations easily with local JSON persistence.
- Multi-Language Support: Seamlessly switch between English (`en`) and Portuguese (`pt`).
- Flexible Units: View forecasts in Celsius (°C) or Fahrenheit (°F).
- 7-Day Forecast: Detailed daily breakdown including maximum/minimum temperatures, precipitation probability, sunrise, and sunset times.

 Built With

- Python (Backend logic, data persistence, and CLI architecture)
- Open-Meteo API (Free weather and geocoding data)
- Claude AI (Frontend web UI collaboration)

 Project Structure

- FullRadar.py - Main application script containing core logic, menu navigation, and API requests.
- FullRadar.json - Local storage file for saved favorite cities (ignored by git).
- FullRadarSettings.json - Local storage file for user language preferences (ignored by git).

 Getting Started (CLI)

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/FullRadar.git](https://github.com/YOUR_USERNAME/FullRadar.git)
