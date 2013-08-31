# -*- coding: utf-8 -*-
""" Test Multiple Tau
    Paul Mueller, Biotec - TU Dresden

    Create exponentially correlated noise, apply multiple tau algorithm
    and save as .csv file (accessible via FCSfit).
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
#import multipletau as multipletauc
import multipletauc

def GenerateExpNoise(N, taud=20., variance=1., deltat=1.):
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
    return z, t
    
    
def SaveCSV(G, trace, filename):
    # Save Correlation function
    csvfile = filename
    openedfile = open(csvfile, 'wb')
    openedfile.write('# This file was created using testmultipletau.py\r\n')
    openedfile.write('# Channel (tau [s]) \t Correlation function  \r\n')
    dataWriter = csv.writer(openedfile, delimiter='\t')
    for i in np.arange(len(G)):
        dataWriter.writerow([ str("%.10e")%G[i,0], str("%.10e")%G[i,1] ])

    openedfile.write('# BEGIN TRACE \r\n')
    openedfile.write('# Time ([s]) \t Intensity Trace [kHz]'+" \r\n")

    for i in np.arange(len(trace)):
        dataWriter.writerow([ str("%.10e")%trace[i,0], str("%.10e")%trace[i,1] ])

    openedfile.close()
            

# Edit parameters
N = 2780000
countrate = 250. # in kHz
taudiff = 55. # in us
deltat = 2e-6 # time discretization [s]

# Do not edit
taudiff *= 1e-6/deltat
data, times = GenerateExpNoise(N, taud=taudiff, deltat=1.)
countrate *= deltat*1000 # since we want kHz instead of Hz
# We set one bin to 1e-6 s.
G = multipletauc.ACFromArray(np.float32(data+countrate), deltat=deltat)
# FCSfit loads intensity traces in kHz, we do not need to edit *countrate* here.
newtrace = multipletauc.BinTraceFromTrace(np.float32(data+countrate), deltat=deltat, length=500)

SaveCSV(G, newtrace, "test.csv")






