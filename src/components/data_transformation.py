from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import sys

from src.logger import logger
from src.exception import CustomException


class DataTransformation:

    def create_features(self, df):
        try:
            logger.info("Feature engineering started")

            rare_titles = [
                'Dr', 'Rev', 'Col', 'Major', 'Don', 'Lady', 'Sir',
                'Capt', 'the Countess', 'Jonkheer', 'Dona'
            ]

            def group_ticket_freq(freq):
                if freq == 1:
                    return 'Solo'
                elif 2 <= freq <= 4:
                    return 'Small_Group'
                else:
                    return 'Large_Group'

            df = (
                df.copy()
                .assign(
                    Title=lambda x: (x["Name"].str.extract(r",\s*([^\.]+)\.")
                        .replace(['Mlle', 'Ms'], 'Miss')
                        .replace('Mme', 'Mrs')
                        .replace(rare_titles, 'Rare')),
                    Deck=lambda x: (x["Cabin"].str[0].fillna("Unknown")
                        .replace('T', 'A')
                        .replace(['A', 'B', 'C'], 'ABC')
                        .replace(['D', 'E'], 'DE')
                        .replace(['F', 'G'], 'FG')),
                    Family_Size=lambda x: x["SibSp"] + x["Parch"] + 1,
                    Ticket=lambda x: x["Ticket"].astype(str),
                    Ticket_Frequency=lambda x: x.groupby("Ticket")["Ticket"].transform("count"),
                    Ticket_Group=lambda x: x["Ticket_Frequency"].apply(group_ticket_freq),
                )
                .drop(columns=["Name", "Ticket", "Ticket_Frequency", "Cabin", "PassengerId"])
            )

            logger.info("Feature engineering completed")
            return df

        except Exception as e:
            logger.error("Error during feature engineering")
            raise CustomException(e, sys)

    def get_preprocessor(self):
        try:
            logger.info("Preprocessor creation started")

            num_cols = ['Age', 'Fare', 'Family_Size', 'SibSp', 'Parch']
            cat_cols = ['Sex', 'Embarked', 'Pclass', 'Title', 'Deck', 'Ticket_Group']

            num_pipe = Pipeline([
                ('impute', SimpleImputer(strategy='median')),
                ('scale', StandardScaler())
            ])

            cat_pipe = Pipeline([
                ('impute', SimpleImputer(strategy='most_frequent')),
                ('onehot', OneHotEncoder(handle_unknown='ignore'))
            ])

            preprocess = ColumnTransformer([
                ('num', num_pipe, num_cols),
                ('cat', cat_pipe, cat_cols)
            ])

            logger.info("Preprocessor creation completed")
            return preprocess

        except Exception as e:
            logger.error("Error during preprocessor creation")
            raise CustomException(e, sys)
