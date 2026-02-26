import pandas as pd
import random
from faker import Faker

fake = Faker()


def generate_data(n_rows=150_000):
    product_categories = [
        "Electronics",
        "Clothing",
        "Books",
        "Home",
        "Sports",
        "Beauty"
    ]

    data = {
        "order_id": [fake.uuid4() for _ in range(n_rows)],
        "customer_name": [fake.name() for _ in range(n_rows)],
        "customer_email": [fake.email() for _ in range(n_rows)],
        "product_category": [random.choice(product_categories) for _ in range(n_rows)],
        "quantity": [random.randint(1, 10) for _ in range(n_rows)],
        "price": [round(random.uniform(5, 500), 2) for _ in range(n_rows)],
        "order_date": [
            fake.date_time_between(start_date="-1y", end_date="now") for _ in range(n_rows)
        ]
    }

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = generate_data()
    df.to_csv("data/raw_data.csv", index=False)
    print("Dataset generated successfully!")
