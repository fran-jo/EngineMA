'''
Created on 19 Sep 2017

@author: fran_jo
'''
import sys
from inout.streamh5cim import StreamH5CIM
from methods.quantitativeAnalysis import QuantitativeAnalysis
from methods.qualitativeAnalysis import QualitativeAnalysis
from inout.streammodeh5 import StreamModeH5

'''TODO relative path, with file name, as input, make it easy'''

def selectData(arrayQualquiera, mensaje):
    ''' TODO Add this method in a general class '''
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
    
def open_database(simulationdbfile, measurementsdbfile= ''):
    ''' TODO Add this method in a general class '''
    ''' considers the option of not having measurement thus, 
    @param measurementsdbfile is empty '''
    __simulationdb= StreamH5CIM('./db/simulation', simulationdbfile)
    __simulationdb.open(simulationdbfile, mode= 'r')
    if not measurementsdbfile == '':
        __measurementdb= StreamH5CIM('./db/measurements', measurementsdbfile)
        __measurementdb.open(measurementsdbfile, mode= 'r')
    else:
        __measurementdb= None
    ''' return '''
    return [__simulationdb, __measurementdb]
    
def select_Signals(simulationdb, measurementdb= None):
    ''' TODO Add this method in a general class '''
    ''' give the chance to analyze one or two signals 
    @return py.dict with (x,y) values for the signal (x= sampletime, y= magnitude)'''
    __simulationSignal= __measurementSignal= []
    arrayQualquiera= simulationdb.select_arrayMeasurements(simulationdb.networkName)
    seleccion= selectData(arrayQualquiera, 'Select a signal: ')
    ''' only allow one value selected '''
    [componentName, variableName]= seleccion[0].split('.')
    simulationdb.select_PowerSystemResource(componentName)
    simulationdb.select_AnalogMeasurement(variableName)
    __simulationSignal= simulationdb.analogMeasurementValues
    if not measurementdb== None:
        arrayQualquiera= measurementdb.select_arrayMeasurements(measurementdb.networkName)
        seleccion= selectData(arrayQualquiera, 'Select a signal: ')
        ''' only allow one value selected '''
        [componentName, variableName]= seleccion[0].split('.')
        measurementdb.select_PowerSystemResource(componentName)
        measurementdb.select_AnalogMeasurement(variableName)
        __measurementSignal= measurementdb.analogMeasurementValues
    ''' return '''
    return [__simulationSignal, __measurementSignal]

def signal_error(simulationSignal, referenceSignal):
    quanta= QuantitativeAnalysis(simulationSignal,referenceSignal)
    # analysis results to report 
    quanta.qaResampling()
    quanta.error_method('MAE')
    print "MAE= ", quanta.scalarValue
    quanta.error_method('MSE')
    print "MSE= ", quanta.scalarValue
    quanta.error_method('RMSE') 
    print "RMSE= ", quanta.scalarValue
    quanta.error_method('MBD') 
    print "MBD= ", quanta.scalarValue
    quala= QualitativeAnalysis(simulationSignal, referenceSignal)
    quala.error_plot()

def modeEst_error(simdb):
    dbmode= StreamModeH5(simdb)
    dbmode.open(StreamModeH5.VEDRAN_METHOD)
    __simulationModes= dbmode.select_modes('simulation')
    __measurementModes= dbmode.select_modes('measurement')
    print 'simulation modes'
    for mode in __simulationModes:
        print str(mode.real), ', j'+ str(mode.imag)
        print 'measurement modes'
    for mode in __measurementModes:
        print str(mode.real), ', j'+ str(mode.imag)
    dbmode.close()
    quala= QualitativeAnalysis([], [])
    quala.polar_plot(__simulationModes, __measurementModes)

if __name__ == '__main__':
#     [simdb, measdb]= open_database(sys.argv[1], sys.argv[2])
#     [simsignal, meassignal]= select_Signals(simdb, measdb)
#     signal_error(simsignal, meassignal)
    modeEst_error(sys.argv[1])