import numpy as np
import pandas as pd
import pandera as pa

    
class Validator:
    
    dataFrameToValidate = []
    dataFrameValidated = []


    def __init__(self,dataFrameToValidate):
        self.dataFrameToValidate = dataFrameToValidate
 
    def validateData(self):
        return self.dataFrameToValidate
