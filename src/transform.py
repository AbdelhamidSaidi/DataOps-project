import pandas as pd


def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna()
    df["total"] = df["quantity"] * df["price"]
    return df
