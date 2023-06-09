from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *

def Repartition_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.repartition(
        10,
        concat(col("`c  - int`"), col("`c_struct -- _  `.`c_string - of a struct -- _`")), 
        concat(lit(Config.c_repartition_colname), col("`c- short`"))
    )
