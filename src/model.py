import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class SalesModel:
    def __init__(self):
        self.model = LinearRegression()

    def train(self, df: pd.DataFrame):
        X = df[['day', 'month', 'weekday']]
        y = df['revenue']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

    def predict(self, df: pd.DataFrame):
        X = df[['day', 'month', 'weekday']]
        return self.model.predict(X)