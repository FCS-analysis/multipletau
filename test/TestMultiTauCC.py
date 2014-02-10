# -*- coding: utf-8 -*-
""" Test Multiple Tau

    Create exponentially cross-correlated noise, apply multiple tau algorithm
    and save as .csv file (accessible via PyCorrFit).

    Author: Paul Müller
"""
import csv
import numpy as np
import matplotlib.pyplot as plt
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

def CreateCrossExp(taud=20., N=200000, variance=1.):
    # length of mean0 trace
    N_steps = N
    # time trace
    t = np.arange(N_steps)
    # AR-1 processes - what does that mean?
    # time constant (inverse of correlationtime taud)
    g = 1./taud
    # variance
    s0 = variance
    
    # normalization factor (memory of the trace)
    exp_g = np.exp(-g)
    one_exp_g = 1-exp_g
    z_norm_factor = np.sqrt(1-np.exp(-2*g))/one_exp_g
    
    # create random number array
    # generates random numbers in interval [0,1)
    randarray = np.random.random(N_steps)
    # make numbers random in interval [-1,1)
    randarray = 2*(randarray-0.5)
    
    # simulate exponential random behavior
    z = np.zeros(N_steps)
    z[0] = one_exp_g*randarray[0]
    for i in np.arange(N_steps-1)+1:
        for j in np.arange(i-1):
            z[i] += exp_g**j*randarray[i-j]
        z[i] += one_exp_g*randarray[i]
        
    z = z * z_norm_factor*s0
    randarray = randarray * z_norm_factor*s0
    return z, randarray


    
def SaveCSV(G, trace, filename, secondtrace=None):
    # Save Correlation function
    csvfile = filename
    openedfile = open(csvfile, 'wb')
    openedfile.write('# This file was created using testmultipletau.py\r\n')
    openedfile.write('# Channel (tau [s]) \t Correlation function \r\n')

    dataWriter = csv.writer(openedfile, delimiter='\t')
    for i in np.arange(len(G)):
        dataWriter.writerow([ str("%.10e")%G[i,0], str("%.10e")%G[i,1] ])

    openedfile.write('# BEGIN TRACE \r\n')
    openedfile.write('# Time ([s]) \t Intensity Trace [kHz] \r\n')


    for i in np.arange(len(trace)):
        dataWriter.writerow([ str("%.10e")%trace[i,0], str("%.10e")%trace[i,1] ])

    if secondtrace is not None:
        openedfile.write('# BEGIN SECOND TRACE \r\n')
        openedfile.write("# Type AC/CC \t Cross-Correlation \r\n")
        openedfile.write('# Time ([s]) \t Intensity Trace [kHz]  \r\n')
        for i in np.arange(len(trace)):
            dataWriter.writerow([ str("%.10e")%secondtrace[i,0],
                                  str("%.10e")%secondtrace[i,1] ])

    openedfile.close()
            

# Edit parameters
N = 20000
countrate = 25000. # in kHz
taudiff = 33. # in us
deltat = 2e-6 # time discretization [s]

# Do not edit
taudiff *= 1e-6/deltat
datab, dataa = CreateCrossExp(N=N, taud=taudiff)
countrate *= deltat*1000 # since we want kHz instead of Hz

print "Created traces"
GACa = multipletauc.ACFromArray(np.float32(dataa+countrate), deltat=deltat)
GACb = multipletauc.ACFromArray(np.float32(datab+countrate), deltat=deltat)
print "Created C-funcs"
# We set one bin to 1e-6 s.
GCCab = multipletauc.CCFromArray(np.float32(dataa+countrate), np.float32(datab+countrate/2), deltat=deltat)
GCCba = multipletauc.CCFromArray(np.float32(datab+countrate/2), np.float32(dataa+countrate), deltat=deltat)
# PyCorrFit loads intensity traces in kHz, we do not need to edit *countrate* here.
newtracea = multipletauc.BinTraceFromTrace(np.float32(dataa+countrate), deltat=deltat, length=500)
newtraceb = multipletauc.BinTraceFromTrace(np.float32(datab+countrate/2), deltat=deltat, length=500)

SaveCSV(GACa, newtracea, "testACa.csv")
SaveCSV(GACb, newtraceb, "testACb.csv")
SaveCSV(GCCab, newtracea, "testCCab.csv", secondtrace = newtraceb)
SaveCSV(GCCba, newtracea, "testCCba.csv", secondtrace = newtraceb)

