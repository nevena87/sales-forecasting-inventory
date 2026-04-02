import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


class SalesModel:
    def __init__(self):
        self.model = LinearRegression()

    # ---------------------------
    # Feature Engineering
    # ---------------------------
    def create_features(self, df: pd.DataFrame):

        df = df.sort_values(['product_id', 'date'])

        # Lag feature (previous day revenue)
        df['revenue_previous_day'] = (
            df.groupby('product_id')['revenue'].shift(1)
        )

        # Rolling 7-day average
        df['rolling_7d_avg'] = (
            df.groupby('product_id')['revenue']
            .rolling(window=7, min_periods=1)
            .mean()
            .reset_index(level=0, drop=True)
        )

        # Date features
        df['date'] = pd.to_datetime(df['date'])
        df['day'] = df['date'].dt.day
        df['month'] = df['date'].dt.month
        df['weekday'] = df['date'].dt.weekday

        # Fill NaN values from lag
        df['revenue_previous_day'] = df['revenue_previous_day'].fillna(0)

        # One-hot encoding for product_id
        df = pd.get_dummies(df, columns=['product_id'], prefix='product')

        return df

    # ---------------------------
    # Train Model
    # ---------------------------
    def train(self, df: pd.DataFrame):

        df = self.create_features(df)

        # Features & target
        X = df.drop(columns=['revenue', 'date'])
        y = df['revenue']

        # Split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Train
        self.model.fit(X_train, y_train)

        # Evaluate
        y_pred = self.model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        print("Model Evaluation:")
        print("MAE:", mae)
        print("RMSE:", rmse)

    # ---------------------------
    # Predict
    # ---------------------------
    def predict(self, df: pd.DataFrame):

        df = self.create_features(df)

        X = df.drop(columns=['revenue', 'date'])

        return self.model.predict(X)