def REL_SC_PIP_DEP_MGMT_ALL():
    from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator # noqa

    return DatabricksSubmitRunOperator(  # noqa
        task_id = "REL_SC_PIP_DEP_MGMT_ALL",
        json = {
          "task_key": "REL_SC_PIP_DEP_MGMT_ALL", 
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
          "libraries": [{"maven" : {"coordinates" : "io.prophecy:prophecy-libs_2.12:3.3.0-7.0.14"}},                          {"pypi" : {"package" : "prophecy-libs==1.4.8"}},                          {
                           "jar": "dbfs:/FileStore/prophecy/artifacts/sony/cp/79/1679913916358/pipeline/REL_SC_PIP_DEP_MGMT_ALL.jar"
                         },                          {"maven" : {"coordinates" : "mysql:mysql-connector-java:8.0.29", "exclusions" : []}},                          {"maven" : {"coordinates" : "org.typelevel:cats-core_2.12:2.6.1", "exclusions" : []}}]
        },
        databricks_conn_id = "databricks_default",
        email = "", 
        queue = "", 
        weight_rule = "", 
        wait_for_downstream = False, 
        email_on_retry = False, 
        depends_on_past = False, 
        retry_exponential_backoff = False, 
        trigger_rule = "", 
        ignore_first_depends_on_past = False, 
        email_on_failure = False
    )
