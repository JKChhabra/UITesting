package com.main.sub_graph_src1.graph

import io.prophecy.libs._
import com.main.sub_graph_src1.config.ConfigStore._
import com.main.sub_graph_src1.config.Context
import com.main.sub_graph_src1.config._
import com.main.sub_graph_src1.graph.Subgraph_1.recursive_1
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._
package object Subgraph_1 {

  def apply(
    context: Context,
    in0:     DataFrame,
    in1:     DataFrame,
    in2:     DataFrame
  ): Subgraph3 = {
    val df_src_csv_all_type_no_partition_1 =
      src_csv_all_type_no_partition_1(context).interim(
        "Subgraph_1",
        "A9rElKDgLrUiv9NV-Gb_N$$oLcoyWSajB96cj_UjB7gM",
        "0NwLDePbq8XoET6rLo-n3$$qqbCnjgSFxmc9ap6Q2yzj"
      )
    Lookup_1_1(context, df_src_csv_all_type_no_partition_1)
    val df_Reformat_2_1 = Reformat_2_1(context, in0).interim(
      "Subgraph_1",
      "hUP1i867OpQpUfEFUJCQy$$rvaoeoJj8DewfxhtkNNQJ",
      "IOGnwjIuO1YjIb-sLJyha$$HTF8HqpP8_naw8yJ3Ttq2"
    )
    val df_Filter_1_1 = Filter_1_1(context, df_Reformat_2_1).interim(
      "Subgraph_1",
      "lgmqnTtMR3qcVjlH2Ep35$$JFzi8SGtBpkzG93fbSUBl",
      "UULbpwesGwistLf0QlHPk$$xokbT7m8fnwwKYBWPVHA1"
    )
    val df_OrderBy_1_1 = OrderBy_1_1(context, df_Filter_1_1).interim(
      "Subgraph_1",
      "l-CYWkwAxWLBq7BtZXNmc$$CzZ_nMlPk_N3h120ksLg2",
      "Ddaz4jJQzSi44fZRicVSW$$A-dLHNaaqmXCBIkQv2ILR"
    )
    val df_Limit_1_1 = Limit_1_1(context, df_OrderBy_1_1).interim(
      "Subgraph_1",
      "4zrXJ1pBVISuC3q-XDTmZ$$vxGMCZONRGKNbspYxFRe2",
      "g6spxFdnq3qgPqw265z3O$$Xkqn59uh8MVUzVKw9kVy4"
    )
    val df_WindowFunction_1_1 =
      WindowFunction_1_1(context, df_Limit_1_1).interim(
        "Subgraph_1",
        "thGcHosI_1BgWDJrHjFoV$$8oixU_uuOK_-9cEZ1A_Dr",
        "gtWt2VSgvUB0J7hcxUL0n$$1G8bqF_pqkuOhr3YeV7UF"
      )
    val df_SetOperation_1_1 = SetOperation_1_1(context,
                                               df_WindowFunction_1_1,
                                               df_WindowFunction_1_1
    ).interim("Subgraph_1",
              "2364u3XyEfqkcOFGPdruQ$$EW7rZeQgZzUUvT2-nuAEC",
              "Vd1zEA7MfS5nw7LTlqhDD$$1evWrRkTooaHtS4I7ihEH"
    )
    val df_SchemaTransform_1_1 =
      SchemaTransform_1_1(context, df_SetOperation_1_1).interim(
        "Subgraph_1",
        "Cpp-eSDWFOydUile7Uyio$$HVXQZrKocwOdLjHd_W3Xy",
        "xLJkxvbQqP8DuRgGsUUiP$$beEr9oUJSVnuPjF0cyaX4"
      )
    val df_Join_1_1 =
      Join_1_1(context, df_SchemaTransform_1_1, df_SchemaTransform_1_1).interim(
        "Subgraph_1",
        "YsPCyfeLBsN_-gEeTFtDN$$rgpekk0cRrGDCCJUEGXuG",
        "RD_fpo-eYIkVlGHMOhi40$$lgO2u-aJ0Si_qNV_KSzNt"
      )
    val (df_RowDistributor_1_1_out0, df_RowDistributor_1_1_out1) = {
      val (df_RowDistributor_1_1_out0_temp, df_RowDistributor_1_1_out1_temp) =
        RowDistributor_1_1(context, df_Join_1_1)
      (df_RowDistributor_1_1_out0_temp.interim(
         "Subgraph_1",
         "PgUYSxgP6yAYJcJ3ppHfX$$ZML3vEJgQzvCX7Q5lZfN-",
         "HxaQX0nF88aUd633ycAPm$$rdEKtj-QoPeqimNSJaQPi"
       ),
       df_RowDistributor_1_1_out1_temp.interim(
         "Subgraph_1",
         "PgUYSxgP6yAYJcJ3ppHfX$$ZML3vEJgQzvCX7Q5lZfN-",
         "PwWx57iOUAbAqGLDKsfGQ$$DrNF_-EqeazJxII0yBfLZ"
       )
      )
    }
    val df_Aggregate_1_1 =
      Aggregate_1_1(context, df_RowDistributor_1_1_out0).interim(
        "Subgraph_1",
        "40x82-YyIIUk7pIhht2LX$$8yJkJueK979QEPVDHFvgb",
        "JSwGY5d6RoYVcwEbme7Hq$$Xr3S2P23gjlnFDsAXufsV"
      )
    val df_FlattenSchema_1_1 =
      FlattenSchema_1_1(context, df_Aggregate_1_1).interim(
        "Subgraph_1",
        "7dSYHS4ccxtaDQIA58yGB$$x1JPMGf3yMJMuUY-OtwTj",
        "1TNe7-gys_ySzJscz90bs$$1W_NSsAGQ3sQzB3HSPyUT"
      )
    val df_Deduplicate_1_1 = Deduplicate_1_1(context, in1).interim(
      "Subgraph_1",
      "6ITI0NEHkk-C0PzFrl3JB$$p_Z7wcOOGKMzNW64WS5Yg",
      "djg3J1fGmwlsK4U4kIhZ1$$0ThxktF-pSMtu_4DMAcfd"
    )
    val df_Reformat_7 = Reformat_7(context, in2).interim(
      "Subgraph_1",
      "rTy83DSuASMaEv6ATwCpc$$dttyOhfR4nO_qSOMdCqCz",
      "5LiZljahU3bU_Rym0A-1p$$lIDKZ9FK_jl1Oj5RPFlym"
    )
    df_Reformat_7.cache().count()
    df_Reformat_7.unpersist()
    val df_Reformat_1_1 =
      Reformat_1_1(context, df_src_csv_all_type_no_partition_1).interim(
        "Subgraph_1",
        "WwV8YcgqfDbTr1Qjw-_ub$$Dw-4lZfpoefk0R5ggK4qG",
        "y-_P0LZWdJ6sodhEZaaQ6$$dPOnqY1Y97r_ei9Me6RL9"
      )
    df_Reformat_1_1.cache().count()
    df_Reformat_1_1.unpersist()
    val df_Script_1_1 = Script_1_1(context, df_Deduplicate_1_1).interim(
      "Subgraph_1",
      "NhC1SRdJyLJ_imHbm-SGU$$URpoDRge_ARFYdNdru4wC",
      "cix9b7hiz5GT6SHK1a2ey$$S8rzxLcxjI0nNLR_s8oJR"
    )
    val df_recursive_1 = recursive_1.apply(context, df_Script_1_1)
    val df_OrderBy_2_1 =
      OrderBy_2_1(context, df_RowDistributor_1_1_out1).interim(
        "Subgraph_1",
        "Q732qOBLhcrT2x0MvHU_E$$AEToO4N74P5-TOd_6oR04",
        "Nljh_h-Q4z_oo_ltnGgSe$$edoA0-3hDqz_Mb6MIj27r"
      )
    (df_FlattenSchema_1_1, df_OrderBy_2_1, df_recursive_1)
  }

}
