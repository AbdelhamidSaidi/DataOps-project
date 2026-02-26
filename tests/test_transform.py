import pandas as pd
from src.transform import transform


def test_total_column():
    df = pd.DataFrame({"quantity": [2], "price": [10]})

    result = transform(df)

    assert result["total"].iloc[0] == 20
