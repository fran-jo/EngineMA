'''
Created on 12 feb 2016

@author: fragom
'''

import numpy as np
import matplotlib.pyplot as mplot
from statisticAnalysis import StatisticAnalysis
from control.matlab import damp

class QualitativeAnalysis(StatisticAnalysis):
    '''
    plots,
    reshaping data
    '''
    def __init__(self, signalSimulation, signalReference):
        '''
        Constructor
        '''
        StatisticAnalysis.__init__(self, signalSimulation, signalReference)
            
    def __signalError(self, arrayone, arraytwo):
        error= np.subtract(np.array(arrayone), np.array(arraytwo))
        #TODO error signal must be a new object signal with own sampletime
        return error
    
    def error_plot(self):
        errorSignal= self.__signalError(self._signalOut['magnitude'], 
                                        self._signalRef['magnitude'])
        mplot.style.use('ggplot')
        mplot.figure(1)
        mplot.subplot(211)
        mplot.plot(self._signalOut['sampleTime'], self._signalOut['magnitude'], label='Simulation signal')
        mplot.plot(self._signalRef['sampleTime'], self._signalRef['magnitude'], label='Reference signal')
        mplot.title('Qualitative Analysis')
        mplot.xlabel('Time (s)')
        mplot.ylabel('Value')
        mplot.legend(loc='lower right', shadow=True, fontsize='x-small')
        mplot.grid(True)
        mplot.subplot(212)
        mplot.plot(self._signalRef['sampleTime'], errorSignal, 'r-', label='Difference')
        mplot.xlabel('Time (s)')
        mplot.ylabel('Value')
        mplot.legend(loc='lower right', shadow=True, fontsize='x-small')
        mplot.grid(True)
        mplot.show()
        
    def signal_plot(self):
        mplot.style.use('ggplot')
        mplot.figure(1)
        mplot.plot(self._signalOut['sampleTime'], self._signalOut['magnitude'], label='Simulation signal')
        if not self._signalRef== {}:
            mplot.plot(self._signalRef['sampleTime'], self._signalRef['magnitude'], label='Reference signal')
        mplot.title('Qualitative Analysis')
        mplot.xlabel('Time (s)')
        mplot.ylabel('Value')
        mplot.legend(loc='lower right', shadow=True, fontsize='x-small')
        mplot.grid(True)
        mplot.show()
        
    def polar_plot(self, simulationModes, measurementModes):
        '''
        simulationModes array of pairs (freq,damp)
        '''
        # 1st plot damping
        vfreq= []
        vdamp= []
        mplot.figure(1)
#         mplot.subplot(211)
        for mode in simulationModes:
            vfreq.append(mode.real)
            vdamp.append(mode.imag)
        mplot.scatter(np.array(vfreq), np.array(vdamp), c='r', marker= 'o')
        vfreq= []
        vdamp= []
        for mode in measurementModes:
            vfreq.append(mode.real)
            vdamp.append(mode.imag)
        mplot.scatter(np.array(vfreq), np.array(vdamp), c='b', marker= '+')
#         for i, txt in enumerate(values):
#             mplot.annotate(txt, (xdamp[i], values[i]))
        mplot.title('Modes')
        mplot.ylabel('Values')
        mplot.grid(True)
        mplot.show()
        
    def ERA_plot(self):
        for eigenvalue in self.engineERA.eraResOut.lambdaValues:
            mplot.scatter(eigenvalue.real, eigenvalue.imag)
        for eigenvalue in self.engineERA.eraResRef.lambdaValues:
            mplot.scatter(eigenvalue.real, eigenvalue.imag)
        limit_x= 1.2 # set limits for axis
        limit_y= 1.2 # set limits for axis
        mplot.axis([-limit_x, limit_x, -limit_y, limit_y])
        axisline= np.linspace(-limit_x, limit_y)
        zerosline= np.zeros(len(axisline))
        mplot.plot(axisline,zerosline,color='black')
        mplot.plot(zerosline,axisline,color='black')
        circulo= mplot.Circle((0,0), radius=1, color='black', fill=False)
        mplot.title('Eigenvalues')
        mplot.ylabel('Imaginary')
        mplot.xlabel('Real')
        mplot.grid(True)
        mplot.gcf().gca().add_artist(circulo)
        mplot.show()