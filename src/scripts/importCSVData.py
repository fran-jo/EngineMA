'''
Created on 19 Sep 2017

@author: fran_jo
'''
import sys
from inout.streamcsvh5 import InputCSVH5
from inout.streamcimh5 import StreamCIMH5

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
    
def csv_to_h5(csvFile='.csv', delimiter= ','):
    sourcecsv= InputCSVH5(csvFile, delimiter)
    sourcecsv.load_csvHeader()
#         print sourcecsv.cheader
    h5name= csvFile.split('.')[1].split('/')[-1]
    dbh5= StreamCIMH5('./db/measurements', h5name)
    dbh5.open(h5name, 'w')
    measname= selectData(sourcecsv.header, 'Select which component data to import: ')
    for selectedMeas in measname:
        nameSplit= selectedMeas.split(':')
        componentname= nameSplit[0]
        parameterName= nameSplit[1]
        sourcecsv.load_csvValues(selectedMeas)
        if not dbh5.exist_PowerSystemResource(componentname):
            dbh5.add_PowerSystemResource(componentname)
        if not dbh5.exist_AnalogMeasurement(parameterName):
            dbh5.add_AnalogMeasurement(parameterName)
        dbh5.add_AnalogValue(sourcecsv.timestamp2sample(sourcecsv.senyal['sampletime']), 
                             sourcecsv.senyal['magnitude'])
    dbh5.close()

if __name__ == '__main__':
    csv_to_h5(sys.argv[1], sys.argv[2])