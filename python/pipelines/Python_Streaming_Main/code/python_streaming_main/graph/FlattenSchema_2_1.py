from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from python_streaming_main.config.ConfigStore import *
from python_streaming_main.udfs.UDFs import *

def FlattenSchema_2_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("value.amount").alias("amount"), 
        col("value.customer_id").alias("customer_id"), 
        col("value.order_category").alias("order_category"), 
        col("value.order_date").alias("order_date"), 
        col("value.order_id").alias("order_id"), 
        col("value.order_status").alias("order_status"), 
        col("timestamp")
    )
