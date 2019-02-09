
'''
Created on 12 feb 2016

@author: fragom
'''

import numpy as np
from statisticAnalysis import StatisticAnalysis
        

class QuantitativeAnalysis(StatisticAnalysis):
    '''
    classdocs
    '''
    def __init__(self, signalSimulation, signalReference):
        '''
        Constructor
        '''
        StatisticAnalysis.__init__(self, signalSimulation, signalReference)
            
    def error_method(self, parametro):
        switcher = {
            'MAE': self.__qaMAE,
            'MSE': self.__qaMSE,
            'RMSE': self.__qaRMSE,
            'MBD': self.__qaMBD,
        }
        # Get the function from switcher dictionary
        func = switcher[parametro]
        # Execute the function
        self._scalarOutput= func()
    
    def __qaMAPE(self):
        arrayRef= np.array(self._signalRef['magnitude'])
        arrayOut= np.array(self._signalOut['magnitude'])
        mape= np.mean(np.divide(np.abs(np.subtract(arrayOut,arrayRef)), np.abs(arrayOut)))* 100
        arrayRef= arrayOut= None
        return mape
        
    def __qaMAE(self):
        arrayRef= np.array(self._signalRef['magnitude'])
        arrayOut= np.array(self._signalOut['magnitude'])
        mae= np.mean(arrayOut - arrayRef)
        arrayRef= arrayOut= None
        return mae
    
    def __qaMSE(self):
        arrayRef= np.array(self._signalRef['magnitude'])
        arrayOut= np.array(self._signalOut['magnitude'])
        mse= np.mean(np.power(np.subtract(arrayOut, arrayRef), 2))
        arrayRef= arrayOut= None
        return mse
    
    def __qaRMSE(self): 
        arrayRef= np.array(self._signalRef['magnitude'])
        arrayOut= np.array(self._signalOut['magnitude'])
        rmse= np.sqrt(np.mean(np.power(np.subtract(arrayOut, arrayRef), 2)))
        arrayRef= arrayOut= None
        return rmse
    
    def __qaMBD(self): 
        arrayRef= np.array(self._signalRef['magnitude'])
        arrayOut= np.array(self._signalOut['magnitude'])
        mbd= np.mean(np.subtract(arrayOut, arrayRef))
        arrayRef= arrayOut= None
        return mbd
    
    def qa_ScalarError(self, calculatedValue, expectedValue):
        '''
        calculatedValue
        expectedValue
        '''
        absoluteError= abs(calculatedValue-expectedValue)
        if expectedValue!= 0:
            relativeError= abs(calculatedValue-expectedValue) / abs(expectedValue)
            
        return [absoluteError, relativeError]
    