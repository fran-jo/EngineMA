'''
Created on 3 aug. 2017

@author: fragom
'''

class Measurement(object):
    '''
    classdocs
    '''
    __max= 0
    __min= 0
    __mode= []
    
    def __init__(self, params):
        '''
        Constructor
        '''
    @property
    def max(self):
        return self.__max
    @max.setter
    def max(self, value):
        self.__max= value  
        
    @property
    def min(self):
        return self.__min
    @min.setter
    def min(self, value):
        self.__min= value  

class EigenValue(Measurement):
    '''
    classdocs
    '''
    __real= 0.0
    __imag= 0.0

    def __init__(self, real= 0.0, imag= 0.0):
        '''
        Constructor
        '''
        self.__real= real
        self.__imag= imag
        
    @property
    def real(self):
        return self.__real
    @real.setter
    def real(self, value):
        self.__real= value  
        
    @property
    def imag(self):
        return self.__imag
    @imag.setter
    def imag(self, value):
        self.__imag= value
