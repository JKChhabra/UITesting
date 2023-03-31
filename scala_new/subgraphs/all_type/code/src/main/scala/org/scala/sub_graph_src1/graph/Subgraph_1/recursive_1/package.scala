package org.scala.sub_graph_src1.graph.Subgraph_1

import io.prophecy.libs._
import com.main.sub_graph_src1.graph.Subgraph_1.recursive_1.Subgraph_2_1
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object recursive_1 {

  def apply(spark: SparkSession, in0: DataFrame): DataFrame = {
    val df_Reformat_3_1 = Reformat_3_1(spark,       in0)
    val df_Subgraph_2_1 = Subgraph_2_1.apply(spark, df_Reformat_3_1)
    df_Subgraph_2_1
  }

}
