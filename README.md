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

The service is containerized and deployed via release-based CI/CD.

**API Base URL**  
https://titanic-api-8g3f.onrender.com

**Swagger UI**  
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
- Render (Cloud)

---

## 🔒 Release & Deployment Rule (Very Important)

This repository follows **release-driven deployment**.

```
Push / Merge  → NO DEPLOY ❌  
Create Release → BUILD → DEPLOY 🚀
```

### Workflow

1. Developers can push or merge changes into `main`.
2. Production is **not** updated automatically.
3. When changes are verified → we create a **GitHub Release**.
4. Release triggers CI/CD.
5. Docker image is built with the release version.
6. Image is pushed to GHCR.
7. Render pulls the new image and deploys.

---

### Why this approach?

✅ prevents accidental deployments  
✅ every production version is traceable  
✅ easy rollback  
✅ reproducible builds  
✅ mirrors real industry systems  

---

### Reminder for future me 🧠

👉 Want new code in production?  
➡ create a **new release**.

---

## 🔁 CI/CD Pipeline

On release publish:

```
release → install deps → run tests → create VERSION file → 
build image → push to GHCR → trigger Render deploy
```

If tests fail → deployment stops.

---

## 📦 Container Registry

Images are stored in:

```
ghcr.io/naveen-anandhan/titanic-ml-pipeline:<version>
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

```bash
PYTHONPATH=. pytest
```

If tests fail → CI blocks image build.

---

## 🧾 Versioning

The application reads its version from a file generated during CI.

Endpoint:
```
GET /version
```

This guarantees we always know **exactly** which release is running.

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
│
├── outputs/
│
├── src/
│   ├── components/
│   ├── pipeline/
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
