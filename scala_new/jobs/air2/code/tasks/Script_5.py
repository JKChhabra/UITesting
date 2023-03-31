def Script_5():
    from airflow.operators.python import PythonOperator

    return PythonOperator(task_id = "Script_5", python_callable = lambda *args, **kwargs: exec(""), )
