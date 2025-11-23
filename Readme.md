🌫️ Air Quality Monitoring System with ESP32 + Edge ML

A real-time smart air quality monitoring system using ESP32, MQ-135 gas sensor, and DHT11 (temperature/humidity), integrated with an on-device machine-learning classifier and a beautiful live web dashboard.

This project collects sensor data, classifies air quality using a trained ML model, logs data for continuous learning, and displays live readings over WiFi on any browser.

🚀 Features

✔ Real-time Air Quality Monitoring
✔ Edge Machine Learning on ESP32 (no cloud required)
✔ Web Dashboard accessible from browser
✔ Live updating graph (MQ135 trend)
✔ WiFi connectivity for UI
✔ Local data logging Python script
✔ Retraining pipeline via Jupyter Notebook
✔ Modular firmware architecture
✔ Easily expandable with more sensors
✔ Sensor-fusion ready
```
🧠 System Architecture
MQ-135   ┐
         ├─→ ESP32 → ML model → Classification → Dashboard
DHT11    ┘                │
                           └→ Serial Output → Python Logger → CSV
                                          │
                                          └→ Retraining → deploy new model
```
🛠 Hardware Used

ESP32 Dev Module

MQ-135 Gas Sensor

DHT11 Temperature/Humidity Sensor

USB data cable

Jumper wires

Breadboard

🔌 Wiring Connections
MQ135
```
VCC  → 3.3V  
GND  → GND  
AOUT → GPIO 34 (ADC input)
```

DHT11 (3-pin module recommended)
```
VCC  → 3.3V  
DATA → GPIO 4  
GND  → GND  
```

🧩 Software Components
Firmware (C++ / Arduino)

AirQualityFirmware.ino

sensors.cpp — reads sensors

classifier.cpp — ML decision logic

wifi_comm.cpp — hosts web dashboard

/data/index.html — UI

Python

log_data.py — logs COM port output to CSV

Machine Learning

training_notebook.ipynb

trains model from:

online datasets

logged sensor data

exports rules as C++ logic for ESP32

📊 Web Dashboard

Accessible at:
```
http://<ESP32-IP>
```

Displays:

Air Quality status with colored indicator

MQ135 gas reading

Temperature (°C)

Humidity (%)

Live line graph of gas readings over time

No internet required — local intranet only.

🧪 Training the ML Model

Collect real sensor data using:
```
python log_data.py
```

Run notebook:
```
training_notebook.ipynb
```

ML model retrains based on:
```
master_log.csv (local real data)
indoor_data.csv (reference dataset)
```

Export model as decision tree

Insert into classifier.cpp

Upload firmware to ESP32

📂 Project Structure
```
AirQualityMonitoringSystem/
│
├── firmware/
│   ├── AirQualityFirmware.ino
│   ├── sensors.cpp
│   ├── classifier.cpp
│   ├── wifi_comm.cpp
│   ├── config.h
│   └── data/
│       ├── index.html
│       ├── style.css
│       └── script.js
│
├── ML_model/
│   ├── training_notebook.ipynb
│   ├── model_exported_rules.txt
│
├── dataset/
│   ├── indoor_data.csv
│   ├── master_log.csv (ignored in .gitignore)
│
├── log_data.py
└── README.md
```
🧠 Machine Learning Concept

Using Decision Tree Classifier:

Predicts AQI label from:

MQ135 raw (gas sensor)

Temperature

Humidity

Example output:
```
Good
Moderate
Unhealthy
```

🏁 Getting Started
1. Flash ESP32 with firmware
2. Open Serial Monitor — check IP
3. Open browser:
```
http://<ESP-IP>
```

4. View live dashboard
5. Optionally log data with:
```
python log_data.py
```

🧩 Future Improvements

Add dust sensor (GP2Y1010)

Add CO sensor (MQ-7)

Add PM2.5 / PM10

Weather API integration

WiFi hotspot mode

Cloud sync + alerts

ESP32 BLE → phone app
