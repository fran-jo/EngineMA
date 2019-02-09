'''
Created on 12 feb 2016

@author: fragom
'''
from numpy.random import sample

class StatisticAnalysis(object):
    '''
    classdocs
    '''
    _signalOut= {}
    _signalRef= {}
    _scalarOutput= 0
    _vectorOutput= []
    
    def __init__(self, signalOut, signalRef):
        self._signalOut= signalOut
        if not signalRef== '' or not signalRef== []:
            self._signalRef= signalRef

    @property
    def signalSimulation(self):
        return self._signalOut
    @signalSimulation.setter
    def signalSimulation(self, senyal):
        self._signalOut= senyal
        
    @property
    def signalReference(self):
        return self._signalRef
    @signalReference.setter
    def signalReference(self, senyal):
        self._signalRef= senyal

    @property
    def scalarValue(self):
        return self._scalarOutput
    @scalarValue.setter
    def scalarValue(self, valor):
        self._scalarOutput= valor

    @property
    def vectorValue(self):
        return self._vectorOutput
    @vectorValue.setter
    def vectorValue(self, valor):
        self._vectorOutput= valor

    def qaResampling(self):
        '''
        basic resampling, based on the signal having less samples, assuming same sample time for each signal
        TODO: apply resampling method
        '''
        signaltemp= self._signalOut
        self._signalOut['magnitude']
        samplesOut= len(self._signalOut['magnitude'])
        samplesRef= len(self._signalRef['magnitude'])
        if samplesOut< samplesRef:
            signaltemp['magnitude']= self._signalRef['magnitude'][0:samplesOut]
            self._signalRef= signaltemp
        if samplesOut> samplesRef:
            signaltemp['magnitude']= self._signalOut['magnitude'][0:samplesRef]
            self._signalOut= signaltemp
        
        signaltemp= None