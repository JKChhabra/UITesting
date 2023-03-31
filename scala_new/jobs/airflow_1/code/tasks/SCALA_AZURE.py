def SCALA_AZURE():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "SCALA_AZURE",
        json = {"task_key" : "SCALA_AZURE"},
        databricks_conn_id = "databricks_default",
    )
