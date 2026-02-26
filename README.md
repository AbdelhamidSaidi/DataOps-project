## DataOps project

Small ETL-style pipeline that:

1. Extracts sales data from a CSV
2. Transforms it (drops nulls, computes `total = quantity * price`)
3. Loads it into a local SQLite database (`data.db`)
4. Generates visualisations in `data/visualisations/`

### Prerequisites

- Python 3.9+ (CI uses Python 3.13)

### Install

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### (Optional) Generate the dataset

This creates/overwrites `data/raw_data.csv` (default: 150,000 rows).

```bash
python data/generate_data.py
```

### Run the pipeline

```bash
python src/main.py
```

### Outputs

- SQLite DB: `data.db` (table: `sales`)
- Visualisations (created/overwritten each run):
	- `data/visualisations/sales_by_category.png`
	- `data/visualisations/quantity_vs_price.png`
	- SVG versions are also produced alongside the PNGs

### Development

Run lint + tests:

```bash
flake8 src/
pytest
```

### CI

GitHub Actions workflow at `.github/workflows/ci.yml` runs on pushes and PRs to `main`:

- installs dependencies
- runs `flake8` + `pytest`
- runs `python src/main.py`
- uploads `data/visualisations/*` as a build artifact named `visualisations`

