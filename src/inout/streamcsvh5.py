'''
Created on 7 apr 2015

@author: fragom
'''
from datetime import datetime
import pandas as panda

class StreamCSVH5(object):
    '''
    Class observer for PMU data, in .csv file format from PMU 
    TODO: handle saving/loading data from the simulation engine 
    _csvFile file object with reference to the .csv file
    cgroup object to keep in memory a group from the .h5 file
    cdataset objet to keep in memory the dataset of signals from the .h5 file
    '''
    _csvFile= None
    _header= []
    _senyal= {}

    def __init__(self, sourceFile, delimiter=','):
        '''
        Constructor
        _sourceFile: .csv file path
        _delimiter: delimiter of fields
        '''
        # TODO solve the issue of signal length
        self._csvFile= panda.read_csv(sourceFile, sep=delimiter, nrows=1000)
        
    @property 
    def fileName(self):
        return self._csvFile
    @fileName.setter
    def fileName(self, value):
        self._csvFile= value
        
    @property 
    def header(self):
        return self._header
    @header.setter
    def header(self, value):
        self._header = value
    
    @property
    def senyal(self):
        return self._senyal
       
    def timestamp2sample(self, variable):
        tiempos= [datetime.strptime(x,"%Y/%m/%d %H:%M:%S.%f") for x in self._senyales[variable].get_sampleTime()]
        sampletime= [(t- tiempos[0]).microseconds/1000 for t in tiempos]
#         print sampletime
        return sampletime 
      
            
class InputCSVH5(StreamCSVH5):
    '''
    Class observer for PMU data, in .csv file format
    Header format: 
    '''
    def __init__(self, sourceFile, delimiter=','):
        print sourceFile
        super(InputCSVH5, self).__init__(sourceFile, delimiter)
    
    def load_csvHeader(self):
        self._header= list(self._csvFile.columns.values)
    
    def load_csvHeaderIdx(self, variable):
        return self._header.index(variable)
    
    def load_csvValues(self, nameSenyal):
        ''' Loads signal data from a specific variable form a specific component
        senyal: variable name of the signal, column name
        '''
        self._senyal['sampletime']= self._csvFile['Timestamp'].values
        self._senyal['magnitude']= self._csvFile[nameSenyal].values
    
    def timestamp2sample(self, timeSenyal):
        '''converts the timestamp value from pmu measurement into sample value as sample time 
        senyal is the corresponding Timestamp array from the pmu measurements
        '''
        tiempos= [datetime.strptime(x,"%Y/%m/%d %H:%M:%S.%f") 
                  for x in timeSenyal]
        sampletime= [(t- tiempos[0]).total_seconds()*1000 for t in tiempos]
        return sampletime
    
    def close_csv(self):
        self._csvFile.close()
        
