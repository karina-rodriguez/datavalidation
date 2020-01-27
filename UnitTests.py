#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:11:37 2020

@author: kre
"""
#Good tutorial for this: https://www.linkedin.com/learning/search?keywords=unittest&u=67552674
#https://docs.python.org/3/library/unittest.html
# =============================================================================
# To Run from console
# (base) KRE-laptop:dataValidator kre$ python -m unittest UnitTests
# (base) KRE-laptop:dataValidator kre$ python -m unittest UnitTests.UnitTests
# (base) KRE-laptop:dataValidator kre$ python -m unittest UnitTests.UnitTests.test_IsString
# import unittest
# =============================================================================
from Reader import Reader
from Validator import Validator

class UnitTests(unittest.TestCase):
    
    #this is a simple example to start with
    def test_IsString(self):
        text = 'this is a text'
        self.assertIsNot(text,'') 

if __name__=='__main__':
    unittest.main()
    