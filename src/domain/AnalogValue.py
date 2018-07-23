'''
Created on 3 aug. 2017
TODO substitute this class by the PyCIM:CIM16:IEC61970:Base:Meas:AnalogValue
@author: fragom
'''

class Analog(object):
    '''
    classdocs
    '''
    __max= 0
    __min= 0
    __meas= []
    
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
     
class AnalogValue(Analog):
    '''
    classdocs
    '''
    __value= 0.0
    __timestamp= 0.0

    def __init__(self, params):
        '''
        Constructor
        '''
    ''' getter/setter methods with _properties '''
    @property
    def value(self):
        return self.__value
    @value.setter
    def value(self, value):
        self.__value= value  
        
    @property
    def timestamp(self):
        return self.__timestamp
    @timestamp.setter
    def timestamp(self, value):
        self.__timestamp= value  
