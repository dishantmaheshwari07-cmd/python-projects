# 🌤️ Live CLI Weather Application

### 📝 Project Description
A dynamic Command Line Interface (CLI) weather application that fetches real-time global weather conditions. It seamlessly chains two micro-services: the **Open-Meteo Geocoding API** to pinpoint geographical coordinates, and the **Weather Forecast API** to display current atmospheric metrics based on location.

### 🚀 Key Features
* **🌍 Global City Geocoding:** Automatically resolves city names into exact latitude, longitude, and country configurations.
* **🏢 Smart Feature Filtering:** Efficiently handles location data by mapping advanced geographic feature codes (like cities, capitals, and administrative seats).
* **🌡️ Real-Time Metrics:** Fetches live temperature readings, relative humidity percentages, and precise wind speeds based on automated timezone syncing.
* **🧩 Weather Code Decoding:** Integrates a built-in map decoder to translate raw numeric WMO weather codes into human-readable descriptions (e.g., "Clear Sky", "Overcast").
* **🛡️ Bulletproof Exception Safety:** Wraps dual HTTP requests into layered `try-except` blocks to handle empty search nodes or sudden network downtime without crashing.
* **💻 Dual-Mode Interface:** Supports interactive standard user inputs along with immediate CLI argument parsing (`sys.argv`).

### 🛠️ Tech Stack & Concepts Used
* **Language:** Python 3 (Optimized for mobile compilers like Pydroid 3)
* **Networking:** `requests` module for multi-tier JSON REST API handling.
* **Data Parsing:** JSON schema mapping, dynamic key-value lookups, and conditional execution workflows.
