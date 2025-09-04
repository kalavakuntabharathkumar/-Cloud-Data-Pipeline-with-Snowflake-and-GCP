
import os
from google.cloud import bigquery

def get_bq_client():
    project = os.getenv("GCP_PROJECT_ID")
    return bigquery.Client(project=project)

def ensure_demo_dataset():
    client = get_bq_client()
    dataset_id = f"{client.project}.{os.getenv('GCP_BQ_DATASET', 'nimbusflow_demo')}"
    dataset = bigquery.Dataset(dataset_id)
    dataset.location = "US"
    client.create_dataset(dataset, exists_ok=True)
    table_id = f"{dataset_id}.events"
    schema = [
        bigquery.SchemaField("event_time", "TIMESTAMP"),
        bigquery.SchemaField("user_id", "STRING"),
        bigquery.SchemaField("event_type", "STRING"),
        bigquery.SchemaField("amount", "FLOAT"),
        bigquery.SchemaField("payload", "JSON"),
    ]
    table = bigquery.Table(table_id, schema=schema)
    client.create_table(table, exists_ok=True)
