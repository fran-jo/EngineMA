<p>
<h4>Using the Engine:</h4>
<h5>Mode estimation based on signal analysis</h5>
Script ./src/scripts/ambientAnalysis.py
<ul><b> $> ambientAnalysis.py 2AreaAVR_woNoise.h5 38 pmu_measurement_file.h5</b></ul>
Execute the script ambientAnalysis.py with 3 input arguments (last optional)
<li> Simulation results file (in folder ./db/simulation/)</li>
<li> Model order (value of the dimension of matrix A of the linear model)</li>
<li> (optional) Measurements results file (in folder ./db/measuremenets/)</li>

</p>

[1] database file of simulation outputs
[2] model order
[3] (optional) database file of field measurements

script prompts to a simple command line choice (multiple selection is not allowed)
[0] bus1.V
[1] bus2.V
[2] bus3.V
[3] bus4.V
[4] g1.g1.P
[5] g2.g2.P
[6] g3.g3.P
[7] g4.gENSAL.P
Select a signal:

Ambient Mode Analysis
Unrecognized MATLAB option "wait".

                            < M A T L A B (R) >
                  Copyright 1984-2016 The MathWorks, Inc.
                   R2016b (9.1.0.441655) 64-bit (maci64)
                             September 7, 2016
...
Once the mehtod finishes, the resulting modes are presented in the screen and a figures pops up, with the plot
of the selected signal.
Modes from Simulation
frequency: 1.31679628403e-06; damping: -1.0
frequency: 4.81409351418; damping: 0.00328727743857
frequency: 5.69047291672; damping: 0.0085946578019
frequency: 2.98897264524; damping: 0.0306614294269
frequency: 1.64405060447; damping: 0.0718355338439
frequency: 5.70647077501; damping: 0.420675797744
frequency: 3.54656839291; damping: 0.68194899557
frequency: 0.0687837120222; damping: 1.0
Modes from Measurements
(this section if empty if no database file is specified)

2) model analysis - linearization
	[1] ./config/simResources.properties
[1] stores the resources a.k.a. model files and library files to work with



The scripts have been tested within PyDev environment from Eclipse
