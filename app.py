from fastapi import FastAPI, UploadFile, File, APIRouter
import pandas as pd
import pickle
import sys
import io
import os

from src.components.data_transformation import DataTransformation
from src.logger import logger
from src.exception import CustomException
from src.llm_service import llm_service
from fastapi.responses import StreamingResponse

import traceback

app = FastAPI()

@app.get("/test-llm-error")
def test_llm_error():
    try:
        1 / 0  # force error
    except Exception:
        error_text = traceback.format_exc()
        explanation = llm_service.explain_error(error_text)
        return {"llm_response": explanation}

# ---- read version from file ----
def get_version():
    try:
        with open("VERSION", "r") as f:
            return f.read().strip()
    except:
        return "dev"


# ---- load model ----
try:
    with open("models/model_pipeline.pkl", "rb") as f:
        model = pickle.load(f)

    transformer = DataTransformation()

    logger.info("Model and transformer loaded successfully")
    logger.info(f"VERSION FILE VALUE = {get_version()}")

except Exception as e:
    logger.exception("Error loading model")
    raise CustomException(e, sys)


@app.get("/")
def home():
    return {"message": "Titanic API running"}


# ---- version endpoint ----
@app.get("/version")
def version():
    return {"version": get_version()}


@app.post("/predict")
def predict(data: dict):
    try:
        logger.info("Prediction request received")

        df = pd.DataFrame([data])
        df = transformer.create_features(df)

        pred = model.predict(df)[0]

        logger.info("Prediction successful")

        return {"prediction": int(pred)}

    except Exception as e:
        logger.exception("Error during prediction")
        raise CustomException(e, sys)


@app.post("/predict_file")
def predict_file(file: UploadFile = File(...)):
    try:
        logger.info("Batch prediction request received")

        contents = file.file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        df = transformer.create_features(df)
        preds = model.predict(df)
        df["prediction"] = preds.astype(int)

        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)

        logger.info("Batch prediction successful")

        return StreamingResponse(
            iter([output.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=predictions.csv"}
        )

    except Exception as e:
        logger.exception("Error in batch prediction")
        raise CustomException(e, sys)
