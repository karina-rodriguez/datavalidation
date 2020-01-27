import numpy as np
import pandas as pd

    
class Validator:
    
    dataFrameToValidate = []
    dataFrameValidated = []


    def __init__(self,dataFrameToValidate):
        self.dataFrameToValidate = dataFrameToValidate
 
    def validateData(self):
        for column in self.dataFrameToValidate.columns.values:
            print ("I am validator",column)

        return self.dataFrameToValidate

#    def test_noEmpty(self):
#        self.assertEqual(self.dataFrameToValidate,[])
#        
#        if 