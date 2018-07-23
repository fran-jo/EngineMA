'''
Created on 24 Aug 2017
@author: fran_jo
'''

import h5py as h5
import collections
from CIM16.IEC61970.Base.Meas import Analog, AnalogValue
from CIM16.IEC61970.Base.Core import PowerSystemResource

'''TODO: use of PyCIM classes and method write ''' 
class StreamH5CIM(object):
    '''
    classdocs
    '''
    __gModel= None
    __gPowerSystemResource= None
    __ganalogMeasurement= None
    __danalogValue= None
    __internalModel= {}
    __internalMeasurement= {}
    '''create a dictionary with id,class as elements '''
    
    def __init__(self, dbpath= '', network= ''):
        '''
        Constructor
        dbpath= folder where to locate h5 files
        resFile= instances of a SimRes object with result file
        '''
        self.__dbfolder= dbpath
        if '.' in network:
            self.__h5namefile= dbpath+ '/'+ network
        else:
            self.__h5namefile= dbpath+ '/'+ network+ '.h5'
    
    def open(self, networkname= '', mode= 'r'):
        ''' h5name is name of the model '''
        if '.' in networkname:
            self.__networkname= networkname.split('.')[0]
        self.__h5file= h5.File(self.__h5namefile, mode)
        if self.__networkname in self.__h5file:
            self.__gmodel= self.__h5file[self.__networkname]

    def close(self):
        self.__h5file.close()
       
    @property 
    def modelName(self):
        return self.__gmodel.name
    
    @property
    def analogMeasurement(self):
        return self.__ganalogMeasurement.name
    
    @property
    def analogMeasurementValues(self):
        return self.__internalMeasurement
    
    @property
    def internalModel(self):
        return self.__internalModel

    @property
    def networkName(self):
        return self.__networkname
    
    def select_arrayMeasurements(self, networkname):
        ''' network name is the name of the h5 file '''
        signalNames= []
        for psres in self.__gmodel.keys():
            self.__gPowerSystemResource= self.__gmodel[psres]
            for meas in self.__gPowerSystemResource.keys():
                signalFullName= psres+ '.'+ meas
                signalNames.append(signalFullName)
        return signalNames
    
    def select_treeMeasurements(self, networkname):
        ''' build a dictionary with the name of the groups '''
        arbol = {}
        senyals= []
        for psres in self.__gmodel.keys():
            self.__gPowerSystemResource= self.__gmodel[psres]
            for meas in self.__gPowerSystemResource.keys():
                senyals.append(meas)
            arbol[psres]= senyals
            senyals= []
#         self.__select_iGroups(self.__gmodel, raiz_element, arbol)
        arbol= collections.OrderedDict(sorted(arbol.items()))
        return arbol
    
    def exist_PowerSystemResource(self, resource):
        if not resource in self.__gmodel:
            return False
        else:
            return True
            
    def select_PowerSystemResource(self, resource):
        ''' TODO: create UUID and mRID automatically '''
        self.__gPowerSystemResource= self.__gmodel[resource]
        powsysres= PowerSystemResource(mRID='someting_PowerSystemResource', 
                                       name= self.__gPowerSystemResource.name,
                                       UUID='someting_PowerSystemResource')
        return powsysres
    
    @property
    def powerSystemResource(self):
        return self.__gPowerSystemResource.name

    def exist_AnalogMeasurement(self, variable):
        if not variable in self.__gPowerSystemResource:
            return False
        else:
            return True
    
    def select_AnalogMeasurement_CIM(self, variable):
        ''' TODO: create UUID and mRID automatically '''
        manyAValues= []
        self.__ganalogMeasurement= self.__gPowerSystemResource[variable]
        aMeas= Analog(mRID= 'something_Analog', name= self.__ganalogMeasurement.name,
                      UUID= 'something_Analog')
        self.__danalogValue= self.__ganalogMeasurement['AnalogValue']
        i= 0
        for sample, valor in zip(self.__danalogValue[:,0],
                         self.__danalogValue[:,1]):
            localmRID= 'analogValue_'+ str(i)
            aValue= AnalogValue(value= valor, timeStamp= sample,
                                mRID= localmRID, UUID= localmRID)
            manyAValues.append(aValue)
            self.__internalModel[aValue.UUID]= aValue
            i= i+1
        aMeas.setAnalogValues(manyAValues)
        self.__internalModel[aMeas.UUID]= aMeas
        return aMeas
    
    def select_AnalogMeasurement(self, variable):
        self.__ganalogMeasurement= self.__gPowerSystemResource[variable]
#         senyal['unitSymbol']= self.__ganalogMeasurement['unitSymbol']
#         senyal['unitMultiplier']= self.__ganalogMeasurement['unitMultiplier']
#         senyal['measurementType']= self.__ganalogMeasurement['measurementType']
        self.__internalMeasurement['sampleTime']= self.__ganalogMeasurement['AnalogValue'][:,0]
        self.__internalMeasurement['magnitude']= self.__ganalogMeasurement['AnalogValue'][:,1]
    