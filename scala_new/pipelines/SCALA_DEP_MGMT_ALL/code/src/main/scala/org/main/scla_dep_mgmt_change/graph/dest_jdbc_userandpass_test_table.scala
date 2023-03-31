package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object dest_jdbc_userandpass_test_table {

  def apply(context: Context, in: DataFrame): Unit =
    in.write
      .format("jdbc")
      .option("url",      "jdbc:mysql://18.144.156.219:3306/test_database")
      .option("dbtable",  "test_table_destination2")
      .option("user",     "test_user")
      .option("password", "admin")
      .option("driver",   "com.mysql.jdbc.Driver")
      .mode("overwrite")
      .save()

}
