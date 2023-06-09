from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def Script_2_1_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, in2: DataFrame) -> DataFrame:
    out1 = in0.select("c-string")
    out2 = in1.select("c-string")
    out3 = in2.select("c-string")
    out0 = out1.union(out2).union(out3)

    return out0
