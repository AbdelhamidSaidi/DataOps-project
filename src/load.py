import sqlite3


def load(df, db_name="data.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()
