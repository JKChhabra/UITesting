package io.prophecy.pipelines.livy_scala.graph

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.config.ConfigStore._
import io.prophecy.pipelines.livy_scala.config.Context
import io.prophecy.pipelines.livy_scala.udfs.UDFs._
import io.prophecy.pipelines.livy_scala.udfs._
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object FlattenSchema_1 {

  def apply(context: Context, in: DataFrame): DataFrame =
    in.withColumn("arr_str1", explode_outer(col("arr_str1")))
      .withColumn("arr_str2", explode_outer(col("arr_str2")))
      .withColumn("struct_complex-col2",
                  explode_outer(col("struct_complex.col2"))
      )
      .withColumn("struct_complex-col1",
                  explode_outer(col("struct_complex.col1"))
      )
      .select(col("arr_str1"),
              col("arr_str2"),
              col("struct_complex.col2").as("struct_complex-col2"),
              col("struct_complex.col1").as("struct_complex-col1"),
              col("year")
      )

}
