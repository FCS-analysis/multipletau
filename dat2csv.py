# -*- coding: utf-8 -*-
""" Binning Data and performing Multiple Tau Algorithm
    Paul Müller, Biotec - TU Dresden

    As fast as you can get with python, binning the photon arrival times
    created by Photon.exe from correlator.com.

    See at the end of the file, which .dat file will be opened.
    In console, we ask for binning time in µs and an .int file
    is created.
"""

#import codecs, sys, win32console
import argparse
import csv
import sys
import numpy as np                  # NumPy
import os
import struct
import tempfile
import time
import zipfile


# c compiled modules
import binningc
import multipletauc

parser = argparse.ArgumentParser()
parser.add_argument('-w', '--tbin', type=float,
                    help='Width of bins in us')
parser.add_argument('input', metavar='INPUT', nargs='?', 
                    type=str, help='Input .dat file')
parser.add_argument('output', metavar='OUTPUT', nargs='?',
                    type=str, help='Output .csv file')

args = parser.parse_args()
p_tbin = args.tbin
p_infile = args.input
p_outfile = args.output

if p_infile is None:
    # Use a standard file
    filename = "./A488_50nMA.dat"
    #filename = "./w01-11A.dat"
    #filename = "./03_100s_pos4.dat"
else:
    filename = p_infile

#system_clock = None
# Also resets system_clock:
a=time.time()
system_clock, event_data = binningc.OpenDat(filename)
print "Finding Events: "+str(time.time()-a)+"s"

print "System clock: "+str(system_clock)+" MHz"

if event_data is None:
    print "Problem acquiring data."
    exit()

if p_tbin is None:
    t_bin = float(raw_input("Enter binning time in us:"))
else:
    t_bin = p_tbin

bintime = 1.*t_bin*system_clock


# Creates binned file
a=time.time()
binningc.BinData(event_data, bintime, filename)
print "binning time: "+str(time.time()-a)+"s"

## Perform multiple tau algorithm
# bintime from µs to s
deltat = t_bin/1e6

# File created by BinData:
newfilename = filename[:-4]+".int"

#trace = np.array(np.fromfile(newfilename, dtype="uint16", count=-1), dtype="float64")


# Calculate autocorrelation
a=time.time()
G_list = multipletauc.ACFromFile(newfilename, deltat, m=128)
print "multiple-tau time: "+str(time.time()-a)+"s"
Trace_list = multipletauc.BinTracesFromFile(newfilename, deltat, length=700)
print "Got traces."

if p_outfile is None:
    zipfilename = filename[:-4]+".zip"
else:
    zipfilename = p_outfile.strip(".zip")+".zip"

Arc = zipfile.ZipFile(zipfilename, mode='w')
returnWD = os.getcwd()
tempdir = tempfile.mkdtemp()
os.chdir(tempdir)

for j in np.arange(len(G_list)):

    # Write G to file
    G = G_list[j]
    if p_outfile is None:
        csvfile = filename[:-4]+"_"+str(j)+".csv"
    else:
        csvfile = p_outfile.strip(".csv")+"_"+str(j)+".csv"

    openedfile = open(csvfile, 'wb')
    openedfile.write('# Created with dat2csv\r\n')
    openedfile.write('# Paul Mueller - BIOTEC, TU Dresden\r\n')
    openedfile.write('# Info:\r\n')
    openedfile.write('#  Binning Time: '+str(deltat)+'s \r\n')
    openedfile.write('#  Source file: '+filename+'\r\n')
    openedfile.write('#  Source segment: '+str(j+1)+' of '+str(len(G_list))+'\r\n')
    openedfile.write('# Channel (tau [s])'+" \t," 
                                     'Correlation function'+" \r\n")

    dataWriter = csv.writer(openedfile, delimiter=',')

    for i in np.arange(len(G)):
        dataWriter.writerow([str(G[i,0])+" \t", str(G[i,1])])

    # Write Trace
    T = Trace_list[j]
    openedfile.write('#\r\n# BEGIN TRACE\r\n#\r\n')
    openedfile.write('# Trace time [s]'+" \t," 
                                     'Intensity trace [kHz]'+" \r\n")

    for i in np.arange(len(T)):
        dataWriter.writerow([str(T[i,0])+" \t", str(T[i,1])])

    openedfile.close()
    Arc.write(csvfile)
    os.remove(csvfile)
os.chdir(returnWD)
os.removedirs(tempdir)




