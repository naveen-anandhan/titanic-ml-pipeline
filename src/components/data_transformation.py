from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer

class DataTransformation:
    def create_features(df):
        df = df.copy()

        rare_titles = [
            'Dr', 'Rev', 'Col', 'Major', 'Don', 'Lady', 'Sir',
            'Capt', 'the Countess', 'Jonkheer', 'Dona'
        ]

        # ======================
        # Title
        # ======================
        df["Title"] = df["Name"].str.extract(r",\s*([^\.]+)\.")
        df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
        df['Title'] = df['Title'].replace('Mme', 'Mrs')
        df['Title'] = df['Title'].replace(rare_titles, 'Rare')

        # ======================
        # Deck
        # ======================
        df['Deck'] = df['Cabin'].str[0]
        df['Deck'] = df['Deck'].fillna('Unknown')

        df['Deck'] = df['Deck'].replace('T', 'A')
        df['Deck'] = df['Deck'].replace(['A', 'B', 'C'], 'ABC')
        df['Deck'] = df['Deck'].replace(['D', 'E'], 'DE')
        df['Deck'] = df['Deck'].replace(['F', 'G'], 'FG')

        # ======================
        # Family size
        # ======================
        df['Family_Size'] = df['SibSp'] + df['Parch'] + 1


        
        # ======================
        # Ticket Group
        # ======================
        df['Ticket'] = df['Ticket'].astype(str)
        df['Ticket_Frequency'] = df.groupby('Ticket')['Ticket'].transform('count')

        def group_ticket_freq(freq):
            if freq == 1:
                return 'Solo'
            elif 2 <= freq <= 4:
                return 'Small_Group'
            else:
                return 'Large_Group'

        df['Ticket_Group'] = df['Ticket_Frequency'].apply(group_ticket_freq)

        # ======================
        # Drop unused columns
        # ======================
        df.drop(
            ['Name', 'Ticket', 'Ticket_Frequency', 'Cabin', 'PassengerId'],
            axis=1,
            inplace=True
        )

        return df


    def get_preprocessor(self):
        num_cols = [
            'Age',
            'Fare',
            'Family_Size',
            'SibSp',
            'Parch'
        ]

        cat_cols = [
            'Sex',
            'Embarked',
            'Pclass',
            'Title',
            'Deck',
            'Ticket_Group'
        ]



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

        return preprocess
