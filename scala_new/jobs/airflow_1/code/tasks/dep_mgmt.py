def dep_mgmt():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "dep_mgmt",
        json = {
          "task_key": "dep_mgmt", 
          "new_cluster": {
            "node_type_id": "i3.xlarge", 
            "spark_version": "11.3.x-scala2.12", 
            "num_workers": 1, 
            "spark_conf": {}, 
            "driver_node_type_id": "i3.xlarge", 
            "aws_attributes": {"first_on_demand" : 1, "availability" : "SPOT_WITH_FALLBACK"}
          }, 
          "spark_jar_task": {
            "main_class_name": "org.main.scla_dep_mgmt_change.Main", 
            "parameters": ["-i", "default", "-O", "{}"]
          }, 
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.0.13"}},                          {"pypi" : {"package" : "prophecy-libs==1.4.7"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/sony/cp/79/1679895452161/pipeline/REL_SC_PIP_DEP_MGMT_ALL.jar"
                         },                          {"maven" : {"coordinates" : "mysql:mysql-connector-java:8.0.29", "exclusions" : []}},                          {"maven" : {"coordinates" : "org.typelevel:cats-core_2.12:2.6.1", "exclusions" : []}}]
        },
        databricks_conn_id = "databricks_default",
    )
