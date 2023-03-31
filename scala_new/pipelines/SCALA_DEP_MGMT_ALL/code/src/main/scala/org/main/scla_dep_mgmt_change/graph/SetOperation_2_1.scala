package org.main.scla_dep_mgmt_change.graph

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.config.Context
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object SetOperation_2_1 {

  def apply(context: Context, in0: DataFrame, in1: DataFrame): DataFrame = {
    var res = in0
    if (Some(false).getOrElse(false))
      res = res.unionByName(in1, allowMissingColumns = true)
    else res = res.unionByName(in1)
    res
  }

}
