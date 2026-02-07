import pandas as pd
import pickle
from src.components.data_transformation import DataTransformation
import os
import sys

from src.logger import logger
from src.exception import CustomException

class PredictPipeline:

    def predict(self, model, test_df):
        try:
            logger.info("Prediction pipeline started")

            # load test data
            test_path = os.path.join("data", "raw", "titanic", "test.csv")
            test_df = pd.read_csv(test_path)

            passenger_ids = test_df["PassengerId"]

            transformer = DataTransformation()
            test_df = transformer.create_features(test_df)

            with open("models/model_pipeline.pkl", "rb") as f:
                model = pickle.load(f)

            preds = model.predict(test_df)

            submission = pd.DataFrame({
                "PassengerId": passenger_ids,
                "Survived": preds.astype(int)
            })

            submission.to_csv("outputs/submission.csv", index=False)

            logger.info("Prediction pipeline completed")
            print("✅ Submission file created at outputs/submission.csv")

        except Exception as e:
            logger.error("Error in prediction pipeline")
            raise CustomException(e, sys)
