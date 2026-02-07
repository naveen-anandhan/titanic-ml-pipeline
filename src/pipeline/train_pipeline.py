from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from sklearn.model_selection import StratifiedKFold, cross_val_score

import sys
import os
from src.logger import logger
from src.exception import CustomException


class TrainPipeline:

    def run(self):
        try:
            logger.info("Training pipeline started")

            train_df, test_df = DataIngestion().initiate_data_ingestion()

            transformer = DataTransformation()

            train_df = transformer.create_features(train_df)
            test_df = transformer.create_features(test_df)

            # ⭐ SAVE PROCESSED DATA
            os.makedirs("data/processed", exist_ok=True)
            train_df.to_csv("data/processed/train_processed.csv", index=False)
            test_df.to_csv("data/processed/test_processed.csv", index=False)

            logger.info("Processed datasets saved")

            y = train_df['Survived']
            X = train_df.drop('Survived', axis=1)

            preprocess = transformer.get_preprocessor()
            pipe = ModelTrainer().train(X, y, preprocess)

            skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
            scores = cross_val_score(pipe, X, y, cv=skf, scoring='accuracy')

            logger.info(f"CV Accuracy: {scores.mean()}")
            print("CV Accuracy:", scores.mean())

            logger.info("Training pipeline completed")

            return pipe, test_df

        except Exception as e:
            logger.error("Error in training pipeline")
            raise CustomException(e, sys)
