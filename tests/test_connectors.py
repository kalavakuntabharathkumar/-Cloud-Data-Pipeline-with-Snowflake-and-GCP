
def test_connectors_importable():
    import connectors.snowflake_conn as sf
    import connectors.bigquery_conn as bq
    assert hasattr(sf, "get_snowflake_conn")
    assert hasattr(bq, "get_bq_client")
