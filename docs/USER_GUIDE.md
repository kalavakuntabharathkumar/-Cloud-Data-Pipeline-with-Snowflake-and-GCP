
# User Guide

## Prereqs
- Docker & Docker Compose
- (Optional) GCP and/or Snowflake accounts for cloud paths

## Quickstart
1. `cp .env.example .env` and set `AIRFLOW_FERNET_KEY` (32-byte key) & other variables.
2. `docker compose up -d --build`
3. In Airflow UI, trigger `nimbusflow_ingest_dbt_publish`.

## dbt Docs
Inside the `dbt` container run:
```
dbt docs generate && dbt docs serve --port 8081
```
