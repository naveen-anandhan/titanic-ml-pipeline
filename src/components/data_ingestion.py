import pandas as pd
import os

class DataIngestion:
    def initiate_data_ingestion(self):
        train_path = os.path.join("data", "raw", "train.csv")
        test_path = os.path.join("data", "raw", "test.csv")

        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        return train_df, test_df
