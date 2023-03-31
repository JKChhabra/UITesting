package io.prophecy.pipelines.scala_azure

import io.prophecy.libs._
import io.prophecy.pipelines.scala_azure.config.ConfigStore._
import io.prophecy.pipelines.scala_azure.config.Context
import io.prophecy.pipelines.scala_azure.config._
import io.prophecy.pipelines.scala_azure.udfs.UDFs._
import io.prophecy.pipelines.scala_azure.udfs._
import io.prophecy.pipelines.scala_azure.graph._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def apply(context: Context): Unit = {
    val df_src_azure  = src_azure(context)
    val df_Reformat_1 = Reformat_1(context, df_src_azure)
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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_AZURE")
    MetricsCollector.start(spark,                    "pipelines/SCALA_AZURE")
    apply(context)
    MetricsCollector.end(spark)
  }

}
