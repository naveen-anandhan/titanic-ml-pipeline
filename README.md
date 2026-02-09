
# 🚢 Titanic Survival Prediction API

End-to-end Machine Learning system that predicts whether a passenger survived the Titanic disaster.

This project demonstrates:

✅ data ingestion  
✅ feature engineering  
✅ model training  
✅ pipeline serialization  
✅ REST API development with FastAPI  
✅ Docker containerization  
✅ production-style deployment mindset  

---

## 🧠 Problem Statement

Given passenger details, predict the survival outcome.

---

## ⚙️ Tech Stack

- Python  
- pandas  
- scikit-learn  
- FastAPI  
- Uvicorn  
- Docker
- Cloud

---

## 🚀 Run Using Docker (Recommended)

No virtual environment.  
No dependency installation.  
No model training.

Just run.

```bash
docker pull naveen8680docker/titanic-api
docker run -p 8000:8000 naveen8680docker/titanic-api
````

Open Swagger UI in Browser:

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

## 🧑‍💻 Run Locally (Development Mode)

```bash
git clone https://github.com/naveen-anandhan/titanic-ml-pipeline.git
cd titanic-ml-pipeline

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

uvicorn api.app:app --reload
```

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
├── data/
│   ├── raw/titanic/
│   └── processed/
│
├── models/
│   └── model_pipeline.pkl
│
├── outputs/
│
├── notebooks/
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🌍 Deployment Ready

The application is packaged as a Docker image and can be deployed to any cloud platform.

**Build once → run anywhere.**

---

## 👤 Author

**Naveen**

```

---
