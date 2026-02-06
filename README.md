
## 📁 Project Structure

```
titanic-ml-pipeline/
│
├── notebooks/
│   └── 01_eda.ipynb          # Exploratory Data Analysis
│
├── data/
│   ├── raw/                 # Original dataset
│   └── processed/           # Cleaned dataset
│
├── src/
│   ├── logger.py            # Logging execution details
│   ├── exception.py         # Custom exception handling
│   ├── utils.py             # Helper utilities
│
│   ├── components/          # Core ML components
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│
│   └── pipeline/            # Training & prediction pipelines
│       ├── train_pipeline.py
│       └── predict_pipeline.py
│
├── models/                  # Saved trained models
├── outputs/                 # Plots and metrics
├── requirements.txt
└── main.py                  # Entry point to run the pipeline
```
