
# Architecture

```mermaid
flowchart LR
  GEN[Event Generator] -->|CSV| GE[Great Expectations]
  GE --> AF[Airflow DAG]
  AF -->|Branch LOCAL/CLOUD| LOAD[Load to BQ/Snowflake]
  LOAD --> DBT[dbt models]
  DBT --> MARTS[Published Marts]
```

- Airflow DAG: `nimbusflow_ingest_dbt_publish` with branch `LOCAL` vs `CLOUD`.
- Data quality via Great Expectations.
- dbt models for staging and marts, plus tests.
- Terraform for GCP and Snowflake.
