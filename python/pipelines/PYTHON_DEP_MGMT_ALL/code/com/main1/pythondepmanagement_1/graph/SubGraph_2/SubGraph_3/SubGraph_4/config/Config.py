from com.main1.pythondepmanagement_1.graph.SubGraph_2.SubGraph_3.SubGraph_4.SubGraph_5.config.Config import (
    SubgraphConfig as SubGraph_5_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, SubGraph_5: dict={}, **kwargs):
        self.SubGraph_5 = self.get_config_object(
            prophecy_spark, 
            SubGraph_5_Config(prophecy_spark = prophecy_spark), 
            SubGraph_5, 
            SubGraph_5_Config
        )
        pass

    def update(self, updated_config):
        self.SubGraph_5 = updated_config.SubGraph_5
        pass

Config = SubgraphConfig()
