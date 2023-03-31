import os
import sys
import pendulum
from datetime import timedelta
import airflow
from airflow.decorators import dag
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from tasks import Pipeline_0, Pipeline_1, Script_1, Script_2

@dag(dag_id = "Prophecy_Job_air2", schedule_interval = "0 0 * * *", default_args = {"owner" : "Prophecy"})
def dag():
    Script_2_op = Script_2()
    Script_1_op = Script_1()
    Pipeline_1_op = Pipeline_1()
    Pipeline_0_op = Pipeline_0()
    Pipeline_0_op >> Script_1_op
    Script_1_op >> Pipeline_1_op
    Pipeline_1_op >> Script_2_op

dag()
