FROM python:3.10-slim

WORKDIR /app

COPY environment.yml /app/environment.yml

RUN pip install --upgrade pip && \
    pip install pyspark==3.5.0 pandas numpy matplotlib scikit-learn

COPY . /app

CMD ["python", "run_pipeline.py"]
