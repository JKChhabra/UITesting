package org.main.scla_dep_mgmt_change

import io.prophecy.libs._
import org.main.scla_dep_mgmt_change.config.Context
import org.main.scla_dep_mgmt_change.config._
import org.main.scla_dep_mgmt_change.config.ConfigStore.interimOutput
import org.main.scla_dep_mgmt_change.udfs.UDFs._
import org.main.scla_dep_mgmt_change.udfs._
import org.main.scla_dep_mgmt_change.graph._
import org.main.scla_dep_mgmt_change.graph.SubGraph_1
import org.main.scla_dep_mgmt_change.graph.all_type_scala_sg_1
import org.main.scla_dep_mgmt_change.graph.Subgraph_2
import org.main.scla_dep_mgmt_change.graph.SubGraph_1.config.{
  Context => SubGraph_1_Context
}
import org.main.scla_dep_mgmt_change.graph.all_type_scala_sg_1.config.{
  Context => all_type_scala_sg_1_Context
}
import org.main.scla_dep_mgmt_change.graph.Subgraph_2.config.{
  Context => Subgraph_2_Context
}
import org.apache.spark._
import org.apache.spark.sql._
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._
import org.apache.spark.sql.expressions._
import java.time._

object Main {

  def graph(context: Context): Unit = {
    val df_src_parquet_all_type_and_partition_withspacehyphens =
      src_parquet_all_type_and_partition_withspacehyphens(context).interim(
        "graph",
        "4c8lUyCOBMQXJt_5f7dbP$$hbMC_bA0Uq2x2q8FW4tAX",
        "pIPX9BUJ7XgmTvGgmV8Hu$$y6Sz1JeyfULGcGgi8slvs"
      )
    Lookup_2(context, df_src_parquet_all_type_and_partition_withspacehyphens)
    val df_src_avro_CustsDatasetInput_1 = src_avro_CustsDatasetInput_1(context)
      .interim("graph", "A7YBjCffwys4LPAleAKpC", "bsEyEzvvLYNF6CFSyeX9o")
    Lookup_1(context,   df_src_avro_CustsDatasetInput_1)
    val df_Reformat_4 =
      Reformat_4(context,
                 df_src_parquet_all_type_and_partition_withspacehyphens
      ).interim("graph",
                "QA8k3yf3NHL4Dj0WAvlcE$$6k8gyMJ_bK4ZvWD-WkPiK",
                "5857bxTW7G9sQZ8dVJJEf$$p25_pviQ-HeuDuRAg5Sv_"
      )
    df_Reformat_4.cache().count()
    df_Reformat_4.unpersist()
    val df_src_orc_all_type_no_partition = src_orc_all_type_no_partition(
      context
    ).interim("graph", "xoDRuSduB1niuIF8PP3ct", "AJqWz1Up0SmtM70ipV65i")
    val df_FlattenSchema_1 =
      FlattenSchema_1(context, df_src_orc_all_type_no_partition)
        .interim("graph",
                 "Szohjp1gWxHYvFe2IrcM0$$UyKRJZMAGITZk2c-3nrry",
                 "y0ljFftVNLexQytwgRtZe$$gCrSp9s-cpbqRZaLKOGRd"
        )
        .cache()
    val df_Script_1 =
      Script_1(context, df_src_avro_CustsDatasetInput_1).interim(
        "graph",
        "zvL4eQufcf7JXDWE5naBz$$FaOjEEhgZ-ohY-GFzOtkz",
        "zvrtFJPhpuoVXq8RQ6UgB$$oj1NDu1sKgKz7Ldy31y9n"
      )
    val df_call_func = call_func(context, df_Script_1).interim(
      "graph",
      "jDGCmYurLPi5p2PI0NGES$$ppPGE4WaX6-Zibw1VKZeH",
      "kcQDaPwg6yVi98DcYU8IQ$$IoQqIwKAkSnY95_gSy2rx"
    )
    df_call_func.cache().count()
    df_call_func.unpersist()
    val df_WindowFunction_1 =
      WindowFunction_1(context,
                       df_src_parquet_all_type_and_partition_withspacehyphens
      ).interim("graph",
                "kHjXzB0HTJD1XTuwrj5kw$$ufL5LdEj0VdfG7-f1lHjQ",
                "Xh1IgHG5x-W2wGzFMUf9N$$f3xyINARrBYxOtt8dLXCx"
      )
    val df_Deduplicate_1 = Deduplicate_1(context, df_WindowFunction_1).interim(
      "graph",
      "vpuiPUloPPI5wKsdnBW2X$$9hYAzmyJqyva6xBUJQas7",
      "OcRhKi5A8GbNRmjSJ_cwb$$AAP0iEMiVDg3mvHXC8Y01"
    )
    val df_src_json_input_custs_1 = src_json_input_custs_1(context)
      .interim("graph", "XM4cdlXB7oVFseHwX2LRg", "gB7zngP2OXebTsbxfm4vF")
      .cache()
    val df_Deduplicate_2 = Deduplicate_2(context, df_FlattenSchema_1).interim(
      "graph",
      "faSnoqDMQPRk7kfregn3H$$ZKCAqB4L-lusn5xKNicMr",
      "FI1jEKVQ6bkCmPl3ojML-$$3tJdDF9N0cONpOP-Xu-2l"
    )
    val df_SubGraph_1 = SubGraph_1.apply(
      SubGraph_1_Context(context.spark, context.config.SubGraph_1),
      df_Deduplicate_2
    )
    val df_Script_12_1 = Script_12_1(context).interim(
      "graph",
      "nCrxuIc-Tmk2bb4CAzQ-b$$bYGtrcauW3HQdrz0rLJL8",
      "1Jpk8w_P0a_pf6wOk9qKI$$aFkzeiGkLZCdjHNwXAVbB"
    )
    val df_Script_12 = Script_12(context).interim(
      "graph",
      "RRao6fAtV9-bAAcIFHpVK$$5yft7FAPiRWuBceDEF0bo",
      "uoV-RBmBiYuGFovNAtDuJ$$0RRSxS_c9dq1385Q4pb4T"
    )
    val df_Script_3 = Script_3(context, df_Script_12).interim(
      "graph",
      "cSJj7NsQRs7_Uk5ojQzBh$$fUpC3VSO1thAtLBI1b43U",
      "NC2h6HtrgC3YA6w3xXUyN$$WDmvH8kAsS3pLUNRVkcqd"
    )
    val df_Script_7 = Script_7(context, df_Script_3).interim(
      "graph",
      "IwIKwcRg959Ki1d-igYP2$$Czi6jKwfFIDDqv8nqlhEf",
      "91MBOyLmS9gSomZqNFDrb$$S2C2OJvbbLO4HrNpJR5ub"
    )
    val df_Script_8 = Script_8(context, df_Script_7)
      .interim("graph",
               "kjm6cQJLBQ7If2meAD1CY$$DPNGtLdU3Jc8CmZXCYvMh",
               "p6tB4A_Qo8pcYbrr9KwOZ$$59JxpTAUw5ISzCVua2GE5"
      )
      .cache()
    val (df_Script_9_out0, df_Script_9_out1, df_Script_9_out2) = {
      val (df_Script_9_out0_temp,
           df_Script_9_out1_temp,
           df_Script_9_out2_temp
      ) = Script_9(context, df_Script_12_1, df_Script_8)
      (df_Script_9_out0_temp.interim(
         "graph",
         "PvlsRiVwRhRzBwXppuR5F$$F5qjPdQS9Bhw0sTvPJYdS",
         "eIfQ2xQxKvhTrUBJ8bi3R$$_Sl7quLnKhmAjqKmXFnrS"
       ),
       df_Script_9_out1_temp.interim(
         "graph",
         "PvlsRiVwRhRzBwXppuR5F$$F5qjPdQS9Bhw0sTvPJYdS",
         "wlS8lQQWy8co_GFEynXjc$$ilwDip5ONP3QoEsoMu248"
       ),
       df_Script_9_out2_temp.interim(
         "graph",
         "PvlsRiVwRhRzBwXppuR5F$$F5qjPdQS9Bhw0sTvPJYdS",
         "Lo6MjOg15j8TkyAtHqbcN$$eOKgM8m7INFfudQQ_vlm_"
       )
      )
    }
    val df_Script_10 = Script_10(context, df_Script_9_out1).interim(
      "graph",
      "95FDNhx9IiEJ0aROYHlwR$$EbhnAT4iXEz-NIvjDN4yV",
      "wrtyAizwYRmMFppyE1CRC$$pCYf5aATA149gvn85_Lzd"
    )
    val df_Script_11 = Script_11(context, df_Script_10).interim(
      "graph",
      "8WRlIwKnB4PSJfaF8HPps$$IdWBJMb2YtxfW4Z6rbS6s",
      "QbEchblewqOHmci2XbdX8$$9iukH3VA35ffZsOBtaT1S"
    )
    val df_Script_13 = Script_13(context, df_Script_11).interim(
      "graph",
      "hoqNQQo5U08Fy5vFOLVI6$$HeKUyd2atKXo2USe5rNkm",
      "D0f72MZW9_HT0wgpV2csR$$wxK-Q7bqih0GE4BnKrPG_"
    )
    val df_Script_14 = Script_14(context, df_Script_13).interim(
      "graph",
      "qR575SPk95eqGZRpFgO_-$$ZzAVSXrsuOOWWNfhNYt4i",
      "2am6ZPyMauc452EwukpzK$$glet8bJxhBcERqM6gXAYj"
    )
    val df_Repartition_2 = Repartition_2(context, df_WindowFunction_1).interim(
      "graph",
      "yfeifaX7xpRlj28Ls-8Vf$$29PiihbU95u1gXWccO3GA",
      "xIA_sDLdYIaSR9jB4VXlg$$Rv5ZSnqWe9vse2SDVvmu_"
    )
    val df_Repartition_3 = Repartition_3(context, df_Repartition_2).interim(
      "graph",
      "COz-6QYHVMxEsZK7xgFjO$$s6pqEnlwUcNFDVBX2NtnT",
      "VE-plh40cOeg9G005TysE$$b0LQzqSl6POGMQ4j4vs3c"
    )
    df_Repartition_3.cache().count()
    df_Repartition_3.unpersist()
    val df_src_csv_special_char_column_name = src_csv_special_char_column_name(
      context
    ).interim("graph", "nEj64p7qzVS7z0LXXTFkx", "2G70-QEVG04zcV_iAsqv1").cache()
    val df_Limit_1 = Limit_1(context, df_src_csv_special_char_column_name)
      .interim("graph", "BtjgWEFk-IrCWsqN3RqDF", "vz8yOBdktTG02eFYUsCr_")
    val df_Filter_1 = Filter_1(context, df_src_csv_special_char_column_name)
      .interim("graph", "gNCO_k3OESC15dRefnTjD", "7ecj16KrYrMc5jCMOyV_-")
    val df_UTGenOrderBy_1 = UTGenOrderBy_1(context,
                                           df_src_csv_special_char_column_name
    ).interim("graph", "hxZRArGTe6IeA715uZ9hX", "NGuAUZuZAsYsYcFmYLp2B")
    val df_Script_2 =
      Script_2(context, df_Limit_1, df_Filter_1, df_UTGenOrderBy_1).interim(
        "graph",
        "K4iDT2F4Oyo-07xFirqRU$$MOT_KJUj7svHsQ2Omum0F",
        "_XsdFTaDIQf4LRvqNufg4$$4S0LETMYftOF473uP_5ql"
      )
    val df_src_parquet_all_type_no_partition =
      src_parquet_all_type_no_partition(context)
        .interim("graph", "PM7sxRmKo0cGk1IYdBNtT", "zMejsXna2UN-uClx0tfKO")
        .cache()
    val df_ComplexExpression = ComplexExpression(
      context,
      df_src_parquet_all_type_no_partition
    ).interim("graph", "2tRCXGkA-6TfjEnFofIJq", "MwSfNu4URv3g0PC7kc9CR")
    val df_src_unittest_parquet_all = src_unittest_parquet_all(context).interim(
      "graph",
      "ASVQUSGemiDjwc6M_V35W$$dFto0bYXNQ_A7n3kGM0jR",
      "U-eeoR9aJ66XXBnbWbzyj$$K894Ue9hU76yLTlb2svbu"
    )
    val df_OrderBy_3 = OrderBy_3(context, df_ComplexExpression).interim(
      "graph",
      "hx5wO_87IAH8xNU8kd6u0$$NZNcKwMNB77oH_rUMhHw2",
      "3QwZLdav6axGl_0dxx9N_$$CvmPmUKZnuBwQ1mj-VrK0"
    )
    val df_Script_6 = Script_6(
      context,
      df_src_avro_CustsDatasetInput_1,
      df_src_avro_CustsDatasetInput_1,
      df_src_avro_CustsDatasetInput_1,
      df_src_json_input_custs_1,
      df_src_json_input_custs_1,
      df_src_json_input_custs_1
    ).interim("graph",
              "OV4umnU64FY8jeq073S6y$$_8eUIqYY7dzwH32AVBmMj",
              "tHwwGYZqVPaRNUPEYJupG$$R-CX6OC_mKEtBWa5RkLHr"
    )
    val (df_all_type_scala_sg_1_out0,
         df_all_type_scala_sg_1_out1,
         df_all_type_scala_sg_1_out2
    ) = {
      val (df_all_type_scala_sg_1_out0_temp,
           df_all_type_scala_sg_1_out1_temp,
           df_all_type_scala_sg_1_out2_temp
      ) = all_type_scala_sg_1.apply(
        all_type_scala_sg_1_Context(context.spark,
                                    context.config.all_type_scala_sg_1
        ),
        df_src_parquet_all_type_and_partition_withspacehyphens,
        df_src_parquet_all_type_and_partition_withspacehyphens,
        df_src_parquet_all_type_and_partition_withspacehyphens
      )
      (df_all_type_scala_sg_1_out0_temp,
       df_all_type_scala_sg_1_out1_temp,
       df_all_type_scala_sg_1_out2_temp
      )
    }
    val df_Script_15 = Script_15(context, df_Script_14).interim(
      "graph",
      "ZbJiBS9TZN49FNNkUOde-$$76e2_QoDYL40xpmXMFgzb",
      "qgd-YjqsT9bTYhd-wc9uO$$p4YmWwBim-w-DBX5ZtnbN"
    )
    df_Script_15.cache().count()
    df_Script_15.unpersist()
    val (df_RowDistributor_1_out0, df_RowDistributor_1_out1) = {
      val (df_RowDistributor_1_out0_temp, df_RowDistributor_1_out1_temp) =
        RowDistributor_1(context, df_Deduplicate_1)
      (df_RowDistributor_1_out0_temp.interim(
         "graph",
         "mxj3GIDr8L_wSjsWZxCzw$$ly00a3LzUT_45X1UWdYHu",
         "out0"
       ),
       df_RowDistributor_1_out1_temp.interim(
         "graph",
         "mxj3GIDr8L_wSjsWZxCzw$$ly00a3LzUT_45X1UWdYHu",
         "out1"
       )
      )
    }
    val df_OrderBy_4 = OrderBy_4(context, df_RowDistributor_1_out0).interim(
      "graph",
      "hWAQiNOptWzlVEkn-huuJ$$q-JVLZQnREXaW_I25BSj5",
      "Z4XurMdUJO-ETinTrSyh6$$CxMPDJXpvul_WH8wvOY5y"
    )
    val df_Script_5 = Script_5(context, df_all_type_scala_sg_1_out0).interim(
      "graph",
      "-1sF51qSXmJKE9XJXPJ8W$$_c2ggE1nZMrpb8USN1LhB",
      "rmzP7Y-i4QV7gVAmbc_Zj$$C30YN2Ip6C7uzw0o94s3c"
    )
    df_Script_5.cache().count()
    df_Script_5.unpersist()
    val df_Limit_3 = Limit_3(context, df_RowDistributor_1_out1).interim(
      "graph",
      "Fveo5Vzi24BOiUGy55PZU$$9-p9OnU3R-r06567Tejez",
      "Ft6cGNpKOE2Nirw_XS9_R$$Cd22cRsabCIorU61swO2N"
    )
    val df_ConfigAndUDF = ConfigAndUDF(context, df_Script_1).interim(
      "graph",
      "ryf6nWZatrJJgaQGDWPjC",
      "bY6dBUB7OHy6i8vc1uwbD"
    )
    val df_Filter_2 = Filter_2(context, df_ConfigAndUDF).interim(
      "graph",
      "F_cxTDso7G28ruB0xni7N",
      "V_c7nCHezVT96rpb-8TzQ"
    )
    val df_OrderBy_2 = OrderBy_2(context, df_Filter_2).interim(
      "graph",
      "0BEbuoCU7vasdz7Wr3Ft1",
      "1DyiAt45y3SZCoDDCNVmw"
    )
    df_OrderBy_2.cache().count()
    df_OrderBy_2.unpersist()
    val df_Join_1 = Join_1(context,
                           df_src_csv_special_char_column_name,
                           df_src_csv_special_char_column_name
    ).interim("graph", "s6VHxJpslzbkbawETR2P-", "Vgk6IkOJ1X4GCgsQt0iEM")
    val df_Filter_3 = Filter_3(context, df_Join_1).interim(
      "graph",
      "ABXvUNM6audpzrMLv5LDr$$gN9X6f19SCw8Y7mEDLIgk",
      "-iLcTHeyPi06v3tqrYjBU$$7s_wmQnvqOe_tiBl8SbF_"
    )
    val df_Script_17 = Script_17(context, df_Script_9_out2).interim(
      "graph",
      "rk2vOthe2UTH1jROrvhxi$$rOTXHJiN102NYZhbuSHuA",
      "7dTdVfYtspgO4ia2svYSb$$jEgNfKpZfXqaQS_VXcAVk"
    )
    df_Script_17.cache().count()
    df_Script_17.unpersist()
    val df_Filter_6 = Filter_6(context, df_Script_6).interim(
      "graph",
      "6RHwsPMshmxqxqLVwxaAf$$qAPCAUOs1yMDoJzt6V2Ho",
      "VNyLn1sWT73jgMQlRni-X$$WRUzyI7gGT6gKhQbB7KaU"
    )
    val df_SetOperation_2 =
      SetOperation_2(context, df_Script_6, df_Filter_6).interim(
        "graph",
        "0D6KA6M69NaxwLh4YHL36$$DBCL7Ij7iKu5Ru7REo8Ff",
        "bal6pUnNminCP0rLQ_Bd9$$r3-2j5Z8_uku45wIZ-gY9"
      )
    val df_Aggregate_1 = Aggregate_1(context, df_OrderBy_3).interim(
      "graph",
      "n0VmJXrJcJhCDBbma0KdJ$$k94j1JSMRlVwaZ6r7RhGb",
      "Q5r1wB6YPEzdTGEVZN4dU$$Z-m7r-v8lekG4XOCQmIO2"
    )
    val (df_SQLStatement_1_out,
         df_SQLStatement_1_out1,
         df_SQLStatement_1_out2
    ) = {
      val (df_SQLStatement_1_out_temp,
           df_SQLStatement_1_out1_temp,
           df_SQLStatement_1_out2_temp
      ) =
        SQLStatement_1(context, df_Aggregate_1, df_Aggregate_1, df_Aggregate_1)
      (df_SQLStatement_1_out_temp.interim(
         "graph",
         "azjqEoM7Qc0DPek_wQxSJ$$nfc8jjh6tJ-azZxb5MxeI",
         "mJUUEuSZ4lWJ2E9rBt8sT$$nKUg8F3PmIbt1crEIYC8o"
       ),
       df_SQLStatement_1_out1_temp.interim(
         "graph",
         "azjqEoM7Qc0DPek_wQxSJ$$nfc8jjh6tJ-azZxb5MxeI",
         "bRcVgEd4wZ_Z5H6Avo0V1$$BjoiTeZgWcQIL3i5UbLP5"
       ),
       df_SQLStatement_1_out2_temp.interim(
         "graph",
         "azjqEoM7Qc0DPek_wQxSJ$$nfc8jjh6tJ-azZxb5MxeI",
         "iCDpy1CVEYIZTX27QQUGW$$mIbXM1H7DYzH9AxP3jIYL"
       )
      )
    }
    df_SQLStatement_1_out2.cache().count()
    df_SQLStatement_1_out2.unpersist()
    val df_Filter_4 = Filter_4(context, df_SQLStatement_1_out1).interim(
      "graph",
      "ciWzfAl9aodUAUcxhIsRU$$FUfG9VfSP7fv8ycEGTlrM",
      "IWrjh8haSj1CB9Wk6h9AR$$l8AFjzZT0OU-Jv2Lc_VOR"
    )
    val df_Script_16 = Script_16(context, df_Script_9_out0).interim(
      "graph",
      "9nWzQRJJA5t5wjl3ercNJ$$5yZEgZZ8xb6xoNauyiNFY",
      "hF5lafO74RNjM137_3FzV$$Lj6SLpr_G3TWQZUpeoINF"
    )
    df_Script_16.cache().count()
    df_Script_16.unpersist()
    val df_src_jdbc_dbsecrets_test_table =
      src_jdbc_dbsecrets_test_table(context).interim(
        "graph",
        "FMl2GuBQkrf6_L2-1_mJj$$StZaODbsxnN9fIdLwaO0z",
        "SmN3D2QHD52ep_LvBEm_y$$7ZYjSWohGfpYZvd31RArp"
      )
    withSubgraphName("graph", context.spark) {
      withTargetId("dest_jdbc_userandpass_test_table", context.spark) {
        dest_jdbc_userandpass_test_table(context,
                                         df_src_jdbc_dbsecrets_test_table
        )
      }
    }
    val df_UTGenRepartition_1 = UTGenRepartition_1(
      context,
      df_src_csv_special_char_column_name
    ).interim("graph", "JDdGnXnYzeiw8aXJ5gB5q", "sNPPOS1ix-ZWOvC-Q0cPD")
    df_UTGenRepartition_1.cache().count()
    df_UTGenRepartition_1.unpersist()
    val df_src_delta_all_type_no_partition = src_delta_all_type_no_partition(
      context
    ).interim("graph", "Fmg6g-ViOm77hFxIpAPch", "ee0X8XILMHhyMro4U1_V7")
    val df_src_catalog_table_test_catalog_source =
      src_catalog_table_test_catalog_source(context).interim(
        "graph",
        "vmRKV0Nd6-lh2PBG9DCyM$$r1IXlDV-WCE_ANbMUvQcs",
        "RiRMBmFnYhsz_jKLJYl4P$$UkVrz2ppXuwUgrdRSOXCa"
      )
    val df_Reformat_2 =
      Reformat_2(context, df_src_catalog_table_test_catalog_source).interim(
        "graph",
        "6Znk7A4h43eh2eyod9GFr$$FUM5E0P9Xrn_WDFN9qFVz",
        "r0a543LnVEGLj4EiHP7P0$$F6WweoNFKHeQEZHINdKwA"
      )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()
    val df_SetOperation_2_1 =
      SetOperation_2_1(context, df_SetOperation_2, df_SetOperation_2).interim(
        "graph",
        "oBvXdYTA5tBj61w6P7m-9$$PW6Ikm92ofDdAGVfMvL_m",
        "TE4HOZUCVuefZj5jvGqDR$$AT2IGIqwYHf-R6lTUfBkJ"
      )
    df_SetOperation_2_1.cache().count()
    df_SetOperation_2_1.unpersist()
    val df_Reformat_5 = Reformat_5(context, df_Aggregate_1).interim(
      "graph",
      "ZohJ-uI1fzL3XQKSP_Umt$$4GCMZbeofo2GO4U1MPXs6",
      "F5wuTXsiXBnYYKYOJ4870$$M0xPxSk9xE2BT2wb6Va5r"
    )
    val df_Filter_5 = Filter_5(context, df_Reformat_5).interim(
      "graph",
      "IeVyvyMj40jBGOIg_RQiH$$JKL7hZbfQtkLCtw62jh3v",
      "u4GgmkkIhWUyZ8fAu8j6s$$hK0j23KHvKHzqt9nB9PWy"
    )
    df_Filter_5.cache().count()
    df_Filter_5.unpersist()
    val df_SchemaTransform_1 =
      SchemaTransform_1(context, df_SubGraph_1).interim(
        "graph",
        "X5J7daeiMxXXaSTwpkDu9$$bZ2O5xQ9NUIlbSkMbv1MY",
        "02JU61gNQIeeb7iKJc5Z5$$_IQVWieQ7Tfs3dWmwjS8M"
      )
    df_SchemaTransform_1.cache().count()
    df_SchemaTransform_1.unpersist()
    val df_SetOperation_1 = SetOperation_1(context,
                                           df_src_delta_all_type_no_partition,
                                           df_src_delta_all_type_no_partition
    ).interim("graph",
              "6MGeoO_3CAkDyZvPYAGOY$$W7ZInyQSxiNrP-XuCd9hK",
              "9nSC-MM8SEHYGTWCQwmW8$$82qHa1CcCeW1MGcYp5jb4"
    )
    val df_OrderBy_6 = OrderBy_6(context, df_SQLStatement_1_out).interim(
      "graph",
      "0RMNXYh8g4Ll-VyJr8jJR$$lsQ_tpR5ggnXVOArbueFm",
      "miS1YaOwxRQTAQ3ED1fZj$$nwRJzE6C20e8cOD03DZ0y"
    )
    val df_Reformat_8 = Reformat_8(context, df_Script_6).interim(
      "graph",
      "VojrEOLLM7nesHVbUffgG$$ujNbJd_Qe--3wvxRqPV3F",
      "USRNNEY4yPLG763IDrN7e$$ALfX5lz8yMMHXG3htDpVy"
    )
    val (df_Subgraph_2_out0,
         df_Subgraph_2_out1,
         df_Subgraph_2_out2,
         df_Subgraph_2_out3,
         df_Subgraph_2_out4,
         df_Subgraph_2_out5,
         df_Subgraph_2_out6,
         df_Subgraph_2_out7
    ) = {
      val (df_Subgraph_2_out0_temp,
           df_Subgraph_2_out1_temp,
           df_Subgraph_2_out2_temp,
           df_Subgraph_2_out3_temp,
           df_Subgraph_2_out4_temp,
           df_Subgraph_2_out5_temp,
           df_Subgraph_2_out6_temp,
           df_Subgraph_2_out7_temp
      ) = Subgraph_2.apply(
        Subgraph_2_Context(context.spark, context.config.Subgraph_2),
        df_Deduplicate_2,
        df_OrderBy_4,
        df_Limit_3,
        df_OrderBy_6,
        df_Filter_4,
        df_Script_2,
        df_Reformat_8,
        df_Filter_3
      )
      (df_Subgraph_2_out0_temp,
       df_Subgraph_2_out1_temp,
       df_Subgraph_2_out2_temp,
       df_Subgraph_2_out3_temp,
       df_Subgraph_2_out4_temp,
       df_Subgraph_2_out5_temp,
       df_Subgraph_2_out6_temp,
       df_Subgraph_2_out7_temp
      )
    }
    df_Subgraph_2_out0.cache().count()
    df_Subgraph_2_out0.unpersist()
    df_Subgraph_2_out1.cache().count()
    df_Subgraph_2_out1.unpersist()
    df_Subgraph_2_out2.cache().count()
    df_Subgraph_2_out2.unpersist()
    df_Subgraph_2_out3.cache().count()
    df_Subgraph_2_out3.unpersist()
    df_Subgraph_2_out4.cache().count()
    df_Subgraph_2_out4.unpersist()
    df_Subgraph_2_out5.cache().count()
    df_Subgraph_2_out5.unpersist()
    df_Subgraph_2_out6.cache().count()
    df_Subgraph_2_out6.unpersist()
    df_Subgraph_2_out7.cache().count()
    df_Subgraph_2_out7.unpersist()
    Script_4(context, df_SetOperation_1)
    val df_UTGenAllType =
      UTGenAllType(context, df_src_unittest_parquet_all).interim(
        "graph",
        "pKHRYS1hsbrGwDD8pGo75$$3oG41nwykeKi4E0wRs4tA",
        "0uOZZEovz1kGAC3K7yB_7$$SZHrPVYA60sLjrwDRHuoE"
      )
    df_UTGenAllType.cache().count()
    df_UTGenAllType.unpersist()
    val df_OrderBy_5 = OrderBy_5(context, df_all_type_scala_sg_1_out2).interim(
      "graph",
      "ob-z78F3IzAX2uhlQdAzt$$R5-sxgmSe6F4lNqqwQk1S",
      "BIK34FonH5y7wEs0h4s2W$$J9rMqqPWA4DXgpiaMTUGO"
    )
    df_OrderBy_5.cache().count()
    df_OrderBy_5.unpersist()
    val df_Reformat_1 =
      Reformat_1(context, df_all_type_scala_sg_1_out1).interim(
        "graph",
        "suL54pumFBm-vMC_7rPqj$$LnB0spZUTAA5qGaKWizGA",
        "2M0DrPW0rnsiTSzHVchx9$$a5mOBh06lRQYCfJ9cx0mW"
      )
    df_Reformat_1.cache().count()
    df_Reformat_1.unpersist()
    val df_UTGenReformat3 = UTGenReformat3(context,
                                           df_src_csv_special_char_column_name
    ).interim("graph", "5jhe2NMutKCmtfsWW03Dh", "SzVxzITqrWe5YCf4ZUe7t")
    df_UTGenReformat3.cache().count()
    df_UTGenReformat3.unpersist()
  }

  def main(args: Array[String]): Unit = {
    val config = ConfigurationFactoryImpl.fromCLI(args)
    val spark: SparkSession = SparkSession
      .builder()
      .appName("Prophecy Pipeline")
      .config("spark.default.parallelism",             "4")
      .config("spark.sql.legacy.allowUntypedScalaUDF", "true")
      .enableHiveSupport()
      .getOrCreate()
      .newSession()
    val context = Context(spark, config)
    MetricsCollector.initializeMetrics(spark)
    implicit val interimOutputConsole: InterimOutput = InterimOutputHive2("")
    spark.conf.set("prophecy.collect.basic.stats",          "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules",
                   "org.apache.spark.sql.catalyst.optimizer.ColumnPruning"
    )
    spark.conf.set("spark_config1",
                   "spark./<>;'\"[]{}\\|~*/-+p- config1 value !~_#@%^&*()-="
    )
    spark.conf.set("spark_config2",     "spark_config2_value")
    spark.conf.set("fs.s3a.access.key", "AKIAR6ESAR2JAQNZNVMH")
    spark.conf
      .set("fs.s3a.secret.key", "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")
    spark.conf
      .set("prophecy.metadata.pipeline.uri", "pipelines/SCALA_DEP_MGMT_ALL")
    spark.sparkContext.hadoopConfiguration.set(
      "hadoop_config1",
      "hadoop./<>;'\"[]{}\\|~*/-+p- config1 value !~_#@%^&*()-="
    )
    spark.sparkContext.hadoopConfiguration
      .set("hadoop_config2", "hadoop_config2_value")
    spark.sparkContext.hadoopConfiguration
      .set("fs.s3a.access.key", "AKIAR6ESAR2JAQNZNVMH")
    spark.sparkContext.hadoopConfiguration
      .set("fs.s3a.secret.key",   "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")
    MetricsCollector.start(spark, "pipelines/SCALA_DEP_MGMT_ALL")
    graph(context)
    MetricsCollector.end(spark)
  }

}
