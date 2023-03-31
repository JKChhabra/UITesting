def Pipeline_0():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "Pipeline_0",
        json = {
          "task_key": "Pipeline_0", 
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
            "parameters": ["-i",  "test-random3",  "-O",                             "{\"c_test\":\"nmnmnm\",\"c_array\":[\"mnmmnmmnm\"],\"bool\":false}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.0.14"}},                          {"pypi" : {"package" : "prophecy-libs==1.4.8"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/sony/cp/79/1679979355552/pipeline/SCALA_BASIC.jar"
                         }]
        },
        databricks_conn_id = "databricks_default",
    )
