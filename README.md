# 🧠 Motivation API – *„Motivationskick“*

Eine einfache, KI-freie **FastAPI-basierte REST-API**, die motivierende Sprüche je nach Stimmung ausgibt.  
Ideal als Demo-Projekt für API-Deployment mit **FastAPI**, **Uvicorn** und **Render**.

---

## 🚀 Live-Version  

👉 **[https://motivationskick.onrender.com/docs](https://motivationskick.onrender.com/docs)**  
(Dort kannst du die API direkt im Browser ausprobieren)

---

## 📋 Funktionsbeschreibung  

Die API liefert einen zufälligen Motivationsspruch basierend auf der gewählten Stimmung.  

Unterstützte Stimmungen:
- 💤 **müde**
- 😣 **gestresst**
- 💪 **fit**

**Beispiel-Request:**
```bash
GET https://motivationskick.onrender.com/motivation?stimmung=fit
```

**Beispiel-Antwort:**
```json
{
  "stimmung": "fit",
  "spruch": "Nutze deine Energie – heute setzt du ein Statement!"
}
```

---

## ⚙️ Lokale Installation

### 1️⃣ Projekt klonen
```bash
git clone https://github.com/armorajdini/AI_Ops_Project.git
cd AI_Ops_Project
```

### 2️⃣ Virtuelle Umgebung erstellen
```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
```

### 3️⃣ Abhängigkeiten installieren
```bash
pip install -r requirements.txt
```

### 4️⃣ Server starten
```bash
uvicorn Code.main:app --reload
```

### 5️⃣ Swagger UI öffnen
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧩 Beispiel in Python

```python
import requests

url = "https://motivationskick.onrender.com/motivation"
params = {"stimmung": "müde"}

resp = requests.get(url, params=params)
data = resp.json()

print(f"Stimmung: {data['stimmung']}")
print(f"Motivationsspruch: {data['spruch']}")
```

---

## 🛠 Technologien

| Komponente | Beschreibung |
|-------------|---------------|
| **FastAPI** | Framework für moderne Web-APIs |
| **Uvicorn** | ASGI-Server zum Hosten der API |
| **Render**  | Cloud-Plattform zum Deployment |
| **Python 3.12+** | Programmiersprache |

---

## 🧾 API-Übersicht

| Route | Methode | Beschreibung |
|-------|----------|---------------|
| `/motivation` | GET | Gibt einen zufälligen Spruch zur gewählten Stimmung |
| `/docs` | GET | Swagger UI zum Testen der API |
| `/` | GET | Leitet automatisch zur Swagger UI weiter |

---

## 🌍 Deployment (Render)

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
uvicorn Code.main:app --host 0.0.0.0 --port $PORT
```

---

## 🧑‍💻 Autor

**Armor Ajdini**  
Business Artificial Intelligence Student (FHNW, Schweiz)  
📍 Projekt: *AI Ops Project*  

---

## 💡 Ideen für Erweiterungen

- POST-Requests für eigene Sprüche  
- Datenbank-Anbindung (z. B. SQLite oder PostgreSQL)  
- KI-Integration für dynamische Motivationssätze  
- Frontend-Interface (React, Streamlit oder Shiny)

---
