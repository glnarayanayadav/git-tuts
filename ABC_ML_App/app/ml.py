"""ML utilities and model management.

Provides simple training, persistence and prediction helpers used by the
Flask test endpoints. Uses a scikit-learn linear regressor as a lightweight
example model.
"""

import os
from typing import Sequence, List
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib


def load_dataframe(path: str) -> pd.DataFrame:
    """Read CSV into a DataFrame (small wrapper)."""
    return pd.read_csv(path)


def train_regressor(X: Sequence[Sequence[float]], y: Sequence[float]):
    """Train a simple LinearRegression and return the fitted model."""
    model = LinearRegression()
    model.fit(X, y)
    return model


def save_model(model, path: str):
    """Persist model to disk using joblib."""
    dirname = os.path.dirname(path)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    joblib.dump(model, path)


def load_model(path: str):
    """Load model from disk; raise FileNotFoundError if missing."""
    if not os.path.exists(path):
        raise FileNotFoundError(path)
    return joblib.load(path)


def predict_with_model(model, X: Sequence[Sequence[float]]) -> List[float]:
    """Run predictions; returns a list of floats."""
    preds = model.predict(X)
    return [float(p) for p in preds]
