'''
Created on 20 jan 2016

@author: fragom
'''

import numpy as np
from scipy import linalg
from quantitativeAnalysis import QuantitativeAnalysis

    
class EigenvalueAnalysis(QuantitativeAnalysis):
    '''
    classdocs
    '''
    __eraresOut= None
    __eraresRef= None

    def __init__(self, params):
        '''
        Constructor
        '''
        super(EigenvalueAnalysis, self).__init__(params)
#         self.__eraresOut= DataERA()
#         self.__eraresRef= DataERA()

    def get_erares_out(self):
        return self.__eraresOut


    def get_erares_ref(self):
        return self.__eraresRef


    def set_erares_out(self, value):
        self.__eraresOut = value


    def set_erares_ref(self, value):
        self.__eraresRef = value


    def del_erares_out(self):
        del self.__eraresOut


    def del_erares_ref(self):
        del self.__eraresRef


    def compute_method(self,  parametro= None):
        ''' eigenvalues and eigen vectors '''
        #first era method
#         self.__eraresOut.A, self.__eraresOut.B, self.__eraresOut.C = mr.compute_ERA_model(np.array(self._signalOut), 2)
        # second, eigenvalues and eigenvectors
        self.__eraresOut.lambdaValues, self.__eraresOut.lambdaVector = linalg.eig(self.__eraresOut.A)
#         self.__eraresRef.A, self.__eraresRefB, self.__eraresRefC = mr.compute_ERA_model(np.array(self._signalRef), 2)
        # second, eigenvalues and eigenvectors
        self.__eraresRef.lambdaValues, self.__eraresRef.lamdaVector = linalg.eig(self.__eraresRef.A)
        
    eraResOut = property(get_erares_out, set_erares_out, del_erares_out, "eraresOut's docstring")
    eraResRef = property(get_erares_ref, set_erares_ref, del_erares_ref, "eraresRef's docstring")
    
    def analyze_ERA(self):
        '''
        _measSignal as output
        _simSignal as input
        '''
        self.engineERA= EigenvalueAnalysis([self.simulationSignal.magnitude,
                                       self.referenceSignal.magnitude])
#         self.engineERA.signalOut= 
#         self.engineERA.signalRef= 
        self.engineERA.compute_method()
        print 'From simulation outputs: '
        print 'A= ', self.engineERA.eraResOut.A
        print 'B= ', self.engineERA.eraResOut.B
        print 'C= ', self.engineERA.eraResOut.C
        print 'From reference outputs: '
        print 'A= ', self.engineERA.eraResRef.A
        print 'B= ', self.engineERA.eraResRef.B
        print 'C= ', self.engineERA.eraResRef.C
    
        
