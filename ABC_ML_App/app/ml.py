"""ML utilities and model management.

Will contain training, inference, and model persistence utilities.
"""

import pandas as pd


def load_dataframe(path):
    # Minimal helper to read CSVs; add validation in later steps.
    return pd.read_csv(path)
