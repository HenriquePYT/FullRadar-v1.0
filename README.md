<div align="center">
  <img src="assets/logo.png" alt="FullRadar Logo" width="240" />
  <h1>FullRadar v1.0</h1>
  <p>
    <strong>Smart Weather Forecast Application (CLI & Web)</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
    <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License MIT" />
  </p>
</div>

---

## 📖 About the Project

**FullRadar** is a weather forecast application designed to go beyond basic temperature readings. Built from scratch with a robust **343-line Python backend**, it processes real-time meteorological data to deliver **smart health and safety insights**, daily activity recommendations, and persistent favorite cities.

While traditional weather apps (such as Google Forecast) focus primarily on raw numbers, FullRadar interprets the climate for your daily routine—evaluating whether conditions are safe for outdoor running, gym workouts, or if specific precautions are needed against wind, heat stress, or low humidity.

### Development Philosophy & Creator Journey
* **Independent Backend Engineering:** Fully designed, architected, and programmed independently in Python, focusing on clean control flow, robust error handling (`FileNotFoundError`, `JSONDecodeError`), API integration, and local JSON data persistence.
* **Collaborative Frontend Innovation:** Built in partnership with **Claude AI** to bring a modern, animated, and responsive web interface to life. This bridges the gap while I continuously expand my skill set across frontend technologies (HTML, JavaScript, C, C++).
* **Open Source Commitment:** Released publicly on GitHub and LinkedIn, marking the foundation of a project that will continuously evolve through ongoing updates and learning milestones.

---

## ✨ Key Features

### 🧠 Smart Weather Insights & Alerts
FullRadar automatically analyzes incoming data and triggers contextual warnings:
* **Rain Detection:** Immediate precipitation alerts and precaution advisories[cite: 1].
* **Wind Speed Monitoring:** High-wind warnings when speeds exceed **20 km/h**, advising against flat-surface outdoor activities[cite: 1].
* **Heat Stress Index:** Alerts when the apparent temperature exceeds the actual air temperature by **2°C or more**, recommending hydration and shade[cite: 1].
* **Cold & Low Humidity Advisories:** Automatic warnings when temperatures drop below **15°C** or relative humidity falls under **30%**[cite: 1].

### 🏃‍♂️ Daily Activity Recommendations
Using a rule-based evaluation engine, FullRadar advises on daily physical activities[cite: 1]:
* **Outdoor Running:** Evaluates temperature extremes (`> 30°C` or `<= 10°C`), low humidity (`<= 30%`), strong winds (`>= 10 km/h`), and active precipitation[cite: 1].
* **Gym Workouts:** Assesses heat stress, indoor humidity discomfort, and commute rain conditions[cite: 1].

### 🌍 Multi-Language & Unit Flexibility
* **Bilingual Support:** Instant switching between **English (`en`)** and **Portuguese (`pt`)**, with user preferences saved locally[cite: 1].
* **Unit Conversion:** Toggle seamlessly between **Celsius (`°C`)** and **Fahrenheit (`°F`)** without altering underlying safety thresholds[cite: 1].

### ⭐ Persistent Favorites & 7-Day Forecast
* **City Management:** Save, load, view all, and remove favorite cities with automatic local storage (`FullRadar.json` on CLI / `localStorage` on Web)[cite: 1].
* **Extended Outlook:** 7-day forecast featuring daily minimum/maximum temperature ranges, precipitation probabilities, and sunrise/sunset tracking[cite: 1].

---

## 🏗️ Repository Structure

```text
FullRadar/
├── assets/
│   └── logo.png              # FullRadar official brand logo[cite: 2]
├── FullRadar.py              # Core Python backend & interactive CLI application[cite: 1]
├── fullradar.html            # Responsive web interface with dynamic sky canvas[cite: 1]
├── README.md                 # Project documentation[cite: 1]
├── LICENSE                   # MIT License[cite: 1]
└── .gitignore                # Ignores local user JSON databases and Python cache[cite: 1]
