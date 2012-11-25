#!/usr/bin/python
"""
    This program creates a .dat file with photon arrival times as
    it is produced by the FLEX correlators from correlator.com
    in photon history recorder mode by "Photon.exe".
    The generated files can be used to test multiple tau algorithm and
    workflow of SFCS analyzation programs.
"""

import numpy as np
import multipletauc
import csv

def MakeDat(linetime, noisearray, dtype, filename):
    """ Create a .dat file (like Photon.exe).
        System clock is fixed to 60MHz.
        linetime [s]
        noisearray integer array (uint16 or uint32)
    """
    NewFile = open(filename, 'wb')
    if dtype == np.uint32:
        newformat = np.uint8(32)
    elif dtype == np.uint16:
        newformat = np.uint8(16)
    else:
        raise ValueError
    newclock = np.uint8(60)
    NewFile.write(newformat)
    NewFile.write(newclock)
    noisearray = dtype(noisearray)
    # Creat matrix. Each line is scanned line with
    data = list()
    timeticks = linetime*60*1e6
    for i in np.arange(len(noisearray)):
        # Create a line
        N = noisearray[i]
        if N == 0:
            line=np.zeros(1, dtype=dtype)
            # Only one event at the far corner
            line[0] = 2*timeticks
            line.tofile(NewFile)
        else:
            line = np.ones(N+1, dtype=dtype)
            # events are included between two far events
            line[0] = line[-1] = timeticks
            line.tofile(NewFile)
    NewFile.close()


def OnSaveDat(filename, data):
    # Save the Data
    """
    Save experimental data as 32bit format.

    Raw data file format:
     1. The file records the difference in system clock ticks (1/60 us)
        between photon events.
     2. The first byte identifies the format of the file: 32 bit
     3. The second byte identifies the system clock: usually 60MHz.
     4. The time unit is 1/system clock.
     5. 32 bit format. 4 bytes represent a photon event, 
        time = 4 bytes/system clock
    """
    # Make a reasonable 32bit filename
    NewFile = open(filename, 'wb')
    newformat = np.uint8(32)
    newclock = np.uint8(60)
    NewFile.write(newformat)
    NewFile.write(newclock)
    data = np.uint32(data)
    data.tofile(NewFile)
    NewFile.close()


def GenerateExpNoise(N, taud=20., variance=1., deltat=1.):
    """
        Generate exponentially correlated noise.
    """
    # length of mean0 trace
    N_steps = N
    dt = int(deltat)
    # time trace
    t = np.arange(N_steps)
    # AR-1 processes - what does that mean?
    # time constant (inverse of correlationtime taud)
    g = 1./taud
    # variance
    s0 = variance
    
    # normalization factor (memory of the trace)
    exp_g = np.exp(-g*dt)
    one_exp_g = 1-exp_g
    z_norm_factor = np.sqrt(1-np.exp(-2*g*dt))/one_exp_g
    
    # create random number array
    # generates random numbers in interval [0,1)
    randarray = np.random.random(N_steps)
    # make numbers random in interval [-1,1)
    randarray = 2*(randarray-0.5)
    
    # simulate exponential random behavior
    z = np.zeros(N_steps)
    z[0] = one_exp_g*randarray[0]
    for i in np.arange(N_steps-1)+1:
        z[i] = exp_g*z[i-1] + one_exp_g*randarray[i]
        
    z = z * z_norm_factor*s0
    return z


def SaveCSV(G, trace, filename):
    """ Save correlation and trace tuple array G and trace to a .csv file
        that can be opened with FCSfit.
    """
    # Save Correlation function
    csvfile = filename
    openedfile = open(csvfile, 'wb')
    openedfile.write('# This file was created using testmultipletau.py\r\n')
    openedfile.write('# Channel (tau [s])'+" \t," 
                                     'Correlation function'+" \r\n")
    dataWriter = csv.writer(openedfile, delimiter=',')
    for i in np.arange(len(G)):
        dataWriter.writerow([str(G[i,0])+" \t", str(G[i,1])])

    openedfile.write('# BEGIN TRACE \r\n')
    openedfile.write('# Time ([s])'+" \t," 
                                     'Intensity Trace [kHz]'+" \r\n")


    for i in np.arange(len(trace)):
        dataWriter.writerow([str(trace[i,0])+" \t", str(trace[i,1])])


    openedfile.close()

# Line time to be ound by SFCS analyzation software
linetime = 0.000714
# Time of exponentially correlated noise
taudiff = 7. # in ms

noisearray = GenerateExpNoise(200000, taud=taudiff/linetime/1e3)
noisearray += np.abs(np.min(noisearray))
noisearray *= 30./np.max(noisearray)
noisearray = np.uint32(noisearray)

# Create 32bit and 16bit binary .dat files
data = MakeDat(linetime/2, noisearray, np.uint16, "test_"+str(taudiff)+"ms_16bit.dat")
data = MakeDat(linetime/2, noisearray, np.uint32, "test_"+str(taudiff)+"ms_32bit.dat")

# Create reference .csv file to check results
G = multipletauc.ACFromArray(np.float32(noisearray), deltat=linetime)
newtrace = multipletauc.BinTraceFromTrace(np.float32(noisearray), deltat=linetime, length=500)
SaveCSV(G, newtrace, "test_"+str(taudiff)+"ms_reference.csv")

