from extract import extract
from transform import transform
from load import load


def run_pipeline():
    df = extract("data/raw_data.csv")
    df = transform(df)
    load(df)


if __name__ == "__main__":
    run_pipeline()
