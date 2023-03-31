package io.prophecy.pipelines.scala_unity_catalog.config

import org.apache.spark.sql.SparkSession
case class Context(spark: SparkSession, config: Config)
