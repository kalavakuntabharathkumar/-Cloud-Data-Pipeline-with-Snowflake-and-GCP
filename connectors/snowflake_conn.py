
import os
import snowflake.connector

def get_snowflake_conn():
    ctx = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        role=os.getenv("SNOWFLAKE_ROLE"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA", "PUBLIC"),
    )
    return ctx

def ensure_demo_schema():
    ddl = [
        "create schema if not exists DEMO",
        "create or replace table DEMO.events (event_time timestamp, user_id string, event_type string, amount number(10,2), payload variant)"
    ]
    with get_snowflake_conn() as conn:
        cs = conn.cursor()
        for stmt in ddl:
            cs.execute(stmt)
        cs.close()
