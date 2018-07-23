'''
Created on 26 maj 2015

@author: fragom
'''

from __builtin__ import str

class Signal(object):
    '''
    classdocs, clase base trabaja con complejos
    '''
    
    _samples= 0
    _signal = []
    _component= ''
    _unit= 'p.u.'
    _systemBase= 0
        
    def __init__(self):
        '''
        Constructor
        '''


    def get_samples(self):
        ''' return the number of samples of the singal '''
        return self._samples

    def set_samples(self, value):
        ''' _value: input sample/time array '''
        self._samples = len(value)
        
    def del_samples(self):
        del self._samples
        
    def get_signal(self):
        ''' return the signal in rectangular form '''
        return self._signal
    
    def get_sampleTime(self):
        ''' returns an array with values of sample/time '''
        series= []
        for s,r,i in self._signal:
            series.append(s)
        return series 
    
    def get_signalReal(self):
        ''' returns an array with real component of the signal'''
        series= []
        for s,r,i in self._signal:
            series.append(r)
        return series    
        
    def get_signalImaginary(self):
        ''' returns an array with imaginary component of the signal '''
        series= []
        for s,r,i in self._signal:
            series.append(i)
        return series
        
    def set_signal(self, samples, firstPart, secondPart):
        ''' create dictionary with real part of the complex signal
        _samples:
        _valueR: '''
        self._signal= [(s,r,i) for s,r,i in zip(samples, firstPart, secondPart)]
        self._samples= len(self._signal)
        
    def del_signal(self):
        del self._signal
        
    def get_component(self):
        ''' returns the name of the component which the signal belongs to '''
        return self._component  

    def set_component(self, value):
        ''' set the name of the component which the signal belongs to '''
        self._component = value

    def del_component(self):
        del self._component

    def get_unit(self):
        return self._unit

    def set_unit(self, value):
        self._unit = value
    
    def del_unit(self):
        del self._unit

    def get_system_base(self):
        return self._systemBase

    def set_system_base(self, value):
        self._systemBase = value

    def del_system_base(self):
        del self._systemBase
        
    def __str__(self):
        pencil= []
        pencil.append(self._component)
        pencil.append(" in (")
        pencil.append(self._unit)
        pencil.append(") - ")
        pencil.append(self._samples)
        pencil.append(" samples")
        estrin= ''.join(pencil)
        return estrin
    
    def __repr__(self):
        return self.__str__()
    
    samples = property(get_samples, set_samples, del_samples, "samples's docstring")
    signal = property(get_signal, set_signal, del_signal, "signal's doctring")
    sampletime= property(get_sampleTime, "signal's doctring")
    magnitude = property(get_signalReal, "signal's doctring")
    phase= property(get_signalImaginary, "signal's doctring")
    component = property(get_component, set_component, del_component, "component's docstring")
    unit = property(get_unit, set_unit, del_unit, "unit's docstring")
    systemBase = property(get_system_base, set_system_base, del_system_base, "systemBase's docstring")
        
 
# class SignalPMU(Signal):
#     '''
#     classdocs
#     '''
# 
#     def __init__(self):
#         '''
#         Constructor, clase que trabaja con representacion polar'''
#         ''' oye, convierte las arrays en dictionarios, el key value siempre must be el tiempo, so
#         self.signal = {(magnitude, angle)}
#         '''
#         Signal.__init__(self)
#     
#     def get_magnitude(self):
#         ''' returns an array with magnitude component of the signal '''
#         series= []
#         for s,m,p in self._signal:
#             series.append(m)
#         return series    
#         
#     def get_phase(self):
#         ''' returns an array with phase component of the signal '''
#         series= []
#         for s,m,p in self._signal:
#             series.append(p)
#         return series    
#     
#     magnitude = property(get_magnitude, "signal's doctring")
#     phase= property(get_phase, "signal's doctring")
