def Pipeline_6():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "Pipeline_6",
        json = {"task_key" : "Pipeline_6"},
        databricks_conn_id = "databricks_default",
    )
