from src.extract import extract
from src.transform import transform
from src.load import load


def run_pipeline():
    df = extract("data/raw_data.csv")
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run_pipeline()
