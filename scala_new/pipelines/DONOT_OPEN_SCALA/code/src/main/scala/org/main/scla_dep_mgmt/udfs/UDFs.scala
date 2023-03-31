package org.main.scla_dep_mgmt.udfs

import _root_.io.prophecy.abinitio.ScalaFunctions._
import _root_.io.prophecy.libs._
import org.apache.spark.sql.types._
import org.apache.spark.sql.functions._
import org.apache.spark.sql._

object UDFs extends Serializable {
  var int_value    = 10
  var string_value = "string value"

  def registerUDFs(spark: SparkSession) = {
    spark.udf.register("udf_multiply",         udf_multiply)
    spark.udf.register("udf_string_null_safe", udf_string_null_safe)
    spark.udf.register("udf_string_length",    udf_string_length)
  }

  def udf_multiply = udf((value: Int) => value * int_value)

  def udf_string_null_safe =
    udf((s: String) => if (s != null) s.length else string_value.length)

  def udf_string_length = udf((s: String) => s.length)
}
