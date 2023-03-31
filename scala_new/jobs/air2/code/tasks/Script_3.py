def Script_3():
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Script_3", python_callable = lambda *args, **kwargs: exec(""), )
