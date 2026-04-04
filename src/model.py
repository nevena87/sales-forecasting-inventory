import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error


class SalesModel:
    def __init__(self):
        self.model = LinearRegression()
        self.feature_columns = None

    # ---------------------------
    # Feature Engineering
    # ---------------------------
    def create_features(self, df: pd.DataFrame):

        df = df.sort_values(['product_id', 'date'])

        df['date'] = pd.to_datetime(df['date'])

        # Lag feature
        df['revenue_previous_day'] = (
            df.groupby('product_id')['revenue'].shift(1)
        )

        # Rolling WITHOUT leakage
        df['rolling_7d_avg'] = (
            df.groupby('product_id')['revenue']
            .shift(1)
            .rolling(window=7, min_periods=1)
            .mean()
        )

        # Date features
        df['day'] = df['date'].dt.day
        df['month'] = df['date'].dt.month
        df['weekday'] = df['date'].dt.weekday

        # Fill NaN
        df['revenue_previous_day'] = df['revenue_previous_day'].fillna(0)
        df['rolling_7d_avg'] = df['rolling_7d_avg'].fillna(0)

        # One-hot encoding
        df = pd.get_dummies(df, columns=['product_id'], prefix='product')

        return df

    # ---------------------------
    # Train Model (time-based split)
    # ---------------------------
    def train(self, df: pd.DataFrame):

        df = self.create_features(df)

        # sort by date
        df = df.sort_values('date')

        # split (80% train, 20% test)
        split_index = int(len(df) * 0.8)

        train_df = df.iloc[:split_index]
        test_df = df.iloc[split_index:]

        X_train = train_df.drop(columns=['revenue', 'date'])
        y_train = train_df['revenue']

        X_test = test_df.drop(columns=['revenue', 'date'])
        y_test = test_df['revenue']

        # save feature columns
        self.feature_columns = X_train.columns

        # align test columns (case mismatch)
        X_test = X_test.reindex(columns=self.feature_columns, fill_value=0)

        # train
        self.model.fit(X_train, y_train)

        # evaluate
        y_pred = self.model.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        rmse = np.sqrt(mean_squared_error(y_test, y_pred))

        print("Model Evaluation:")
        print(f"MAE: {mae:.2f}")
        print(f"RMSE: {rmse:.2f}")

    # ---------------------------
    # Predict
    # ---------------------------
    def predict(self, df: pd.DataFrame):

        df = self.create_features(df)

        X = df.drop(columns=['revenue', 'date'])

        # align columns
        X = X.reindex(columns=self.feature_columns, fill_value=0)

        return self.model.predict(X)