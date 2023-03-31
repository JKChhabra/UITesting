def scala_basic():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "scala_basic",
        json = {
          "task_key": "scala_basic", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {}, 
            "driver_node_type_id": "i3.xlarge", 
            "aws_attributes": {"first_on_demand" : 1, "availability" : "SPOT_WITH_FALLBACK"}
          }, 
          "spark_jar_task": {
            "main_class_name": "com.scala.main.job1.Main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.0.13"}},                          {"pypi" : {"package" : "prophecy-libs==1.4.7"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/sony/cp/79/1679895452178/pipeline/SCALA_BASIC.jar"
                         }]
        },
        databricks_conn_id = "databricks_default",
    )
