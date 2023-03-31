package com.scala.main.job1.graph

import com.holdenkarau.spark.testing.DataFrameSuiteBase
import com.scala.main.job1.config._
import io.prophecy.libs.SparkTestingUtils._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{Column, DataFrame}
import org.apache.spark.sql.functions._
import org.junit.runner.RunWith
import org.junit.Assert
import org.scalatest.FunSuite
import java.time.LocalDateTime
import org.scalatest.junit.JUnitRunner
import java.sql.{Date, Timestamp}
import scala.collection.JavaConverters._
import java.nio.file.{Files, Paths}
import java.math.BigDecimal

@RunWith(classOf[JUnitRunner])
class SCALA_BASIC12Test extends FunSuite with DataFrameSuiteBase {
  import sqlContext.implicits._
  var context: Context = null

  test("Unit Test 0") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/data/unit_test_0.json",
      "in0"
    )
    val dfOut0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/data/unit_test_0.json",
      "out0"
    )

    val dfOut0Computed = com.scala.main.job1.graph.SCALA_BASIC12(context, dfIn0)

  }

  test("Unit Test 1") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/data/unit_test_1.json",
      "in0"
    )
    val dfOut0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/data/unit_test_1.json",
      "out0"
    )

    val dfOut0Computed = com.scala.main.job1.graph.SCALA_BASIC12(context, dfIn0)

  }

  test("Unit Test 2") {

    val dfIn0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/in0/data/unit_test_2.json",
      "in0"
    )
    val dfOut0 = createDfFromResourceFiles(
      spark,
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/schema.json",
      "/data/com/scala/main/job1/graph/SCALA_BASIC12/out0/data/unit_test_2.json",
      "out0"
    )

    val dfOut0Computed = com.scala.main.job1.graph.SCALA_BASIC12(context, dfIn0)

  }

  override def beforeAll() = {
    super.beforeAll()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")

    val fabricName = System.getProperty("fabric")

    val config = ConfigurationFactoryImpl.fromCLI(
      Array("--confFile",
            getClass.getResource(s"/config/${fabricName}.json").getPath
      )
    )

    context = Context(spark, config)
  }

}
