package com.main.sub_graph_src1.config

import org.apache.spark.sql._
import com.main.sub_graph_src1.config.ConfigStore._
import com.main.sub_graph_src1.config.Context
import pureconfig.ConfigReader.Result
import pureconfig._
import pureconfig.generic.ProductHint
import pureconfig.generic.auto._
import io.prophecy.libs._

object ConfigStore {
  implicit val interimOutput: InterimOutput = InterimOutputHive2("")
}

object ConfigurationFactoryImpl extends ConfigurationFactory[Config] {

  override protected def load(
    fileConfig: ConfigObjectSource
  ): Result[Config] = {
    implicit val confHint: ProductHint[Config] =
      ProductHint[Config](ConfigFieldMapping(CamelCase, CamelCase))
    fileConfig.load[Config]
  }

}