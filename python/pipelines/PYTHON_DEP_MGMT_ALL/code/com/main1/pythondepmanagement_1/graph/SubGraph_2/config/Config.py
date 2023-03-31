from com.main1.pythondepmanagement_1.graph.SubGraph_2.SubGraph_3.config.Config import (
    SubgraphConfig as SubGraph_3_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, SubGraph_3: dict={}, **kwargs):
        self.SubGraph_3 = self.get_config_object(
            prophecy_spark, 
            SubGraph_3_Config(prophecy_spark = prophecy_spark), 
            SubGraph_3, 
            SubGraph_3_Config
        )
        pass

    def update(self, updated_config):
        self.SubGraph_3 = updated_config.SubGraph_3
        pass

Config = SubgraphConfig()
