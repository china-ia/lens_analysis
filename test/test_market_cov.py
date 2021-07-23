# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:30:01 2021

@author: David
"""

import unittest
from context import lens_analysis
from lens_analysis import market_cov as mc
import pandas as pd

FOLD = "res/"


class TestFuncs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fam = pd.read_excel(FOLD+"fam_cits.xlsx")

    def testCalcMarkCov(self):
        fam = mc.calc_mark_cov(self.fam)
        assert fam.iloc[0]["Market Coverage"] > 0.045 and fam.iloc[0]["Market Coverage"] < 0.046
        assert fam.iloc[-1]["Market Coverage"] == 0.7
    
    def testGetMarkCov(self):
        cov = mc._get_mark_cov("AR", 1961)
        assert cov == 24450604878.0
    
    
if __name__ == '__main__':
    unittest.main()