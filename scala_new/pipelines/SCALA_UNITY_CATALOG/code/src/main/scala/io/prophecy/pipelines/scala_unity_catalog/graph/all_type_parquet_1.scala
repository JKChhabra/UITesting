package io.prophecy.pipelines.scala_unity_catalog.graph

import io.prophecy.libs._
import io.prophecy.pipelines.scala_unity_catalog.config.ConfigStore._
import io.prophecy.pipelines.scala_unity_catalog.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object all_type_parquet_1 {

  def apply(context: Context): DataFrame =
    context.spark.read.table("qa_database.all_type_parquet")

}
