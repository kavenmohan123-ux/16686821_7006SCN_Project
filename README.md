# Reddit Finance Analytics Pipeline

## Project Overview
This project implements an end-to-end data engineering and analytics pipeline
for Reddit finance discussions related to S&P 500 companies. It integrates
PySpark for distributed data processing and machine learning, along with
Tableau dashboards for visualization and insight generation.

## Components
- **PySpark Data Engineering**: Data ingestion, cleaning, partitioning, and optimization
- **Distributed Machine Learning**: MLlib models (Logistic Regression, Random Forest, GBT)
- **Scalability Analysis**: Strong and weak scaling experiments
- **Visualization**: Tableau dashboards for data quality, performance, business insights, and scalability
- **Performance Profiling**: Spark UI–aligned profiling scripts

## Project Structure
- `run_pipeline.py` – End-to-end Spark ML pipeline
- `performance_profiler.py` – Spark performance and scaling analysis
- `setup_environment.sh` – Local environment setup
- `spark_config.yaml` – Spark configuration
- `tableau_config.json` – Tableau dashboard configuration
- `data/` – Schemas and sample data
- `tests/` – Basic pipeline tests

## How to Run
### Local (Python)
```bash
bash setup_environment.sh
python run_pipeline.py
```

### Docker
```bash
docker build -t reddit-finance-spark .
docker run reddit-finance-spark
```

## Notes
- Tableau dashboards are built using raw fields only (no calculated fields or bins).
- Models are evaluated using distributed AUC metrics and business-aligned measures.
- This project is suitable for academic submissions and applied data engineering demonstrations.
