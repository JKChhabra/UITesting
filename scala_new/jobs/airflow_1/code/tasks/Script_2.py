def Script_2():
    from airflow.operators.python import PythonOperator

    return PythonOperator(
        task_id = "Script_2",
        python_callable = lambda *args, **kwargs: exec("print(\"test test\")"),
    )
