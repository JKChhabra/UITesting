package com.scala.main.job1

import io.prophecy.libs._
import com.scala.main.job1.config.ConfigStore._
import com.scala.main.job1.config.Context
import com.scala.main.job1.config._
import com.scala.main.job1.udfs.UDFs._
import com.scala.main.job1.udfs._
import com.scala.main.job1.graph._
import com.scala.main.job1.graph.Subgraph_1
import com.scala.main.job1.graph.Subgraph_3
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_parquet_all_type_and_partition_withspacehyphens1 =
      src_parquet_all_type_and_partition_withspacehyphens1(context)
    val df_SQLStatement_1 = SQLStatement_1(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Reformat_1 = Reformat_1(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_1 = Subgraph_1.apply(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Subgraph_3 = Subgraph_3.apply(context, df_Subgraph_1)
    val df_Reformat_7 = Reformat_7(context,       df_Subgraph_3)
    val df_Reformat_11 = Reformat_11(
      context,
      df_src_parquet_all_type_and_partition_withspacehyphens1
    )
    val df_Reformat_4 = Reformat_4(context, df_Reformat_1)
    dest_test(context, df_Reformat_4)
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.fromCLI(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    spark.conf.set("spark_config1", "spark_config_value_1")
    spark.conf.set("spark_config2", "spark_config_value_2")
    spark.conf.set("prophecy.metadata.pipeline.uri",
                   "pipelines/EM_DISABLED_SCALA_BASIC"
    )
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config1", "hadoop_config_value1")
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2",      "hadoop_config_value2")
    MetricsCollector.start(spark, "pipelines/EM_DISABLED_SCALA_BASIC")
    apply(context)
    MetricsCollector.end(spark)
  }

}
