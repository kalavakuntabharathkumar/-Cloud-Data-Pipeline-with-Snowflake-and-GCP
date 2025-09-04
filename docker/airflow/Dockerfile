
FROM apache/airflow:2.9.3-python3.11
USER root
RUN apt-get update && apt-get install -y build-essential git && rm -rf /var/lib/apt/lists/*
USER airflow
RUN pip install --no-cache-dir     apache-airflow-providers-google==12.3.0     apache-airflow-providers-snowflake==5.4.0     snowflake-connector-python==3.10.1     google-cloud-bigquery==3.25.0     dbt-core==1.7.9 dbt-bigquery==1.7.6 dbt-snowflake==1.7.2     great-expectations==0.18.12     cryptography==43.0.1
