def Script_2():
    from airflow.operators.bash import BashOperator

    return BashOperator(task_id = "Script_2", bash_command = "echo \"test\"", )
