'''
Created on 22 jan 2016

@author: fragom
'''

import sys, os
from modelicares import SimRes
from inout.streamcimh5 import StreamCIMH5
from inout.streammatfile import InputMATStream

    
def selectData(arrayQualquiera, mensaje):
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
    
def mat_to_h5(matFile='.mat', compiler= 'openmodelica'):
    ''' .mat files resulting from Dymola or OpenModelica simulation 
    use of ModelicaRes library'''
    sourcemat= InputMATStream(matFile, compiler)
    networkname= matFile.split('.')[1].split('/')[-1]
    h5name= networkname + '.h5'
    dbh5= StreamCIMH5('./db/measurements', h5name)
    dbh5.open(h5name, 'w')
    sourcemat.load_components()
    componentsName= selectData(sourcemat.components, 'Select which component data to import: ')
    sourcemat.load_variables(componentsName)
    componentsSignals= zip(componentsName,sourcemat.variables)
    for componentname, componentSignal in componentsSignals:
        variablesName= selectData(componentSignal, 'Select which signals from components to import: ')
        # TODO supose user only select 2 variabler per component, what if selects more?
        sourcemat.load_signals(componentname, variablesName)
        if not dbh5.exist_PowerSystemResource(componentname):
            dbh5.add_PowerSystemResource(componentname)
        else:
            dbh5.update_PowerSystemResource(componentname,componentname)
        for variable in variablesName:
            paramName= componentname+ '.'+ variable
            if not dbh5.exist_AnalogMeasurement(variable):
                dbh5.add_AnalogMeasurement(variable)
                dbh5.add_AnalogValue(sourcemat.senyal['sampletime'], 
                                     sourcemat.senyal[paramName])
            else:
                dbh5.update_AnalogMeasurement(variable)
                dbh5.update_AnalogValue(variable,sourcemat.senyal['sampletime'], 
                                     sourcemat.senyal[paramName])
    dbh5.close()

if __name__ == '__main__':  
    mat_to_h5(sys.argv[1], sys.argv[2])
