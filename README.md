
# NimbusFlow (Recruiter-Ready)

[![CI](https://img.shields.io/github/actions/workflow/status/youruser/nimbusflow/ci.yml?branch=main)](./.github/workflows/ci.yml)
[![Docker Build](https://img.shields.io/github/actions/workflow/status/youruser/nimbusflow/docker-build.yml?branch=main)](./.github/workflows/docker-build.yml)
[![Terraform](https://img.shields.io/github/actions/workflow/status/youruser/nimbusflow/terraform.yml?branch=main)](./.github/workflows/terraform.yml)

A production-grade, end-to-end data platform skeleton: **Airflow → (Great Expectations) → BigQuery/Snowflake → dbt → publish**.

## One-command local run

```bash
cp .env.example .env  # fill secrets
docker compose up -d --build
```

Then open:
- Airflow: http://localhost:8080
- Flower:  http://localhost:5555

## Deploy (Terraform)

See `terraform/` for GCP (GCS, BQ) and Snowflake infra. Provide `terraform.tfvars` based on `terraform.tfvars.example`.

## CI/CD

GitHub Actions for lint/tests, Docker builds, and Terraform validate.

## Security

- PII tokenization via Fernet (`PII_TOKENIZATION_KEY`).
- No credentials committed; use `.env` / Secret Manager / Vault.
- Least-privilege IaC roles (see Terraform).

## Docs

- See `docs/ARCHITECTURE.md`, `docs/USER_GUIDE.md`, and `docs/ASSUMPTIONS.md`.
# -Cloud-Data-Pipeline-with-Snowflake-and-GCP
