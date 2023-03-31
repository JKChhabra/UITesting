from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from . import *
from .config import *

def all_type_main_1(
        spark: SparkSession,
        config: SubgraphConfig,
        in0: DataFrame,
        in1: DataFrame,
        in2: DataFrame
) -> (DataFrame, DataFrame, DataFrame):
    Config.update(config)
    df_Source_1_1_1 = Source_1_1_1(spark)
    df_Source_1_1_1 = collectMetrics(
        spark, 
        df_Source_1_1_1, 
        "all_type_main_1", 
        "1r_pZPVR3jKgUYztuH7tP$$GYroKPMlkJ38F-IYBss09", 
        "vrGooAVxXtbCLM9W-fF9T$$VhFn_-QUHy-2uElldpNfs"
    )
    df_Reformat_1_1_1 = Reformat_1_1_1(spark, df_Source_1_1_1)
    df_Reformat_1_1_1 = collectMetrics(
        spark, 
        df_Reformat_1_1_1, 
        "all_type_main_1", 
        "Rs1_2W86Fz2uEOx4rSPuK$$x057wMSZcqwSMQFw0szw4", 
        "Xh7JXB8u5rtXUDlUQrCoh$$kIk8ZTls5ACmeX3IhkI0G"
    )
    df_Reformat_2_1_1 = Reformat_2_1_1(spark, in0)
    df_Reformat_2_1_1 = collectMetrics(
        spark, 
        df_Reformat_2_1_1, 
        "all_type_main_1", 
        "QTebrQxcnMAv36Nrl63HZ$$rSWfqiIn-psnYowZTNbBF", 
        "7nZx0CC34uTUy4PtEZymC$$6YONRNAXgtB2LQoP0CjRx"
    )
    df_Join_1_1 = Join_1_1(spark, df_Reformat_1_1_1, df_Reformat_2_1_1)
    df_Join_1_1 = collectMetrics(
        spark, 
        df_Join_1_1, 
        "all_type_main_1", 
        "GbN9UX4QagmmdTDy5lRB7$$ibCOTkQEAONLpGqsKXUtb", 
        "O2iO5NU5HNEsmU520TNq_$$K37LD2kt599lPeCD3M7IB"
    )
    df_Limit_1_1_1 = Limit_1_1_1(spark, df_Join_1_1)
    df_Limit_1_1_1 = collectMetrics(
        spark, 
        df_Limit_1_1_1, 
        "all_type_main_1", 
        "gyHkhltV014QeqsokWIIQ$$G2k815QHOBa4X0lvX07zM", 
        "4C61I3tvKmt_X8E29ZH6k$$nXLxRsVI0W8CANQoQfUm1"
    )
    df_Filter_1_1_1 = Filter_1_1_1(spark, df_Limit_1_1_1)
    df_Filter_1_1_1 = collectMetrics(
        spark, 
        df_Filter_1_1_1, 
        "all_type_main_1", 
        "C24ulF5fayEDM8juBsH4j$$m3uuILWiGMO7WcaYshxjf", 
        "2rUoefG1Q0m10sbPniEa3$$-A3JVMKXKNaYIeiZo7EVF"
    )
    df_OrderBy_1_1_1 = OrderBy_1_1_1(spark, df_Filter_1_1_1)
    df_OrderBy_1_1_1 = collectMetrics(
        spark, 
        df_OrderBy_1_1_1, 
        "all_type_main_1", 
        "FdMdMKA9PwdDzQISgBmgv$$O0xBYK7Gqm9WW_hBm5CFE", 
        "1BzY1nnb-9FJ1TEI9BHBg$$YVPFYr-vqM3Yjc9Nl3iCB"
    )
    df_Aggregate_1_1_1 = Aggregate_1_1_1(spark, df_OrderBy_1_1_1)
    df_Aggregate_1_1_1 = collectMetrics(
        spark, 
        df_Aggregate_1_1_1, 
        "all_type_main_1", 
        "OfT5Aq5SMdAyz3OV3xklC$$kQfLqkXg-QImKOpWxygTj", 
        "Ku_NG7h8pJiUsIeAGbt56$$bShut_boNTX2C2_TyFABu"
    )
    df_Reformat_8_1_1 = Reformat_8_1_1(spark, in1)
    df_Reformat_8_1_1 = collectMetrics(
        spark, 
        df_Reformat_8_1_1, 
        "all_type_main_1", 
        "YHIfTUaSlFVhJPOGJROKe$$4RMKPqflXXdUEv-hrpjnR", 
        "6SGK1kGgLTQ8zVbOGEyZA$$USSlTwQmyXCY7XRFRWTFT"
    )
    df_Limit_3_1_1 = Limit_3_1_1(spark, df_Reformat_8_1_1)
    df_Limit_3_1_1 = collectMetrics(
        spark, 
        df_Limit_3_1_1, 
        "all_type_main_1", 
        "upAb93zRvQLP1GxdWLDac$$frkOGQOnfeQV8S4OzEEA6", 
        "IE05rCO7oJ17bB-lvwoQJ$$61vD-1i4UwXMQRLmIZE6x"
    )
    df_SchemaTransform_1_1_1 = SchemaTransform_1_1_1(spark, df_Aggregate_1_1_1)
    df_SchemaTransform_1_1_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1_1_1, 
        "all_type_main_1", 
        "iG8957kdxSmfu07RUwfoB$$DtUijJcuHZp86LSplKZe-", 
        "rVo0A5cms8UV5uQLRNcWw$$e9cvf-IpFVR0ntj6qRDr3"
    )
    df_Deduplicate_1_1_1 = Deduplicate_1_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_1_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_1_1_1, 
        "all_type_main_1", 
        "uwaoDWL2HnqS9obV8tUjF$$8t4EHvndW0k1IFjvJKLln", 
        "8X76Tt1F5v5IHcr3p28Ft$$Ie14jkmxv5QrbPIvPvyol"
    )
    df_Deduplicate_2_1_1 = Deduplicate_2_1_1(spark, df_SchemaTransform_1_1_1)
    df_Deduplicate_2_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_2_1_1, 
        "all_type_main_1", 
        "kVRevUdYnj2gVUfwaaQnS$$ZYP-0DrclFaQSX2Ie1wy2", 
        "C7pDD_QjctbPnqOzEhe_J$$2EGW-Cyfn8Q3WAfVa1nwn"
    )
    df_SetOperation_1_1_1 = SetOperation_1_1_1(spark, df_Deduplicate_1_1_1, df_Deduplicate_2_1_1)
    df_SetOperation_1_1_1 = collectMetrics(
        spark, 
        df_SetOperation_1_1_1, 
        "all_type_main_1", 
        "c2RCqWeCFSP45FFtbXtg6$$JWDtUKRSA3Od33yTm5Jy-", 
        "DzE6skFt4WEu_h2op_uU-$$-hJTHzYXUGLG2pp_vctHj"
    )
    df_WindowFunction_1_1_1 = WindowFunction_1_1_1(spark, df_SetOperation_1_1_1)
    df_WindowFunction_1_1_1 = collectMetrics(
        spark, 
        df_WindowFunction_1_1_1, 
        "all_type_main_1", 
        "tnoOANcn_jdGbTDqenzaf$$gX5kcd0KOt-DFplQtzz-R", 
        "AQxmVdWuNbRGwuPyaRGNp$$4mARQO4hEyOrFz9exMaWd"
    )
    df_Script_1_1_1 = Script_1_1_1(spark, df_WindowFunction_1_1_1)
    df_Script_1_1_1 = collectMetrics(
        spark, 
        df_Script_1_1_1, 
        "all_type_main_1", 
        "kDtlPVKdWUQf_7XY6ifv3$$PbrJpzcBYZW0oj0Ocpw_p", 
        "yfDfY5NcG_9ODRyxLBvMF$$MOgFNUlhv5gqByleOml6F"
    )
    df_Repartition_1_1_1 = Repartition_1_1_1(spark, df_Limit_1_1_1)
    df_Repartition_1_1_1 = collectMetrics(
        spark, 
        df_Repartition_1_1_1, 
        "all_type_main_1", 
        "HWz_Oa6ZdW5o0Gi_49u-c$$sPPAxrRFgEmLPd__RwNzw", 
        "o_Bf30uwcijDr4Mqg9J5Q$$yNujZdtnfRKDZ7FlNvaLh"
    )
    df_RowDistributor_1_1_1_out0, df_RowDistributor_1_1_1_out1 = RowDistributor_1_1_1(spark, df_Repartition_1_1_1)
    df_RowDistributor_1_1_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out0, 
        "all_type_main_1", 
        "Luy_AH7IaKcLQoR8ro4Sf$$FFjSQnS3EothkxsCQ4MxX", 
        "1E2PiLjmHUqLynLaEnyCk$$A27nuAlED42F_h42jTmXT"
    )
    df_RowDistributor_1_1_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_1_1_out1, 
        "all_type_main_1", 
        "Luy_AH7IaKcLQoR8ro4Sf$$FFjSQnS3EothkxsCQ4MxX", 
        "1EwHOqiPZ72rR68y-KeiG$$dHu6_aIk5yY-zXn8AksdP"
    )
    df_Subgraph_4_1_1 = Subgraph_4_1_1(
        spark, 
        config.Subgraph_4_1_1, 
        df_RowDistributor_1_1_1_out0, 
        df_RowDistributor_1_1_1_out1, 
        df_Script_1_1_1
    )
    df_OrderBy_3_1_1 = OrderBy_3_1_1(spark, in2)
    df_OrderBy_3_1_1 = collectMetrics(
        spark, 
        df_OrderBy_3_1_1, 
        "all_type_main_1", 
        "N_q0oNs6I9Th86QzopXq3$$6lwzpPjFFgt60Y0dCUjIG", 
        "KAU9vWbd6bQb3HTGkuzZB$$-3hS_3OE5gBtkDsakG9fO"
    )
    df_Deduplicate_3_1_1 = Deduplicate_3_1_1(spark, df_OrderBy_3_1_1)
    df_Deduplicate_3_1_1 = collectMetrics(
        spark, 
        df_Deduplicate_3_1_1, 
        "all_type_main_1", 
        "-Nrb7QUp1eCEqz0AyZHzO$$EcHYpHAKbvBkshrAvIkaQ", 
        "LcvMPPnxzPBzC6QZPp_KJ$$CFEYSWyzRpkv8WZ2CDAot"
    )

    return df_Subgraph_4_1_1, df_Limit_3_1_1, df_Deduplicate_3_1_1
