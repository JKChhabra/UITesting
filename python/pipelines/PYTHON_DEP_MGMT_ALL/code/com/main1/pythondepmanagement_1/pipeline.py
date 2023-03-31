from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from com.main1.pythondepmanagement_1.config.ConfigStore import *
from com.main1.pythondepmanagement_1.udfs.UDFs import *
from prophecy.utils import *
from com.main1.pythondepmanagement_1.graph import *

def pipeline(spark: SparkSession) -> None:
    df_all_type_part_parquet = all_type_part_parquet(spark)
    df_all_type_part_parquet = collectMetrics(
        spark, 
        df_all_type_part_parquet, 
        "graph", 
        "4h71IOPBDFyzOnxjjfKPl$$8MhjH0PVU12ED2fJyDLpS", 
        "K1XpTR7-jgHPuX6PHVdPr$$wHEmbxozybFo-eRVP11a3"
    )
    df_RowDistributor_1_out0, df_RowDistributor_1_out1, df_RowDistributor_1_out2, df_RowDistributor_1_out3 = RowDistributor_1(
        spark, 
        df_all_type_part_parquet
    )
    df_RowDistributor_1_out0 = collectMetrics(
        spark, 
        df_RowDistributor_1_out0, 
        "graph", 
        "1SN-pEh_8DmEvfS9UhGNE$$64hDBTC35HIwIiZktE_Ld", 
        "out0"
    )
    df_RowDistributor_1_out1 = collectMetrics(
        spark, 
        df_RowDistributor_1_out1, 
        "graph", 
        "1SN-pEh_8DmEvfS9UhGNE$$64hDBTC35HIwIiZktE_Ld", 
        "W59iy89iTXSgFaxfQEwhW"
    )
    df_RowDistributor_1_out2 = collectMetrics(
        spark, 
        df_RowDistributor_1_out2, 
        "graph", 
        "1SN-pEh_8DmEvfS9UhGNE$$64hDBTC35HIwIiZktE_Ld", 
        "3a-JMPZZW4g-OIK6u8pOH"
    )
    df_RowDistributor_1_out3 = collectMetrics(
        spark, 
        df_RowDistributor_1_out3, 
        "graph", 
        "1SN-pEh_8DmEvfS9UhGNE$$64hDBTC35HIwIiZktE_Ld", 
        "CKp-fYcvwRV-xHIE140JV"
    )
    Lookup_1(spark, df_RowDistributor_1_out1)
    df_csv_special_chars = csv_special_chars(spark)
    df_csv_special_chars = collectMetrics(
        spark, 
        df_csv_special_chars, 
        "graph", 
        "zM4C2oFSMY1j4ofziFf9I$$R7DcTNFgSQS8aDiZv_xUz", 
        "ORTrvFWDCkxykwAXnkn1g$$fwpMbWEu626Vg01d_d77R"
    )
    df_Filter_1 = Filter_1(spark, df_csv_special_chars)
    df_Filter_1 = collectMetrics(
        spark, 
        df_Filter_1, 
        "graph", 
        "5_yNvqIFR0X3gtj0acpc5$$8lshGYMNKW7YDdFdn3a3i", 
        "2sVaJyYIOhDWczNzrH865$$EZP0zXynO1ZUGdxYXqVHn"
    )
    df_ConfigAndUDF = ConfigAndUDF(spark, df_Filter_1)
    df_ConfigAndUDF = collectMetrics(
        spark, 
        df_ConfigAndUDF, 
        "graph", 
        "3ZL3zn7QeM6Yhv-O1O3lw$$FDI6ABdUy6fCp3YqgF1Yv", 
        "0YDYZPDtmMHOdXMO3igze$$uzOCbwhK48a5yijnl6X1B"
    )
    df_OrderBy_1 = OrderBy_1(spark, df_ConfigAndUDF)
    df_OrderBy_1 = collectMetrics(
        spark, 
        df_OrderBy_1, 
        "graph", 
        "LuvCHinHtvzgUCBzLr99X$$C0IBWgHAMSE5ovVqtha7Q", 
        "XMZ9PL47KCK49bhwywt-X$$ApvHMBHWabBeZQaHanXfh"
    )
    df_Deduplicate_1 = Deduplicate_1(spark, df_OrderBy_1)
    df_Deduplicate_1 = collectMetrics(
        spark, 
        df_Deduplicate_1, 
        "graph", 
        "UrZUXs4Zb0DFJ2kliyvD0$$sjteqYHfJEoEm2HSzpcjE", 
        "x7W-pjW-6TjOG3oAscMiK$$3-swEthJhrqJivBfqlgl_"
    )
    df_SchemaTransform_1 = SchemaTransform_1(spark, df_Deduplicate_1)
    df_SchemaTransform_1 = collectMetrics(
        spark, 
        df_SchemaTransform_1, 
        "graph", 
        "MewCOxa3iVvHoWv9bNsev$$2LCHEi6uClGEROiiNv5jo", 
        "9322GqVhXmMJikkf6i0hH$$CjC7KUFPAPleRMaw7mmWn"
    )
    df_SetOperation_1 = SetOperation_1(spark, df_SchemaTransform_1, df_SchemaTransform_1)
    df_SetOperation_1 = collectMetrics(
        spark, 
        df_SetOperation_1, 
        "graph", 
        "JFnDL5Prrj2Z6OXTovov1$$ve0XgF2vT-qYRHHPUnJog", 
        "WU1M6vXwP42j5xhraZQ3H$$5gnYkvzcJzyHGXzBxtNsd"
    )
    df_csv_all_type = csv_all_type(spark)
    df_csv_all_type = collectMetrics(
        spark, 
        df_csv_all_type, 
        "graph", 
        "AsFanA7iJDHUy6iFkD494$$T-Rr6gZuGzb20v-9AtP73", 
        "_posjARhGw9jdalJzj-z7$$evC658R8ZUCPVoEw1Zwo0"
    )
    dest_csv_all_type_no_partition(spark, df_csv_all_type)
    df_delta = delta(spark)
    df_delta = collectMetrics(
        spark, 
        df_delta, 
        "graph", 
        "zf0XWHwj9SGWzhPSbiXtO$$Rrw8tZ269ts-muTnc1IJ5", 
        "m-fvj-aHPWpu0ZMPSFDzn$$pGK30odKzqypWhcv-uIx0"
    )
    df_Limit_4 = Limit_4(spark, df_delta)
    df_Limit_4 = collectMetrics(
        spark, 
        df_Limit_4, 
        "graph", 
        "e8gYR43R2yAepDV8orPFH$$mqYXtHvju6Wt2CQ248Vf9", 
        "7Jv_nxOWQ3vIMtWiogYvM$$36XNVyAh1tPUEZN2JMuoK"
    )
    df_Script_4 = Script_4(spark)
    df_Script_4 = collectMetrics(
        spark, 
        df_Script_4, 
        "graph", 
        "lY2wiyCbPyvB-4x5W9gPf$$FDN9-_Juqk0WtKuFeXk4v", 
        "QMatwwpfn7YoGtUPWDu2x$$auqaJuVTRBwQENaisUZAM"
    )
    df_Script_10 = Script_10(spark, df_Script_4)
    df_Script_10 = collectMetrics(
        spark, 
        df_Script_10, 
        "graph", 
        "Y8pV9KYei6ZrtKjDNfnN2$$jDK-OEV-6QbchelPYUCi4", 
        "ZxjsypY1vN6TOit7_cv5l$$zlKxZKzlpE325XPhRKZyf"
    )
    df_Script_10_1 = Script_10_1(spark, df_Script_10)
    df_Script_10_1 = collectMetrics(
        spark, 
        df_Script_10_1, 
        "graph", 
        "oTF8w9KEvtcB1J-Q-ck4M$$vTpBZUjZEUiCVTLEU4pMv", 
        "DVVHE17maXZzoVCzqPO1p$$lPc6KUQDM_dkoHnMsaUdk"
    )
    df_Script_10_1_1 = Script_10_1_1(spark, df_Script_10_1)
    df_Script_10_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1, 
        "graph", 
        "LQJfAYnHylyTO9g9T8F6k$$rfkg45iXbMXOdnnfzVLLD", 
        "mjiwQmxd9Pd8ZgJqo2yfy$$etodXNGoNHZRP1B3bn83z"
    )
    df_Script_10_1_1_1 = Script_10_1_1_1(spark, df_Script_10_1_1)
    df_Script_10_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1, 
        "graph", 
        "C4OH4KEMEBm6jIm06xz98$$-KTiKRyjUjSwDpp1FEEgk", 
        "KGT7Fiv7NoMlFg7jKpeyQ$$U9WX6BlC808i0fnMn8xb7"
    )
    df_Script_10_1_1_1_1 = Script_10_1_1_1_1(spark, df_Script_10_1_1_1)
    df_Script_10_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1, 
        "graph", 
        "3VC7efSICkJQ9MwJ1XFxI$$YKLGqI88c4UEgqDhM6MTL", 
        "lqPmflqoStkJIOn21_LST$$YHVsS6mhMbxXyZjeii36R"
    )
    df_Script_10_1_1_1_1_1 = Script_10_1_1_1_1_1(spark, df_Script_10_1_1_1_1)
    df_Script_10_1_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1, 
        "graph", 
        "etmsIXXRFdd9pc4vvnXGK$$sMI3v9zLYqdxC9C5nf_eP", 
        "5cxG2eRSKjI2XPFjqGh6C$$pfCwKDxam7E0TJa-Qc8QQ"
    )
    df_Script_10_1_1_1_1_1_1 = Script_10_1_1_1_1_1_1(spark, df_Script_10_1_1_1_1_1)
    df_Script_10_1_1_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1, 
        "graph", 
        "rD1a31yR5mboCBDwddTyd$$DCsEUxqhwUwpvK9FH04fr", 
        "LGD9vYVhi4aVSaAdTor-w$$Z79neyDC7HI0IARnomizN"
    )
    df_Join_6 = Join_6(spark, df_all_type_part_parquet, df_all_type_part_parquet)
    df_Join_6 = collectMetrics(
        spark, 
        df_Join_6, 
        "graph", 
        "iEnqqwuUU903Sc6B_QpaN$$mNOlU1sc0sAZ498rr0OQR", 
        "fNZqXt6WvdzOXAyNr4758$$BE7hlmAdCbDDST7GjcwJC"
    )
    df_Limit_7 = Limit_7(spark, df_Join_6)
    df_Limit_7 = collectMetrics(
        spark, 
        df_Limit_7, 
        "graph", 
        "jx0AdKV0WFX6qD6_Zndbj$$6yE9NSkJz2Ci1dyJzVJmV", 
        "i1Nsh_PK_FcaOd_3McZm6$$aLqbOLClxwrjo0T9rUVwW"
    )
    df_Repartition_1 = Repartition_1(spark, df_Limit_7)
    df_Repartition_1 = collectMetrics(
        spark, 
        df_Repartition_1, 
        "graph", 
        "AVrA22qbSiO5D8bGEnww6$$d4-r8EQ3lHXDKn2sZL5oX", 
        "yrNcCB_hx8IOjKH2Wh8Jx$$-xZBC0SRBrEmyMsO8m70G"
    )
    df_SubGraph_2 = SubGraph_2(spark, Config.SubGraph_2, df_Repartition_1, df_RowDistributor_1_out0)
    df_Limit_8 = Limit_8(spark, df_SubGraph_2)
    df_Limit_8 = collectMetrics(
        spark, 
        df_Limit_8, 
        "graph", 
        "7UKyoy2UqgcsQzTizhlnB$$nQ6VfkPkFqv-P65G9p-K2", 
        "2i3OcF3ZKDVsz86or5b4T$$Hvs_91XxZ8bYvNEaY_gM-"
    )
    df_Reformat_6 = Reformat_6(spark, df_Limit_8)
    df_Reformat_6 = collectMetrics(
        spark, 
        df_Reformat_6, 
        "graph", 
        "XVZA4jaSignv4W79047qL$$c4PKPbLcdXPTOnxegUVdE", 
        "OMvFDXYs4rbzeNHPH195J$$GhXfyPI0OdcDGgZ8EKjX3"
    )
    df_orc_src = orc_src(spark)
    df_orc_src = collectMetrics(
        spark, 
        df_orc_src, 
        "graph", 
        "Z6XmsZw2cEPcc5iAkiyMW$$VhcT7sWlspQ2-KoTh8imV", 
        "44_XPIJCPj1I1tCDMEHmh$$EXLiSwqLDSiRnR3w528in"
    )
    df_Deduplicate_2 = Deduplicate_2(spark, df_orc_src)
    df_Deduplicate_2 = collectMetrics(
        spark, 
        df_Deduplicate_2, 
        "graph", 
        "Y1jPqa-nQfmW_Y3WPDwuf$$P9PIjfA_IXQALkDXfOJxr", 
        "olvbl4JfshuFca-YS1IgG$$MwzaZr7NHXWa5wa4BnmUj"
    )
    df_Reformat_5 = Reformat_5(spark, df_Deduplicate_2)
    df_Reformat_5 = collectMetrics(
        spark, 
        df_Reformat_5, 
        "graph", 
        "jrow1zOQ_eYNkU7aiU1tu$$OdmRkRg-5-BU6S_fxWvIS", 
        "KHVcU5Rq5aJT_x6sZwuKL$$9z7HwEmo_IqtzD5yPwjo5"
    )
    df_Join_3 = Join_3(spark, df_Reformat_6, df_Reformat_5)
    df_Join_3 = collectMetrics(
        spark, 
        df_Join_3, 
        "graph", 
        "BjVJrfBTuUlCatWGJ3hfm$$JIVbOEE7F8Mf6ITiHvIA6", 
        "vmapgTXKYJzJsi-DEbrL9$$K8RNJs8ZPxe0pQ-ISdEld"
    )
    df_avro = avro(spark)
    df_avro = collectMetrics(
        spark, 
        df_avro, 
        "graph", 
        "5CWHE-tPSkfgaUUbMv5u5$$bz3wkz4t1Qs8S2xkBshkc", 
        "O7MlD4SsSNAngvEmyO2mL$$EPYlbrlI9CP94b-tBwNsN"
    )
    df_UTGenOrderBy_3 = UTGenOrderBy_3(spark, df_avro)
    df_UTGenOrderBy_3 = collectMetrics(
        spark, 
        df_UTGenOrderBy_3, 
        "graph", 
        "F-O0ZWyymLHQ7NAiD4HwH$$mRW3uIYVYRgYXJeBJQ7JX", 
        "23_EUJ5mmZmxkUF_FP06-$$05CM-G0C71N7lAUdf7DdA"
    )
    df_Reformat_7 = Reformat_7(spark, df_UTGenOrderBy_3)
    df_Reformat_7 = collectMetrics(
        spark, 
        df_Reformat_7, 
        "graph", 
        "oEhaLSE6b3A1LJxg3Bkz_$$l12DOtVNEzu8reItRujM_", 
        "kX6osjcARyB_vtVysaBkg$$k2MRDGFfUnWalJzYqYMPk"
    )
    df_Join_4 = Join_4(spark, df_Join_3, df_Reformat_7)
    df_Join_4 = collectMetrics(
        spark, 
        df_Join_4, 
        "graph", 
        "SdsAu-JEcKL4oHBjOOWw5$$xyS1iKUMKSKDsyjxCiYZL", 
        "OQ4wWZItknICGVTFmZ7Df$$sJY9WA14U_nDYll42Tk8T"
    )
    df_Script_10_1_1_1_1_1_1_1 = Script_10_1_1_1_1_1_1_1(spark, df_Script_10_1_1_1_1_1_1)
    df_Script_10_1_1_1_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1, 
        "graph", 
        "FBexJVOppwC2UYrLKfUOF$$cE8m7D92aovlUPzOg7Y3p", 
        "TWz7U4Dv2ITMhldL03IbO$$vq96vACQVKUxBQEJtt0zL"
    )
    df_Script_10_1_1_1_1_1_1_1_1_output0, df_Script_10_1_1_1_1_1_1_1_1_output1, df_Script_10_1_1_1_1_1_1_1_1_output2 = Script_10_1_1_1_1_1_1_1_1(
        spark, 
        df_Script_10_1_1_1_1_1_1_1
    )
    df_Script_10_1_1_1_1_1_1_1_1_output0 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1_1_output0, 
        "graph", 
        "pYIghOBjIgYcw74vG9bbQ$$gHF2OQST_t8VtlB3ylKOV", 
        "-_aWa_jQ4lRQN-n0DRweO$$0QqcxYzVUc7m7F0HYRt5Y"
    )
    df_Script_10_1_1_1_1_1_1_1_1_output1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1_1_output1, 
        "graph", 
        "pYIghOBjIgYcw74vG9bbQ$$gHF2OQST_t8VtlB3ylKOV", 
        "a8Qx4sS8LpZ98GFsPPo88$$sQ-OxebwVBEt2otlf0Tki"
    )
    df_Script_10_1_1_1_1_1_1_1_1_output2 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1_1_output2, 
        "graph", 
        "pYIghOBjIgYcw74vG9bbQ$$gHF2OQST_t8VtlB3ylKOV", 
        "1DVFl12tqxqRe_cXY1PNS$$dV5ZX3t9BH7HC5cL7-Xom"
    )
    df_Script_10_1_1_1_1_1_1_1_1_1 = Script_10_1_1_1_1_1_1_1_1_1(spark, df_Script_10_1_1_1_1_1_1_1_1_output0)
    df_Script_10_1_1_1_1_1_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1_1_1, 
        "graph", 
        "thUTfJIgnC7MWUYGGusi8$$QeCg-kRxLw2JH_QFD5W5-", 
        "yxWh_nrSAuBr-WU2G6hH1$$V-n-1P6v5VByaT2w-JAg6"
    )
    df_Script_10_1_1_1_1_1_1_1_1_1.cache().count()
    df_Script_10_1_1_1_1_1_1_1_1_1.unpersist()
    df_catalog = catalog(spark)
    df_catalog = collectMetrics(
        spark, 
        df_catalog, 
        "graph", 
        "__BeSCJf1X2jfa8iyY4-T$$07c-JgTp7QeEW439tKvAI", 
        "cY2VcRtlr_Ypjbo2YK6bm$$RAnzMQK3YjV0hNDb-86v_"
    )
    df_Reformat_14 = Reformat_14(spark, df_catalog)
    df_Reformat_14 = collectMetrics(
        spark, 
        df_Reformat_14, 
        "graph", 
        "LEDjjajm33AFBjMK7JioI$$rVWjZayD16h1-uiVX4Hdm", 
        "fbhuMh-rzp5KYLcyDkDFf$$hmxqhdByTaoXKqNkuTfOf"
    )
    df_all_type_part_parquet_1 = all_type_part_parquet_1(spark)
    df_all_type_part_parquet_1 = collectMetrics(
        spark, 
        df_all_type_part_parquet_1, 
        "graph", 
        "NY4yqJbSD-gQI-1V42gYM$$w5ymXdPw-ReVC9yZ4wF-k", 
        "lggmnFNhfGqyLsMY-ObrJ$$2patt1XujEHnBwrUEaUsi"
    )
    df_FlattenSchema_1_1 = FlattenSchema_1_1(spark, df_all_type_part_parquet_1)
    df_FlattenSchema_1_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1_1, 
        "graph", 
        "cilPVPGiROS6q-i6Bmoud$$sUHsch1VrEcur_1rk5Su2", 
        "OT7opQ2fDXgbL3XwnkWTR$$peKEhC8QkFeUtdCrLRljy"
    )
    df_FlattenSchema_1_1.cache().count()
    df_FlattenSchema_1_1.unpersist()
    df_src_ut_parquet_all = src_ut_parquet_all(spark)
    df_src_ut_parquet_all = collectMetrics(
        spark, 
        df_src_ut_parquet_all, 
        "graph", 
        "2gdpmd5LP9WpcJvc7sBWg$$CcRfyYPTUGbcDheu3WiMB", 
        "0NWji28TTLxZHhoBCEBHk$$LnAcQC6vvtD6CMfGObhj_"
    )
    df_UTGenAllReformat_12 = UTGenAllReformat_12(spark, df_src_ut_parquet_all)
    df_UTGenAllReformat_12 = collectMetrics(
        spark, 
        df_UTGenAllReformat_12, 
        "graph", 
        "xFJ677pxDBcB70K6jtp4d$$9tPV0j5HB9l1XWUZh_piT", 
        "VeZntApaeK-RzMXX89SZY$$-SPdWodOllgm5Z0QrisTq"
    )
    df_UTGenAllReformat_12.cache().count()
    df_UTGenAllReformat_12.unpersist()
    df_Aggregate_1_1 = Aggregate_1_1(spark, df_SetOperation_1)
    df_Aggregate_1_1 = collectMetrics(
        spark, 
        df_Aggregate_1_1, 
        "graph", 
        "EMMifgFmXFCuFCW7L3J5R$$YDn_-qay3xshGz4j0lkk3", 
        "N7M8FCo12kDmc6qSlyuQd$$yI-eqzjFrYhvMVTnYdXea"
    )
    df_Aggregate_1 = Aggregate_1(spark, df_SetOperation_1)
    df_Aggregate_1 = collectMetrics(
        spark, 
        df_Aggregate_1, 
        "graph", 
        "UM37Y4sZy0XbEvnMP3z0d$$PJ-qsFp1oBTaLAY-uUmOZ", 
        "eXuydhO1EqpAMfbq8b8LT$$dqKKSFDwQjydqmvIi4Dft"
    )
    df_Script_10_1_1_1_1_1_1_1_1_1_1 = Script_10_1_1_1_1_1_1_1_1_1_1(spark, df_Script_10_1_1_1)
    df_Script_10_1_1_1_1_1_1_1_1_1_1 = collectMetrics(
        spark, 
        df_Script_10_1_1_1_1_1_1_1_1_1_1, 
        "graph", 
        "8kYLRQLDi8b18GgrD3bqY$$p95j20cwGehxiufSVYfBa", 
        "ajqnr1h_8Jxe7AIhYS7NP$$Jt1vVgln81IBnRUh1phtN"
    )
    df_Script_10_1_1_1_1_1_1_1_1_1_1.cache().count()
    df_Script_10_1_1_1_1_1_1_1_1_1_1.unpersist()
    df_text = text(spark)
    df_text = collectMetrics(
        spark, 
        df_text, 
        "graph", 
        "QmGu-UelGs__wu0AWreZx$$Dec9-PSzLbbv6Iyos5iku", 
        "gWPrIMMlkrG2UvHqNPj6D$$FruLC9PEQ8DO2qLMBWDKJ"
    )
    df_Reformat_4 = Reformat_4(spark, df_text)
    df_Reformat_4 = collectMetrics(
        spark, 
        df_Reformat_4, 
        "graph", 
        "nLjPP0w7Cl6MSM6RXHIK0$$iS1hmJ0J0ImQO_7vTMOSk", 
        "Z7JdWCGM7uYZheCRUgwvh$$_JKl5kg-4-dO6AgxV7k8-"
    )
    df_all_type_main_1_out0, df_all_type_main_1_out1, df_all_type_main_1_out2 = all_type_main_1(
        spark, 
        Config.all_type_main_1, 
        df_all_type_part_parquet, 
        df_all_type_part_parquet, 
        df_all_type_part_parquet
    )
    df_Script_1 = Script_1(spark, df_Aggregate_1)
    df_Script_1 = collectMetrics(
        spark, 
        df_Script_1, 
        "graph", 
        "TFjH9dGegxAAq0-7pL845$$EA0NgKHjYint6E1mmks-E", 
        "ZvgsUJ_9eyK0UXoawagVL$$gD5njuMvJZpys_gRx0vcy"
    )
    df_Script_1.cache().count()
    df_Script_1.unpersist()
    df_json_in = json_in(spark)
    df_json_in = collectMetrics(
        spark, 
        df_json_in, 
        "graph", 
        "iEAhKfffRKYROLhkq6LCM$$FUrIc9QCdGEO7TuzFhdTJ", 
        "AkoFj0jmMBshTbQIjr103$$OaRGS-kcQrvnXd_bho8ve"
    )
    df_VeryLargeExpr = VeryLargeExpr(spark, df_json_in)
    df_VeryLargeExpr = collectMetrics(
        spark, 
        df_VeryLargeExpr, 
        "graph", 
        "HlaWDG5dsklrL9pm8GG8M$$PhFCGBTLGIr5vXoTnP5v6", 
        "NumrPyiY_QXIWM_GXd7Un$$36iPKHFjqehM2767gFFSP"
    )
    df_src_jdbc_userandpass_test_table = src_jdbc_userandpass_test_table(spark)
    df_src_jdbc_userandpass_test_table = collectMetrics(
        spark, 
        df_src_jdbc_userandpass_test_table, 
        "graph", 
        "tDHimyfMF82X07PcbAqMd$$zjHKyxNg41YpDM0iwSesv", 
        "MsAswUIDzMJhEdX8ioNDy$$5nAnyVJP7rMU6khHW97QY"
    )
    df_Reformat_9 = Reformat_9(spark, df_RowDistributor_1_out2)
    df_Reformat_9 = collectMetrics(
        spark, 
        df_Reformat_9, 
        "graph", 
        "C29lAbt4R5GEzHuRikLcu$$KJhkbaqwor1_W6sTIOM4N", 
        "GsbGTC9lDwPUI4TRCfxNm$$yFCIAy92G56gcU54tsYp_"
    )
    df_Reformat_9.cache().count()
    df_Reformat_9.unpersist()
    df_Script_11 = Script_11(spark, df_Script_10_1_1_1_1_1_1_1_1_output1)
    df_Script_11 = collectMetrics(
        spark, 
        df_Script_11, 
        "graph", 
        "oe5VAiZiKLu7SUG99Oai7$$71QliKPCawKw68wVndpcV", 
        "vmuEUuPBRL9z_m1bXRtLz$$oB5Mph0woDZxBk9is6Obu"
    )
    df_Script_11.cache().count()
    df_Script_11.unpersist()
    df_SQLStatement_1_out, df_SQLStatement_1_out1, df_SQLStatement_1_out2 = SQLStatement_1(
        spark, 
        df_all_type_part_parquet, 
        df_all_type_part_parquet
    )
    df_SQLStatement_1_out = collectMetrics(
        spark, 
        df_SQLStatement_1_out, 
        "graph", 
        "gjMe6lyUngJb9qtWsPJdG$$a5FgmlsagVGQ-Ir816l6x", 
        "p0CRooVi1DlyYp3KyzjcP$$2Tb7QiSl_GDPSBf5tK94C"
    )
    df_SQLStatement_1_out1 = collectMetrics(
        spark, 
        df_SQLStatement_1_out1, 
        "graph", 
        "gjMe6lyUngJb9qtWsPJdG$$a5FgmlsagVGQ-Ir816l6x", 
        "mmAThmA8eZ8TWGKyEYAeT$$-SVeAEm5c4CGAt7992p5j"
    )
    df_SQLStatement_1_out2 = collectMetrics(
        spark, 
        df_SQLStatement_1_out2, 
        "graph", 
        "gjMe6lyUngJb9qtWsPJdG$$a5FgmlsagVGQ-Ir816l6x", 
        "klZjo-VL4nM-x2mJw2x9v$$mUt9_Lydb9sTlfHI8OkBM"
    )
    df_SQLStatement_1_out1.cache().count()
    df_SQLStatement_1_out1.unpersist()
    df_SQLStatement_1_out2.cache().count()
    df_SQLStatement_1_out2.unpersist()
    df_Reformat_15 = Reformat_15(spark, df_csv_all_type)
    df_Reformat_15 = collectMetrics(
        spark, 
        df_Reformat_15, 
        "graph", 
        "zjl2OkVETv6JHbonHp74V$$V9bfArO_p5n2ED2KwqGeS", 
        "9jXaJTdFUIjZGLj_vc5cy$$lND32pDnRQ4Mh__Dw292O"
    )
    df_OrderBy_4 = OrderBy_4(spark, df_delta)
    df_OrderBy_4 = collectMetrics(
        spark, 
        df_OrderBy_4, 
        "graph", 
        "PMK5IbeHdFKI_kVBXezxv$$SvIv8eXADLBabqXLFsSye", 
        "JPp8waTMEALCxx-RgmBLe$$7-AKbD5Qi60_VRKRZmJ8w"
    )
    df_Limit_5 = Limit_5(spark, df_delta)
    df_Limit_5 = collectMetrics(
        spark, 
        df_Limit_5, 
        "graph", 
        "BRL6b1VATi5syNUzo8RH7$$UdOSsNaBqb7PzrNypQy2H", 
        "tnqt3tW00nFE1obAN03sb$$djd_zMdJ_F1Ns9sfsyofk"
    )
    df_Script_3 = Script_3(
        spark, 
        df_Reformat_14, 
        df_Limit_5, 
        df_OrderBy_4, 
        df_Limit_4, 
        df_VeryLargeExpr, 
        df_Reformat_15, 
        df_OrderBy_1
    )
    df_Script_3 = collectMetrics(
        spark, 
        df_Script_3, 
        "graph", 
        "-3VpysfVzMeGJlzqBNlq_$$ZaNTPymddlozSuJherlQv", 
        "8NNUyPXeI68kaysRjOSPK$$wsEyecXcd28exUXVvELKN"
    )
    df_FlattenSchema_1 = FlattenSchema_1(spark, df_SQLStatement_1_out)
    df_FlattenSchema_1 = collectMetrics(
        spark, 
        df_FlattenSchema_1, 
        "graph", 
        "3-3pUxg-OmbLmN46tcBUz$$KT_BvNIfSrzYQAX6bPoP8", 
        "INfBHLuOcxIwIT33NNcTv$$RLgOfO3B23UnM-2xLZz0-"
    )
    Script_8(spark, df_FlattenSchema_1)
    df_Script_6 = Script_6(
        spark, 
        df_all_type_main_1_out0, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out1, 
        df_all_type_main_1_out2, 
        df_all_type_main_1_out2, 
        df_all_type_main_1_out2
    )
    df_Script_6 = collectMetrics(
        spark, 
        df_Script_6, 
        "graph", 
        "5kjgFXnDVKXnZbuLD5jdC$$SyZ5rbYl2DTmA2SBi2eLW", 
        "EvF8Dow274Ex0OhnayGYM$$i6UX0uzgLjqHwTvtrZnVu"
    )
    df_Reformat_11 = Reformat_11(spark, df_Script_6)
    df_Reformat_11 = collectMetrics(
        spark, 
        df_Reformat_11, 
        "graph", 
        "AaIDfqAztEkgFn5KRvY02$$XDz5fzxaLT2bgSZSaafW6", 
        "CslDD0qqB0eax70M2UCCZ$$8mL1DtQCpFdTWxsvaY3xk"
    )
    df_Reformat_11.cache().count()
    df_Reformat_11.unpersist()
    df_Script_12 = Script_12(spark, df_Script_10_1_1_1_1_1_1_1_1_output2)
    df_Script_12 = collectMetrics(
        spark, 
        df_Script_12, 
        "graph", 
        "I3JANHzf1GVbjRXxw3kQe$$U8_HNjQP9CDilu1Em8Vlj", 
        "vDDKfjiuErpQ8qOGkZoBa$$dhu6sUv80Tcbc-qI0Hbyi"
    )
    df_Script_12.cache().count()
    df_Script_12.unpersist()
    df_SubGraph_7 = SubGraph_7(spark, Config.SubGraph_7, df_Script_3)
    df_Filter_3 = Filter_3(spark, df_SubGraph_7)
    df_Filter_3 = collectMetrics(
        spark, 
        df_Filter_3, 
        "graph", 
        "k8c-yzRHlRf7RSubV8RUN$$djFCzsgrBRWotU5TBT5vc", 
        "I40tiaflw7UPxUVYWFBBJ$$RGRM5sgD3AdRIgM1TivRt"
    )
    df_Filter_3.cache().count()
    df_Filter_3.unpersist()
    df_src_parquet_all_type_no_partition = src_parquet_all_type_no_partition(spark)
    df_src_parquet_all_type_no_partition = collectMetrics(
        spark, 
        df_src_parquet_all_type_no_partition, 
        "graph", 
        "m7IaU0XgW06uSIbFGef0B$$8YjTXHRWeIcuhvz_iG2NZ", 
        "gC-8YSjj5-83Mi4jzyWeE$$eWVZk_fAShNrHFWsAWIsA"
    )
    df_Limit_9 = Limit_9(spark, df_Join_4)
    df_Limit_9 = collectMetrics(
        spark, 
        df_Limit_9, 
        "graph", 
        "cKFCDnAFle9Y7_Z75f91D$$-8WecmUvnsMzFmFYraCx4", 
        "0GItvH4CK7tzzNvabLTsh$$r7w5ecu0XsEojWY08vimA"
    )
    df_call_func = call_func(spark, df_src_parquet_all_type_no_partition)
    df_call_func = collectMetrics(
        spark, 
        df_call_func, 
        "graph", 
        "hfO-eOQ0xKNtnRtvSSV4t$$DqsYwlOwb_iu0xyhymWP1", 
        "PI6oCR2ZnJ8q_6JSAamDE$$jTRIjq7nxEmJFH9tZVvsC"
    )
    df_call_func.cache().count()
    df_call_func.unpersist()
    df_WindowFunction_1 = WindowFunction_1(spark, df_RowDistributor_1_out3)
    df_WindowFunction_1 = collectMetrics(
        spark, 
        df_WindowFunction_1, 
        "graph", 
        "6M_hg9gAzr8d7tp6EWYAP$$6ze3-Fnz0TJL3FHRhDRoo", 
        "THZf4U0Afr0WwFlHIExkT$$ZcG-fixeZPUAPkqvmsgpR"
    )
    Script_2(spark, df_WindowFunction_1)
    df_UTGenSetOperation_2 = UTGenSetOperation_2(spark, df_csv_all_type, df_csv_all_type)
    df_UTGenSetOperation_2 = collectMetrics(
        spark, 
        df_UTGenSetOperation_2, 
        "graph", 
        "nhcr8lRzD1Z62M29QSJV2$$G3wZPVKTwdIe7pFbDPx8A", 
        "8BO0wVrXpfywc10AAtnm3$$HOGG5Xn1Bn2NB3wojyJQI"
    )
    df_Reformat_13 = Reformat_13(spark, df_Aggregate_1_1)
    df_Reformat_13 = collectMetrics(
        spark, 
        df_Reformat_13, 
        "graph", 
        "qciLOlCUfyfhosU27NIj3$$P0M1VEJ3Clio9bfefngFW", 
        "ub5IMhbShodKsQsAGjlmR$$4HtiJIk-ERg45edVspYUO"
    )
    df_Reformat_13.cache().count()
    df_Reformat_13.unpersist()
    df_ComplexExpr = ComplexExpr(spark, df_src_parquet_all_type_no_partition)
    df_ComplexExpr = collectMetrics(
        spark, 
        df_ComplexExpr, 
        "graph", 
        "jLMRpTBR_DSQXcbn3-w5t$$DURs_-zDLoFxoxJ2U3jav", 
        "QeW6AXzdAfKrFZuBLp-aB$$4TUqZXq0hzrXa7yNQJNBJ"
    )
    df_OrderBy_5 = OrderBy_5(spark, df_ComplexExpr)
    df_OrderBy_5 = collectMetrics(
        spark, 
        df_OrderBy_5, 
        "graph", 
        "VItSFIYTxm_DTe_NTG7TA$$zuwJmTgGpxrS-lqeNt_Cw", 
        "Czcyk9sHItA4nU32spgaq$$qKeZEqV15XoqnCgXV2j2K"
    )
    df_OrderBy_5.cache().count()
    df_OrderBy_5.unpersist()
    df_Script_7 = Script_7(spark, df_UTGenSetOperation_2)
    df_Script_7 = collectMetrics(
        spark, 
        df_Script_7, 
        "graph", 
        "n1g0WJ7SQRJRYT8wqn0oJ$$X6V1qjyaavNtgCHMr03gZ", 
        "u2CtcUxhYnoPMoms-dkSx$$ZXgJ1fz7TrUcGymd8YhJV"
    )
    df_Script_7.cache().count()
    df_Script_7.unpersist()
    df_Join_5 = Join_5(spark, df_Limit_9, df_Reformat_4)
    df_Join_5 = collectMetrics(
        spark, 
        df_Join_5, 
        "graph", 
        "BxLGlSJsIH_GX44ps93vE$$GQFLMIHvyp20PqCdwSHu1", 
        "dvt3l9wKZJwxnYzggRdLH$$qFCG8vzzPdKTat2OjHZWH"
    )
    df_Join_5.cache().count()
    df_Join_5.unpersist()
    df_Reformat_10 = Reformat_10(spark, df_src_jdbc_userandpass_test_table)
    df_Reformat_10 = collectMetrics(
        spark, 
        df_Reformat_10, 
        "graph", 
        "ByZSaN7V3M-_cZrjbizJq$$9M3q3JF5NRznUxIOkUA9b", 
        "zeVvn61bvb9-05ypFVEHM$$hFn8YFWNSbxSImL3RwFGf"
    )
    df_Reformat_10.cache().count()
    df_Reformat_10.unpersist()

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    MetricsCollector.initializeMetrics(spark)
    spark.conf.set("prophecy.collect.basic.stats", "true")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    spark.conf.set("spark.sql.optimizer.excludedRules", "org.apache.spark.sql.catalyst.optimizer.ColumnPruning")
    spark.conf.set("spark_config1", "spark./<>;'\"[]{}\\|~*/-+p- config1 value !~_#@%^&*()-=")
    spark.conf.set("spark_config2", "spark_config2 value")
    spark.conf.set("fs.s3a.access.key", "AKIAR6ESAR2JAQNZNVMH")
    spark.conf.set("fs.s3a.secret.key", "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")
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_DEP_MGMT_ALL")
    spark.sparkContext._jsc\
        .hadoopConfiguration()\
        .set(
        "hadoop_config1",
        "hadoo./<>;'\"[]{}\\|~*/-+p- config1 value !~_#@%^&*()-="
    )
    spark.sparkContext._jsc.hadoopConfiguration().set("hadoop_config2", "hadoop_config2 value")
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.access.key", "AKIAR6ESAR2JAQNZNVMH")
    spark.sparkContext._jsc.hadoopConfiguration().set("fs.s3a.secret.key", "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")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_DEP_MGMT_ALL")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
