import pandas as pd
import os
import sys

from src.logger import logger
from src.exception import CustomException


class DataIngestion:
    def initiate_data_ingestion(self):
        try:
            logger.info("Data ingestion started")

            train_path = os.path.join("data", "raw", "titanic", "train.csv")
            test_path  = os.path.join("data", "raw", "titanic", "test.csv")

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info("Data ingestion completed")

            return train_df, test_df

        except Exception as e:
            logger.error("Error occurred in data ingestion")
            raise CustomException(e, sys)
