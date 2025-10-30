# 🚦 Obstruction Detection System  

A full-stack application that detects and classifies potential **obstructions** using simulated multi-sensor data.  
This project combines **Machine Learning**, **Flask**, and a **React + TailwindCSS** frontend to deliver real-time obstruction detection for autonomous systems and safety monitoring.

---

## 🧠 Overview  

The system processes readings from multiple sensors (distance, LiDAR, camera, IR, sonar) and uses trained **KNN** and **Naive Bayes** models to determine whether an obstruction is present.  
It is designed to simulate an intelligent obstacle-detection pipeline suitable for self-driving vehicles, robotics, or IoT applications.

---

## 🚀 Features  

- 🧩 Multi-sensor data analysis (Distance, LiDAR, Camera, IR, Sonar)  
- 🧠 Machine Learning inference using **KNN** and **GaussianNB**  
- ⚙️ Backend built with **Flask + scikit-learn**  
- 💻 Frontend built with **React + Vite + TailwindCSS**  
- 🔄 Real-time predictions via REST API  
- 🧰 Modular structure — separate backend and frontend folders  

---

## 🏗️ Tech Stack  

| Layer | Technologies |
|-------|---------------|
| **Backend** | Python, Flask, scikit-learn, NumPy, Pandas |
| **Frontend** | React, Vite, TailwindCSS, Axios |
| **ML Models** | K-Nearest Neighbors, Gaussian Naive Bayes |
| **Data Simulation** | Synthetic sensor data generator for testing |

---

## 📁 Folder Structure  

```
📁 Obstruction-Detection-System/
│
├── 📂 backend/
│   ├── 📄 app.py
│   ├── 📂 routes/
│   │   └── detection.py
│   ├── 📂 model/
│   │   ├── knn.pkl
│   │   └── nb.pkl
│   ├── 📂 processed/
│   │   ├── scaler.pkl
│   │   └── sample_dataset.csv
│   ├── 📂 utils/
│   │   └── sensors.py
│   ├── 📄 requirements.txt
│   └── 📄 README.md
│
└── 📂 frontend/
    ├── 📂 public/
    │   └── index.html
    ├── 📂 src/
    │   ├── App.jsx
    │   ├── main.jsx
    │   ├── 📂 api/
    │   │   └── detectionAPI.js
    │   ├── 📂 components/
    │   │   ├── SensorInput.jsx
    │   │   └── ResultCard.jsx
    │   └── 📂 pages/
    │       └── Home.jsx
    ├── 📄 package.json
    ├── 📄 tailwind.config.js
    ├── 📄 vite.config.js
    └── 📄 README.md
```


---

## ⚙️ Setup & Run  

### 🧩 Backend Setup  

```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
The backend will start on http://localhost:5000

💻 Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available on http://localhost:5173

🔬 How It Works
 1.Data Simulation: Synthetic sensor data is generated to simulate distance, IR temperature difference, and other readings.
 2. Model Training: The backend includes pre-trained KNN and Naive Bayes models that classify each sample as either “Clear” or “Obstruction Detected”.
 3. Prediction API: The frontend sends sensor readings to the Flask API at /api/predict.
 4. Real-Time Detection: The backend returns a prediction and confidence probability, which is displayed instantly in the web interface.

📈 Example Input / Output

Input:
```json
{
  "distance_cm": 48.7,
  "lidar_intensity": 0.52,
  "camera_confidence": 0.74,
  "ir_temp_diff": 1.6,
  "sonar_echo": 0.42
}
```
Output:
```json
{
  "prediction": "OBSTRUCTION DETECTED",
  "probability": 0.87
}
```

🎯 Future Improvements
 1. Integrate real-world sensor data from Raspberry Pi or microcontrollers
 2. Add time-series models (LSTM) for temporal pattern detection
 3. Deploy backend to Render / AWS / Railway
 4. Add real-time graphs in the frontend using Chart.js or Recharts
 5. Implement a dashboard for analytics and system health monitoring.
