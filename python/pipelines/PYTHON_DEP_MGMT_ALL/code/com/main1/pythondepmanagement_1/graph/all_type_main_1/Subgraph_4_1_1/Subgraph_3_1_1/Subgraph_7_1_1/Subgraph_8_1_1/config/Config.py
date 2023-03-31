from com.main1.pythondepmanagement_1.graph.all_type_main_1.Subgraph_4_1_1.Subgraph_3_1_1.Subgraph_7_1_1\
    .Subgraph_8_1_1\
    .Subgraph_9_1_1\
    .config\
    .Config import SubgraphConfig as Subgraph_9_1_1_Config
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, Subgraph_9_1_1: dict={}, **kwargs):
        self.Subgraph_9_1_1 = self.get_config_object(
            prophecy_spark, 
            Subgraph_9_1_1_Config(prophecy_spark = prophecy_spark), 
            Subgraph_9_1_1, 
            Subgraph_9_1_1_Config
        )
        pass

    def update(self, updated_config):
        self.Subgraph_9_1_1 = updated_config.Subgraph_9_1_1
        pass

Config = SubgraphConfig()
