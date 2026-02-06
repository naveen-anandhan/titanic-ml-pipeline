from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline

class ModelTrainer:
    def train(self, X, y, preprocessor):
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
        return pipe
