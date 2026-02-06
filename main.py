from src.pipeline.train_pipeline import TrainPipeline
from src.pipeline.predict_pipeline import PredictPipeline

if __name__ == "__main__":
    model, test_df = TrainPipeline().run()
    PredictPipeline().predict(model, test_df)
