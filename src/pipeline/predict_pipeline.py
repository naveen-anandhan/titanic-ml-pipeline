import pandas as pd
import pickle
from src.components.data_transformation import DataTransformation


class PredictPipeline:

    def predict(self):
        # load test data
        test_df = pd.read_csv("data/raw/test.csv")

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

        print("✅ Submission file created at outputs/submission.csv")
