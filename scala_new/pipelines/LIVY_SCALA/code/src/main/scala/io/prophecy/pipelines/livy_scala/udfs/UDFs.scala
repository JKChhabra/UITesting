package io.prophecy.pipelines.livy_scala.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {
  var a = 10

  def registerUDFs(spark: SparkSession) =
    spark.udf.register("udf1", udf1)

  def udf1 = udf((value: Int) => value * a)
}
