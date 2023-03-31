package org.scala.livy.pipelines.livy_scala.graph.livyscalaSG1_1

import io.prophecy.libs._
import io.prophecy.pipelines.livy_scala.config.ConfigStore._
import io.prophecy.pipelines.livy_scala.config.Context
import io.prophecy.pipelines.livy_scala.graph.livyscalaSG1_1.Subgraph_2_1_2.Subgraph_3_1_2
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_2_1_2 {

  def apply(context: Context, in0: DataFrame): DataFrame = {
    val df_Reformat_3_1_2 = Reformat_3_1_2(context,       in0)
    val df_Subgraph_3_1_2 = Subgraph_3_1_2.apply(context, df_Reformat_3_1_2)
    df_Subgraph_3_1_2
  }

}
