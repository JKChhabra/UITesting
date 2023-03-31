def Script_4():
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Script_4", python_callable = lambda *args, **kwargs: exec(""), )
