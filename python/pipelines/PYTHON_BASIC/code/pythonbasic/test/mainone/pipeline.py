from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pythonbasic.test.mainone.config.ConfigStore import *
from pythonbasic.test.mainone.udfs.UDFs import *
from prophecy.utils import *
from pythonbasic.test.mainone.graph import *

def pipeline(spark: SparkSession) -> None:
    df_src_csv_special_char_column_name = src_csv_special_char_column_name(spark)
    df_src_csv_special_char_column_name = collectMetrics(
        spark, 
        df_src_csv_special_char_column_name, 
        "graph", 
        "vlcUd7KAM_zvifvMwu9pZ$$8MswNyzCALGAeJjSxRNDZ", 
        "CHZEgFOxU2vx1Q32ysboc$$LB9injlM6BGINFq1djzRE"
    )
    df_Reformat_1 = Reformat_1(spark, df_src_csv_special_char_column_name)
    df_Reformat_1 = collectMetrics(
        spark, 
        df_Reformat_1, 
        "graph", 
        "oSnCy6FWydBV675_CTMv8$$In5C4VfAlHsx5qLzItDuW", 
        "OgcPwunAgx_Y_Y3m8Krd0$$2IcX9S_gny3CS3TcShBZe"
    )
    df_Script_4 = Script_4(spark, df_Reformat_1)
    df_Script_4 = collectMetrics(
        spark, 
        df_Script_4, 
        "graph", 
        "Uooc3h8tVmdPw5lJv48-v$$8fU6UMC7OvanJjkndel2x", 
        "1DpbGVDq4gDguuxlp-FsI$$a6wwBFUElAoCP-OZd2Dyj"
    )
    df_Script_4.cache().count()
    df_Script_4.unpersist()
    df_Script_1 = Script_1(spark, df_src_csv_special_char_column_name)
    df_Script_1 = collectMetrics(
        spark, 
        df_Script_1, 
        "graph", 
        "wBdgJvaD01uN-lcIie2xJ$$i1vDCthN6JF7nseh4f0kK", 
        "HG2PFttcDIFYU1vzP-sYS$$LRER5fLiAr-bMCiDFK5N1"
    )
    df_Reformat_2 = Reformat_2(spark, df_Script_1)
    df_Reformat_2 = collectMetrics(
        spark, 
        df_Reformat_2, 
        "graph", 
        "048ogu6WADjDj-febNiED$$cbZiqf-vOBq4RxSRvDKRY", 
        "8350_cv_665aSsH1tXMLM$$Vf7xQDVe0OoO9CY0smQKu"
    )
    df_Reformat_2.cache().count()
    df_Reformat_2.unpersist()
    df_Script_5 = Script_5(spark, df_src_csv_special_char_column_name)
    df_Script_5 = collectMetrics(
        spark, 
        df_Script_5, 
        "graph", 
        "2asYObWPU5LTeK5quA_Y6$$j6AVMgNkfy9f2PyXW2Apb", 
        "IyTLFxYC1V6hn64VpC3kw$$In-71aGN5Ovd2ygKVYWRH"
    )
    df_Reformat_3 = Reformat_3(spark, df_Script_5)
    df_Reformat_3 = collectMetrics(
        spark, 
        df_Reformat_3, 
        "graph", 
        "Z2MampB4oCcGewquXgPE1$$jta-gpnDuEhM598aJtDiT", 
        "CdFT_y4Eg_9ZqT8q7xG0q$$0DgBGM5ndnDRhNPCkYNI5"
    )
    df_Reformat_3.cache().count()
    df_Reformat_3.unpersist()
    df_Script_3 = Script_3(spark, df_src_csv_special_char_column_name)
    df_Script_3 = collectMetrics(
        spark, 
        df_Script_3, 
        "graph", 
        "cGWWs9JdAHyiYStCJ-ryD$$rzbrJ6yXTp9VuZwvwy0aS", 
        "IwBHmVE1rBeErOjcJlXb6$$dhF8pSpysAHLkg1Ua8G4e"
    )
    df_Script_3.cache().count()
    df_Script_3.unpersist()

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
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/PYTHON_BASIC")
    
    MetricsCollector.start(spark = spark, pipelineId = "pipelines/PYTHON_BASIC")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
