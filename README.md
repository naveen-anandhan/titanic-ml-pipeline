# 🚢 Titanic Survival Prediction API

An end-to-end Production-Ready Machine Learning System that predicts whether a passenger survived the Titanic disaster.

This project demonstrates a real-world ML deployment pipeline including model training, API serving, containerization, release-based CI/CD, cloud deployment, and LLM-assisted error analysis.

---

## ✨ What This Project Demonstrates

* ✅ Data ingestion & preprocessing
* ✅ Feature engineering pipeline
* ✅ Model training & serialization
* ✅ Production inference pipeline
* ✅ FastAPI REST API
* ✅ Structured logging & custom exception handling
* ✅ 🤖 LLM-powered error analysis & fix suggestion
* ✅ Docker containerization
* ✅ Release-driven CI/CD automation
* ✅ GitHub Container Registry (GHCR)
* ✅ Cloud deployment on Render
* ✅ Version traceability

---

## 🧠 Problem Statement

Given passenger attributes such as class, age, gender, fare, and embarkation port, predict whether the passenger survived the Titanic disaster.

---

# 🚀 Live Deployment

The service is deployed via **release-based CI/CD** using Docker images stored in GHCR.

### 🔗 API Base URL
https://titanic-api-8g3f.onrender.com

### 📘 Swagger UI

https://titanic-api-8g3f.onrender.com/docs


### 🧾 Version Endpoint

```
GET /version
```

This ensures full traceability of the running production version.

---

# ⚙️ Tech Stack

* Python
* pandas
* scikit-learn
* FastAPI
* Uvicorn
* Docker
* GitHub Actions
* GitHub Container Registry (GHCR)
* Render (Cloud Hosting)

---

# 🔒 Release & Deployment Strategy (Important)

This project follows a **Release-Driven Deployment Model**.

```
Push / Merge  → NO DEPLOY ❌  
Create Release → BUILD → DEPLOY 🚀
```

## 🛠 Deployment Workflow

1. Developers push or merge changes into `main`.
2. Production is NOT updated automatically.
3. When verified → a GitHub Release is created.
4. Release triggers CI/CD.
5. Tests are executed.
6. Docker image is built using release version.
7. Image is pushed to GHCR.
8. Render pulls the new image and deploys.

---

## 🧠 Why This Approach?

* ✅ Prevents accidental production deployments.
* ✅ Every production version is traceable.
* ✅ Enables easy rollback.
* ✅ Guarantees reproducible builds.
* ✅ Follows real-world MLOps standards.

---

# 🔁 CI/CD Pipeline

Triggered on **Release Publish**:

```
release 
   → install dependencies 
   → run tests 
   → generate VERSION file 
   → build Docker image 
   → push to GHCR 
   → trigger Render deploy
```

If tests fail → deployment is blocked automatically.

---

# 📦 Container Registry

Images are stored at:

```
ghcr.io/naveen-anandhan/titanic-ml-pipeline:<version>
ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
```

Each release creates an immutable, versioned container image.

---

# 🏷 Versioning Policy

This project follows **Semantic Versioning (SemVer)**:

```
MAJOR.MINOR.PATCH
```

Example:

* `v1.2.0` → New feature
* `v1.2.1` → Bug fix
* `v2.0.0` → Breaking change

⚠️ Released versions are immutable.
Bug fixes require a new patch version.

---

# 🐳 Run Using Docker

```bash
docker pull ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
docker run -p 8000:8000 ghcr.io/naveen-anandhan/titanic-ml-pipeline:latest
```

Access locally:

```
http://localhost:8000/docs
```

---

# 🧪 Example Prediction Request

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

# 🧑‍💻 Run Locally (Development Mode)

```bash
git clone https://github.com/naveen-anandhan/titanic-ml-pipeline.git
cd titanic-ml-pipeline

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn app:app --reload
```

---

# 🧪 Run Tests

```bash
PYTHONPATH=. pytest
```

If tests fail → CI blocks image build.

---

# 🏗️ System Architecture

```
Client / User
      │
      ▼
FastAPI Application
      │
      ├── SUCCESS FLOW
      │      → Load Serialized ML Pipeline
      │      → Generate Prediction
      │      → Return API Response
      │
      └── ERROR FLOW
             → Exception Raised
             → Exception Captured (Custom Handler)
             → Structured Logging
             → Send Error Context to LLM Service
             → LLM Generates Suggested Fix
             → Suggested Fix Logged
```

---

# 📁 Project Structure

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

# 🌍 Deployment Philosophy

> **Build once → Store in registry → Deploy anywhere**

Each production version corresponds to an immutable Docker image.

---

# 👤 Author

**Naveen**

---
