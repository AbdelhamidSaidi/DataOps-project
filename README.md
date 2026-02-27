DataOps Project – End-to-End Data Pipeline with CI/CD and Interactive Dashboard

Overview

This project demonstrates a complete DataOps workflow, from data
generation and processing to automated testing, CI/CD integration, and
interactive data visualization using Streamlit.

The goal of this project is to showcase:

-   Data pipeline automation
-   Clean project structure
-   Continuous Integration (CI)
-   Continuous Deployment (CD)
-   Interactive dashboard deployment
-   Production-ready dependency management

------------------------------------------------------------------------

Project Architecture

					+---------------------+
					|   Data Generation   |
					|   (Faker / Scripts) |
					+----------+----------+
							   |
							   v
					+---------------------+
					|   Data Processing   |
					|   (Pandas / Numpy)  |
					+----------+----------+
							   |
							   v
					+---------------------+
					|   Data Validation   |
					|     (Pytest CI)     |
					+----------+----------+
							   |
							   v
					+---------------------+
					|   GitHub Actions    |
					| Continuous Integration |
					+----------+----------+
							   |
							   v
					+---------------------+
					|   Streamlit App     |
					|   Interactive Viz   |
					+----------+----------+
							   |
							   v
					+---------------------+
					| Streamlit Cloud     |
					| Continuous Deployment |
					+---------------------+

------------------------------------------------------------------------

Tech Stack

-   Python
-   Pandas
-   NumPy
-   Plotly
-   Streamlit
-   Pytest
-   GitHub Actions

------------------------------------------------------------------------

Project Structure

	dataops-project/
	│
	├── app.py                  # Streamlit dashboard
	├── requirements.txt        # Production dependencies
	├── runtime.txt             # Python version control
	│
	├── data/
	│   ├── raw/                # Generated raw data
	│   ├── processed/          # Cleaned datasets
	│   └── visualizations/     # Exported charts
	│
	├── tests/
	│   └── test_data.py        # Data validation tests
	│
	└── .github/workflows/
		└── ci.yml              # GitHub Actions pipeline

------------------------------------------------------------------------

Features

1. Data Generation

-   Synthetic dataset creation using Faker
-   Structured tabular format
-   Reproducible pipelines

2. Data Processing

-   Cleaning and transformation
-   Aggregations
-   Feature engineering

3. Automated Testing

-   Data validation using Pytest
-   Schema verification
-   Integrity checks

4. Continuous Integration (CI)

-   Automated testing on every push
-   Linting and quality checks
-   Fails fast on broken builds

5. Continuous Deployment (CD)

-   Automatic deployment to Streamlit Cloud
-   Rebuild on GitHub push
-   Zero manual deployment

6. Interactive Dashboard

-   Built with Streamlit
-   Dynamic filtering
-   Interactive visualizations with Plotly
-   Real-time data exploration

------------------------------------------------------------------------

Installation (Local Development)

Clone the repository:

	git clone https://github.com/AbdelhamidSaidi/dataops-project.git
	cd dataops-project

Create virtual environment:

	python -m venv venv
	source venv/bin/activate  # or venv\Scripts\activate on Windows

Install dependencies:

	pip install -r requirements.txt

Run the app:

	streamlit run app.py

------------------------------------------------------------------------

Deployment

The project is deployed using Streamlit Cloud.

Deployment workflow:

1.  Push changes to main branch
2.  GitHub Actions runs tests
3.  If tests pass → Streamlit Cloud rebuilds
4.  New version goes live automatically

------------------------------------------------------------------------

Dependency Management Strategy

Production dependencies are intentionally minimal:

-   Only top-level libraries are pinned
-   No development tools in production
-   numpy<2 ensures Streamlit compatibility
-   Python version controlled with runtime.txt

This prevents cloud deployment conflicts.

------------------------------------------------------------------------

CI/CD Pipeline

GitHub Actions automatically:

-   Installs dependencies
-   Runs tests
-   Fails build if tests fail
-   Allows deployment only on success

This simulates real-world DataOps workflow.

------------------------------------------------------------------------

Future Improvements

-   Add database integration (PostgreSQL)
-   Add Docker containerization
-   Add data quality monitoring
-   Add scheduled data refresh
-   Implement logging & observability

------------------------------------------------------------------------
