from com.main1.pythondepmanagement_1.graph.SubGraph_2.SubGraph_3.SubGraph_4.config.Config import (
    SubgraphConfig as SubGraph_4_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, SubGraph_4: dict={}, **kwargs):
        self.SubGraph_4 = self.get_config_object(
            prophecy_spark, 
            SubGraph_4_Config(prophecy_spark = prophecy_spark), 
            SubGraph_4, 
            SubGraph_4_Config
        )
        pass

    def update(self, updated_config):
        self.SubGraph_4 = updated_config.SubGraph_4
        pass

Config = SubgraphConfig()
