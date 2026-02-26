import sqlite3
import pandas as pd


def load(df: pd.DataFrame, db_name: str = "data.db") -> None:
    with sqlite3.connect(db_name) as conn:
        df.to_sql("sales", conn, if_exists="replace", index=False)
