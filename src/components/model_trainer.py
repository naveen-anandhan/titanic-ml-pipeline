from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from src.utils import save_object

import sys
from src.logger import logger
from src.exception import CustomException


class ModelTrainer:
    def train(self, X, y, preprocessor):
        try:
            logger.info("Model training started")

            model = RandomForestClassifier(
                n_estimators=800,
                max_depth=7,
                random_state=42
            )

            pipe = Pipeline([
                ('prep', preprocessor),
                ('model', model)
            ])

            pipe.fit(X, y)

            logger.info("Model training completed")

            # save trained pipeline
            save_object("models/model_pipeline.pkl", pipe)
            logger.info("Model saved successfully")

            return pipe

        except Exception as e:
            logger.error("Error during model training")
            raise CustomException(e, sys)
