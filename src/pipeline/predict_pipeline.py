import pandas as pd

class PredictPipeline:

    def predict(self, model, test_df):
        preds = model.predict(test_df)

        submission = pd.DataFrame({
            "PassengerId": pd.read_csv("data/raw/test.csv")['PassengerId'],
            "Survived": preds.astype(int)
        })

        submission.to_csv("outputs/submission.csv", index=False)
