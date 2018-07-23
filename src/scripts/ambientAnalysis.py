'''
Created on 3 aug. 2017

@author: fragom
'''
import os, sys
from methods import MethodAmbientAnalysis
from inout.streamh5cim import StreamH5CIM
from methods.qualitativeAnalysis import QualitativeAnalysis

# Analysis Engine Methods
class AmbientAnalysis(object):
    
    __analysisTask= None
    
    def selectData(self, arrayQualquiera, mensaje):
        count= 0
        indexMapping={}
        for i, meas in enumerate(arrayQualquiera):
            print '[%d] %s' % (i, meas)
            indexMapping[count]= i
            count+= 1
        try:
            value= raw_input(mensaje)
            lindex = value.split()
        except ValueError:
            print "Wrong choice ...!" 
        values= []
        for idx in lindex:  
            idx= int(idx)
            values.append(arrayQualquiera[indexMapping[idx]])
        return values

    def open_database(self, simulationdbfile, measurementsdbfile= ''):
        ''' considers the option of not having measurement thus, 
        @param measurementsdbfile is empty '''
        self.__simulationdb= StreamH5CIM('./db/simulation', simulationdbfile)
        self.__simulationdb.open(simulationdbfile, mode= 'r')
        if not measurementsdbfile == '':
            self.__measurementdb= StreamH5CIM('./db/measurements', measurementsdbfile)
            self.__measurementdb.open(measurementsdbfile, mode= 'r')
        else:
            self.__measurementdb= None
        ''' return '''
        return [self.__simulationdb, self.__measurementdb]
        
    def select_Signals(self, simulationdb, measurementdb= None):
        ''' give the chance to analyze one or two signals 
        @return py.dict with (x,y) values for the signal (x= sampletime, y= magnitude)'''
        self.__simulationSignal= self.__measurementSignal= []
        arrayQualquiera= self.__simulationdb.select_arrayMeasurements(self.__simulationdb.networkName)
        seleccion= self.selectData(arrayQualquiera, 'Select a signal: ')
        ''' only allow one value selected '''
        names= seleccion[0].split('.')
        componentName= names[0]
        variableName= '.'.join(names[1:]) if len(names)> 2 else names[1]
#         [componentName, variableName]= seleccion[0].split('.')
        self.__simulationdb.select_PowerSystemResource(componentName)
        self.__simulationdb.select_AnalogMeasurement(variableName)
        self.__simulationSignal= self.__simulationdb.analogMeasurementValues
        if not measurementdb== None:
            arrayQualquiera= self.__measurementdb.select_arrayMeasurements(self.__measurementdb.networkName)
            seleccion= self.selectData(arrayQualquiera, 'Select a signal: ')
            ''' only allow one value selected '''
            [componentName, variableName]= seleccion[0].split('.')
            self.__measurementdb.select_PowerSystemResource(componentName)
            self.__measurementdb.select_AnalogMeasurement(variableName)
            self.__measurementSignal= self.__measurementdb.analogMeasurementValues
        else:
            self.__measurementSignal= {}
        ''' return '''
        return [self.__simulationSignal, self.__measurementSignal]
        
    def onStart_basicMethod(self, simulationSignal, order, measurementSignal= {}):
        self.__analysisTask = MethodAmbientAnalysis(simulationSignal,measurementSignal, order)
        self.__analysisTask.toolDir= os.getcwd()
        self.__analysisTask.taskFinished.connect(self.onFinish_basicMethod)
        self.__analysisTask.start()
        self.__analysisTask.wait()
            
    def onFinish_basicMethod(self, compareWithMeasurements= False):
        os.chdir(self.__analysisTask.toolDir)
        self.__analysisTask.gather_EigenValues()
        print 'Modes from Simulation'
        for mode in self.__analysisTask.simulationModes:
            print 'frequency: %s; damping: %s'%(str(mode.real), str(mode.imag))
        print 'Modes from Measurements'
        if compareWithMeasurements:
            for mode in self.__analysisTask.measurementModes:
                print 'frequency: %s; damping: %s'%(str(mode.real), str(mode.imag))
        
if __name__ == '__main__':
    analysisapi= AmbientAnalysis()
    if len(sys.argv)<= 3:
        [simulationTable, measurementTable]= analysisapi.open_database(sys.argv[1], '')
        [simulationSignal, measurementSignal]= analysisapi.select_Signals(simulationTable, measurementTable)
        analysisapi.onStart_basicMethod(simulationSignal, sys.argv[2], measurementSignal)
        analysisapi.onFinish_basicMethod(False)
    else:
        [simulationTable, measurementTable]= analysisapi.open_database(sys.argv[1], sys.argv[3])
        [simulationSignal, measurementSignal]= analysisapi.select_Signals(simulationTable, measurementTable)
        analysisapi.onStart_basicMethod(sys.argv[2], simulationSignal, measurementSignal)
        analysisapi.onFinish_basicMethod(True)
    quala= QualitativeAnalysis(simulationSignal, measurementSignal)
    quala.signal_plot()
    