from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from sklearn.model_selection import StratifiedKFold, cross_val_score

class TrainPipeline:

    def run(self):
        train_df, test_df = DataIngestion().initiate_data_ingestion()

        transformer = DataTransformation()

        train_df = transformer.create_features(train_df)
        test_df = transformer.create_features(test_df)

        y = train_df['Survived']
        X = train_df.drop('Survived', axis=1)

        preprocess = transformer.get_preprocessor()
        pipe = ModelTrainer().train(X, y, preprocess)

        skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
        scores = cross_val_score(pipe, X, y, cv=skf, scoring='accuracy')

        print("CV Accuracy:", scores.mean())

        return pipe, test_df
