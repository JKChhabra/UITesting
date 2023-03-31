from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def FlattenSchema_1_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0\
        .withColumn("c_array--long", explode_outer("c_array--long"))\
        .withColumn("c_array-int  _ int", explode_outer("c_array-int  _ int"))\
        .withColumn("-- c_array_timestamp -- ", explode_outer("-- c_array_timestamp -- "))\
        .withColumn("c_array -- float", explode_outer("c_array -- float"))\
        .withColumn("c_struct -- _  -c_array_int - of a struct ", explode_outer("c_struct -- _  .c_array_int - of a struct "))\
        .select(col("c_struct -- _  .c_string - of a struct -- _").alias("c_struct -- _  -c_string - of a struct -- _"), col("c_struct -- _  .c_array_int - of a struct ").alias("c_struct -- _  -c_array_int - of a struct "), col("c_array--long"), col("c_array-int  _ int"), col("-- c_array_timestamp -- "), col("c_array -- float"))
