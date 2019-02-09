'''
Created on 7 apr 2015

@author: fragom
'''
import h5py as h5
from ema.domain.EigenValue import EigenValue
import numpy

class StreamModeH5(object):
    '''
    _h5file file object with reference to the .h5 file
    _group object to keep in memory a group from the .h5 file
    cdataset objet to keep in memory the dataset of signals from the .h5 file
    '''
    #basic enum definition
    MODE_RESULT_DB= 'mode_estimation_result.h5'
    VEDRAN_METHOD= 'vedran_method'
    __h5namefile= ''
    __h5file= None
    __resfolder= ''
    __gResults= None
    __dmode= None
    
    def __init__(self, directorio= '/', resfile= ''):
        '''
        Constructor
        dbpath= folder where to locate h5 files
        resFile= instances of a SimRes object with result file
        '''
        self.__h5namefile= directorio + '/'+ resfile
        
    def open(self, methodGroup, mode= 'r'):
        ''' 
        @param methodGroup, is the name of the main group, correspond to the method used
        @param mode '''
        self.__h5file= h5.File(self.__h5namefile, mode)
        self.__gResults= self.__h5file[methodGroup]
    
    def close(self):
        self.__h5file.close()
            
    def select_modes(self, whichsignal):
        ''' build an array of EigenValues '''
        modes= listmodes= []
        if whichsignal== 'simulation': 
            groupWithData= self.__gResults['simulationSignal']
            self.__dmode= groupWithData['modes']
        elif whichsignal== 'measurement':
            groupWithData= self.__gResults['measurementSignal']
            self.__dmode= groupWithData['modes']
        listmodes= self.__dmode[0:]
        iValues= len(listmodes[0]) if not listmodes[0].__class__== numpy.float64 else 1
        if iValues> 1:
            i= 0
            while i< iValues:
                mode= EigenValue(listmodes[0,i],listmodes[1,i])
                modes.append(mode)
                i= i+1
        else:
            mode= EigenValue(listmodes[0],listmodes[1])
            modes.append(mode)
        return modes
