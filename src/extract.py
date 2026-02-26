import pandas as pd


def extract(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
