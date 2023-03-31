from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythondoanything.config.ConfigStore import *
from pythondoanything.udfs.UDFs import *
from prophecy.utils import *
from pythondoanything.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_special_char_column_name = src_csv_special_char_column_name(spark)
    df_Join_1 = Join_1(spark, df_src_csv_special_char_column_name, df_src_csv_special_char_column_name)
    df_RowDistributor_1_out0, df_RowDistributor_1_out1 = RowDistributor_1(spark, df_Join_1)
    df_src_parquet_all_type_and_partition_withspacehyphens = src_parquet_all_type_and_partition_withspacehyphens(spark)
    df_Reformat_1 = Reformat_1(spark, df_src_parquet_all_type_and_partition_withspacehyphens)
    df_Filter_1 = Filter_1(spark, df_Reformat_1)
    df_OrderBy_1 = OrderBy_1(spark, df_Filter_1)
    df_Aggregate_1 = Aggregate_1(spark, df_OrderBy_1)
    df_Repartition_1 = Repartition_1(spark, df_RowDistributor_1_out0)
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_OrderBy_1)
    df_Script_1 = Script_1(spark, df_RowDistributor_1_out1)
    df_src_orc_all_type_no_partition = src_orc_all_type_no_partition(spark)
    df_Limit_1 = Limit_1(spark, df_src_orc_all_type_no_partition)
    df_SetOperation_1 = SetOperation_1(
        spark, 
        df_src_parquet_all_type_and_partition_withspacehyphens, 
        df_src_parquet_all_type_and_partition_withspacehyphens
    )
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_SetOperation_1)
    df_Deduplicate_1 = Deduplicate_1(spark, df_SchemaTransform_1)
    df_WindowFunction_1 = WindowFunction_1(spark, df_OrderBy_1)
    df_OrderBy_2 = OrderBy_2(spark, df_Limit_1)
    df_SQLStatement_1_out, df_SQLStatement_1_out1 = SQLStatement_1(spark, df_Deduplicate_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_GCP")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_GCP")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
