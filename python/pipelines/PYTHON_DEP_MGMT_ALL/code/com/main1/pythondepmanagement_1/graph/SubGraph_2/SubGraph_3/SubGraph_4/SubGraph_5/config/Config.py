from com.main1.pythondepmanagement_1.graph.SubGraph_2.SubGraph_3.SubGraph_4.SubGraph_5.SubGraph_6.config.Config import (
    SubgraphConfig as SubGraph_6_Config
)
from prophecy.config import ConfigBase


class SubgraphConfig(ConfigBase):

    def __init__(self, prophecy_spark=None, SubGraph_6: dict={}, **kwargs):
        self.SubGraph_6 = self.get_config_object(
            prophecy_spark, 
            SubGraph_6_Config(prophecy_spark = prophecy_spark), 
            SubGraph_6, 
            SubGraph_6_Config
        )
        pass

    def update(self, updated_config):
        self.SubGraph_6 = updated_config.SubGraph_6
        pass

Config = SubgraphConfig()
