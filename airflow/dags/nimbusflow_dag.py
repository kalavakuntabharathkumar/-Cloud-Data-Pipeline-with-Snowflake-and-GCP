
from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.trigger_rule import TriggerRule
from airflow.utils.edgemodifier import Label
from great_expectations.data_context import FileDataContext
from great_expectations.checkpoint import Checkpoint
from connectors.snowflake_conn import ensure_demo_schema as sf_ensure
from connectors.bigquery_conn import ensure_demo_dataset as bq_ensure

DAG_ID = "nimbusflow_ingest_dbt_publish"
default_args = {
    "owner": "data-eng",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "email_on_failure": False,
    "email_on_retry": False,
}

def branch_env():
    return "cloud_path" if os.getenv("NIMBUS_ENV", "LOCAL").upper() == "CLOUD" else "local_path"

def create_expectations(**_):
    # minimal GE checkpoint referencing a CSV produced by generator as an example
    context = FileDataContext(project_root_dir="/opt/great_expectations")
    checkpoint = Checkpoint(
        name="events_checkpoint",
        data_context=context,
        validations=[{
            "batch_request": {
                "datasource_name": "local_filesystem",
                "data_asset_name": "events",
                "options": {"path": "/usr/app/data/events_latest.csv"},
            },
            "expectation_suite_name": "events_suite",
        }],
    )
    result = checkpoint.run()
    if not result["success"]:
        raise Exception("Data quality checks failed")

with DAG(
    dag_id=DAG_ID,
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    default_args=default_args,
    catchup=False,
    sla_miss_callback=lambda *args, **kwargs: print("SLA missed!"),
) as dag:

    start = EmptyOperator(task_id="start")

    choose = BranchPythonOperator(task_id="branch_env", python_callable=branch_env)

    local = EmptyOperator(task_id="local_path")
    cloud = EmptyOperator(task_id="cloud_path")

    ingest = PythonOperator(
        task_id="ingest",
        python_callable=lambda: print("Ingest complete"),
    )

    validate = PythonOperator(task_id="validate", python_callable=create_expectations)

    def load_local():
        bq_ensure()
        sf_ensure()
        print("Local load to demo schemas complete")

    load = PythonOperator(task_id="load", python_callable=load_local)

    dbt_run = PythonOperator(
        task_id="dbt_run",
        python_callable=lambda: os.system("cd /opt/dbt && dbt deps && dbt run && dbt test"),
    )

    publish = EmptyOperator(task_id="publish", trigger_rule=TriggerRule.ALL_DONE)

    end = EmptyOperator(task_id="end")

    start >> choose
    choose >> Label("LOCAL") >> local >> ingest
    choose >> Label("CLOUD") >> cloud >> ingest
    ingest >> validate >> load >> dbt_run >> publish >> end
