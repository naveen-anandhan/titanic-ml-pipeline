# 🚢 Titanic Survival Prediction API

End-to-end Machine Learning system that predicts whether a passenger survived the Titanic disaster.

This project demonstrates:

✅ data ingestion  
✅ feature engineering  
✅ model training  
✅ pipeline serialization  
✅ REST API with FastAPI  
✅ Docker containerization  
✅ CI/CD automation  
✅ registry-based deployments  

---

## 🧠 Problem Statement

Given passenger attributes, predict survival outcome.

---

## 🚀 Live Deployment

The service is containerized and automatically deployed.

**API Base URL** : 
https://titanic-api-8g3f.onrender.com


**Swagger UI** : 
https://titanic-api-8g3f.onrender.com/docs


---

## ⚙️ Tech Stack

- Python  
- pandas  
- scikit-learn  
- FastAPI  
- Uvicorn  
- Docker  
- GitHub Actions  
- GitHub Container Registry (GHCR)  
- Cloud deployment  

---

## 🔁 CI/CD Pipeline

Every push to `main` triggers:

```
push → install deps → run tests → build image → push to GHCR → trigger Render deploy
```

No manual steps.

---

## 📦 Container Registry

Images are stored in:

```
ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
```

---

## 🚀 Run Using Docker

```bash
docker pull ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
docker run -p 8000:8000 ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
```

Open in browser:
```
http://localhost:8000/docs
```

---

## 🧪 Example Prediction Request

**POST** `/predict`

```json
{
  "PassengerId": 892,
  "Pclass": 3,
  "Name": "Kelly, Mr. James",
  "Sex": "male",
  "Age": 34.5,
  "SibSp": 0,
  "Parch": 0,
  "Ticket": "330911",
  "Fare": 7.8292,
  "Cabin": null,
  "Embarked": "Q"
}
```

---

## 🧑‍💻 Run Locally (Dev Mode)

```bash
git clone https://github.com/naveen-anandhan/titanic-ml-pipeline.git
cd titanic-ml-pipeline

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app:app --reload
```

---

## 🧪 Testing

CI validates the API before building images.

```bash
PYTHONPATH=. pytest
```

If tests fail → deployment stops.

---

## 🏗️ System Architecture

```
client → FastAPI → load trained model → predict → response
                          ↓
                         logs
                          ↓
                    error handling
```

---

## 📁 Project Structure

```
titanic-ml-pipeline/
│
├── .github/
│   └── workflows/
│       └── cicd.yml
│
├── data/
│   ├── processed/
│   └── raw/
│
├── logs/
│
├── models/
│   ├── model_pipeline.pkl
│   └── .gitkeep
│
├── notebooks/
│   ├── 01.ipynb
│   └── titanic.ipynb
│
├── outputs/
│   ├── submission.csv
│   └── .gitkeep
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── tests/
│   └── test_app.py
│
├── app.py
├── main.py
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🌍 Deployment Philosophy

**Build once → store in registry → deploy anywhere.**

---

## 👤 Author

**Naveen**

