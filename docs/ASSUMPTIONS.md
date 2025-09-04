
# Assumptions

- Demo pipeline writes CSV locally; cloud loads are schema-ensured but not auto-ingesting to avoid costs.
- dbt uses profiles from `profiles.yml.example`; users will copy to their `~/.dbt/profiles.yml` or mount env vars.
- Alerting via Slack webhook is optional.
