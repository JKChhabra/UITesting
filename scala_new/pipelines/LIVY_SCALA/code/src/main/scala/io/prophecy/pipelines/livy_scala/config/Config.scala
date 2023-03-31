package io.prophecy.pipelines.livy_scala.config

import io.prophecy.pipelines.livy_scala.config.ConfigStore._
import io.prophecy.pipelines.livy_scala.config.Context
import pureconfig._
import pureconfig.generic.ProductHint
import io.prophecy.libs._

case class Config(
  c_expr:    String = "%11%",
  c_st_expr: String = "concat(industry_code_ANZSIC, industry_name_ANZSIC)",
  c_string:  String = "this is default",
  c_int:     Int = 11,
  c_array: List[C_array] = List(
    C_array(car_sparkexpression = "concat('a', 10)",
            car_short = -10,
            car_float = -10.1f
    )
  ),
  c_record: C_record = C_record()
) extends ConfigBase

object C_array {

  implicit val confHint: ProductHint[C_array] =
    ProductHint[C_array](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_array(
  car_sparkexpression: String,
  car_short:           Short,
  car_float:           Float
)

object C_record {

  implicit val confHint: ProductHint[C_record] =
    ProductHint[C_record](ConfigFieldMapping(CamelCase, CamelCase))

}

case class C_record(
  cr_string: String = "hello",
  cr_double: Double = 1.23213213435e11d
)
