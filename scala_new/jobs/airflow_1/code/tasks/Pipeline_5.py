def Pipeline_5():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "Pipeline_5",
        json = {"task_key" : "Pipeline_5"},
        databricks_conn_id = "databricks_default",
    )
