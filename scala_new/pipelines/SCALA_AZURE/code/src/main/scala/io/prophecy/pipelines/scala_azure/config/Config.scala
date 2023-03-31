package io.prophecy.pipelines.scala_azure.config

import io.prophecy.pipelines.scala_azure.config.ConfigStore._
import io.prophecy.pipelines.scala_azure.config.Context
import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._
case class Config() extends ConfigBase
