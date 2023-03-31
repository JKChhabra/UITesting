import unittest

from test.pythonbasic.test.mainone.graph.test_Script_4 import *
from test.pythonbasic.test.mainone.graph.test_Reformat_2 import *
from test.pythonbasic.test.mainone.graph.test_Reformat_1 import *
from test.pythonbasic.test.mainone.graph.test_Reformat_3 import *
from test.pythonbasic.test.mainone.graph.test_Script_3 import *
from test.pythonbasic.test.mainone.graph.test_Script_1 import *

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(unittest.TestSuite())
