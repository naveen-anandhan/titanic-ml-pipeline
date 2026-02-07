
## 📁 Project Structure

```
client → FastAPI (cloud server) → load model from S3 → predict → response
                                        ↓
                                      logs
                                        ↓
                                   error handling

```

```
titanic-ml-pipeline/
│
├── data/
│   ├── raw/
│   │   └── titanic/
│   │       ├── train.csv
│   │       └── test.csv
│   │
│   └── processed/
│       └── .gitkeep
│
├── models/
│   ├── model_pipeline.pkl
│   └── .gitkeep
│
├── outputs/
│   ├── submission.csv
│   └── .gitkeep
│
├── notebooks/
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── venv/                # ignored in git
├── main.py              # entry point
├── requirements.txt
└── README.md
```



