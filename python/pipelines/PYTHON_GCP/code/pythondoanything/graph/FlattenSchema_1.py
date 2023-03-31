from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *

def FlattenSchema_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("c_array-int  _ int", explode_outer("c_array-int  _ int"))\
        .withColumn("c_array-string  _ string", explode_outer("c_array-string  _ string"))\
        .withColumn("-- c_array_timestamp -- ", explode_outer("-- c_array_timestamp -- "))\
        .withColumn("c_struct -- _  -c_array_int - of a struct ", explode_outer("c_struct -- _  .c_array_int - of a struct "))\
        .select(col("c_array-int  _ int"), col("c_array-string  _ string"), col("c_double"), col("-- c_array_timestamp -- "), col("c_struct -- _  .c_array_int - of a struct ").alias("c_struct -- _  -c_array_int - of a struct "))
