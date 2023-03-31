def Pipeline_4():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "Pipeline_4",
        json = {"task_key" : "Pipeline_4"},
        databricks_conn_id = "databricks_default",
    )
