# -*- coding: utf-8 -*-
""" Binning Data for Multiple Tau Algorithm
    Paul Müller, Biotec - TU Dresden

    As fast as you can get with python, binning the photon arrival times
    created by Photon.exe from correlator.com.

    See at the end of the file, which .dat file will be opened.
    In console, we ask for binning time in µs and an .int file
    is created.
"""

#import codecs, sys, win32console
import sys
import numpy as np                  # NumPy
# See cython documentation for following stuff
# "cimport" is used to import special compile-time information
# about the numpy module (this is stored in a file numpy.pxd which is
# currently part of the Cython distribution).
cimport numpy as np
# We now need to fix a datatype for our arrays. I've used the variable
# DTYPE for this, which is assigned to the usual NumPy runtime
# type info object.
DTYPEuint32 = np.uint32
DTYPEuint16 = np.uint16
# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.uint32_t DTYPEuint32_t
ctypedef np.uint16_t DTYPEuint16_t

# Negative indices are checked for and handled correctly. The code is
# explicitly coded so that it doesn’t use negative indices, and it (hopefully) 
# always access within bounds. We can add a decorator to disable bounds checking:
cimport cython
#@cython.boundscheck(False) # turn of bounds-checking for entire function
#def function():

# Vector to use as a list
#from libcpp.vector cimport vector



#Current
@cython.boundscheck(False) # turn of bounds-checking for entire function
def OpenDat(filename):
    # Open a data file
    """
    We open a .dat file as produced by the "Flex02-12D" correlator in photon
    history recorder mode.
    The file contains the time differences between single photon events.

    Returns:
    This function makes the filename publicly available, bins a couple
    of events to get 1e+6 points and plots them into the plotting area
    (plotarea), using the Bin_Photon_Events() function.

    Raw data file format (taken from manual):
     1. The file records the difference in system clock ticks (1/60 us)
        between photon event.
     2. The first byte identifies the format of the file 8 : 8 bit, 16: 16 bit
     3. The second byte identifies the system clock. 60MHz.
     4. The time unit is 1/system clock.
     5. 16 bit format. Each WORD (2 bytes) represents a photon event, 
        time = WORD/system clock, unless the value is 0xFFFF, in which case, 
        the following four bytes represent a photon event.
     6. 8 bit format: Each BYTE represents a photon event unless the value is 
        0xFF, in which case, the BYTE means 255 clock ticks passed without a 
        photon event. For example 0A 0B FF 08 means there are three
        photon events. The time series are 0x0A+1, 0x0B+1, 0xFF+8+1.

    """
    cdef np.ndarray[DTYPEuint16_t] Data
    cdef np.ndarray[DTYPEuint32_t] datData
    cdef int i, N
    # open file
    File = open(filename, 'rb')
    # 1st byte: get file format
    # should be 16 - for 16 bit
    format = int(np.fromfile(File, dtype="uint8", count=1))
    if format == 8:
        # No 8 bit format supported
        print 'Error 8 bit format not supported.'
        return None
    # 2nd byte: read system clock
    system_clock = int(np.fromfile(File, dtype="uint8", count=1))

    # There is an utility to convert data to 32bit. This makes life easier:
    if format == 32:
        datData = np.fromfile(File, dtype="uint32", count=-1)
        return  system_clock, datData
    # In case of 16 bit file format (assumed), read the rest of the file in
    # 16 bit format.
    # Load bunch of Data
    Data = np.fromfile(File, dtype="uint16", count=-1)
    File.close()

    # Now we need to check if there are any 0xFFFF values which would
    # mean, that we do not yet have the true data in our array.
    # There is 32 bit data after a 0xFFFF = 65535
    print "Searching for 32bit events."
    occurences = np.where(Data == 65535)[0]
    N = len(occurences)
    print "Found "+str(N)+" 32bit events."
    # Make a 32 bit array
    datData = np.uint32(Data)

    for i in occurences:
        # The following two events represent the actual event
        # Convert 2*16bit uint to 1*32bit uint:
        datData[i] = np.uint32(Data[i+1]) + np.uint32(Data[i+2])*65536

    print "Added new 32 bit array. Finishing..."

    # Now delete the zeros
    zeroids = np.zeros(N*2)
    for i in range(N):
        zeroids[i*2] = occurences[i]+1
        zeroids[i*2+1] = occurences[i]+2
    
    datData = np.delete(datData, zeroids)

    del Data
    return system_clock, datData


@cython.boundscheck(False) # turn of bounds-checking for entire function
def BinData(np.ndarray[DTYPEuint32_t] data, double t_bin, filename):
    cdef int N = len(data)
    BinData = []
    time_c = 0.0                 # time counter
    cdef int phot_c = 0                        # photon counter
    cdef int maxphot = 0
    cdef int j, i, emptybins, bin

    dtype=np.uint16

    newfilename = filename[:-4]+".int"

    print "Creating file "+newfilename

    NewFile = open(newfilename, 'wb')
    TempTrace = list()

    for j in range(100):
        percent = str(j)
        sys.stdout.write("\r Counting photons: "+percent+"%")
        sys.stdout.flush()

        for i in range(N/100):
            i = i+N/100*j
            time_c += data[i]

            if time_c >= t_bin:
                # Append counted photons and
                # reset counters
                #NewFile.write(dtype(phot_c))
                TempTrace.append(phot_c)
                time_c -=  t_bin
                phot_c = 0
                # Empty bins between this and next event:
                emptybins = int(time_c/t_bin)
                #NewFile.write(dtype(np.zeros(emptybins)))
                for bin in np.arange(emptybins):
                    # Does not matter if emptybins is "0"
                    #NewFile.write(dtype(0))
                    TempTrace.append(0)
                time_c -=  emptybins*t_bin
                # Equivalent to:
                # time_c = int(time_c)%int(t_bin)
            phot_c +=  1
        NewFile.write(dtype(TempTrace))
        TempTrace = list()


    # Now write the rest:
    for i in range(N/100*100,N-1):
        time_c += data[i]
        if time_c >= t_bin:
            # Append counted photons and
            # reset counters
            #NewFile.write(dtype(phot_c))
            TempTrace.append(phot_c)
            time_c -=  t_bin
            phot_c = 0
            # Empty bins between this and next event:
            emptybins = int(time_c/t_bin)
           # NewFile.write(dtype(np.zeros(emptybins)))
            for bin in range(emptybins):
                # Does not matter if emptybins is "0"
                #NewFile.write(dtype(0))
                TempTrace.append(0)
            time_c -=  emptybins*t_bin
            # Equivalent to:
            # time_c = int(time_c)%int(t_bin)
        phot_c +=  1
    NewFile.write(dtype(TempTrace))
    TempTrace = list()



    sys.stdout.write("\r Counting photons: 100%")
    sys.stdout.flush()
    sys.stdout.write("\r \r\n") # clean up stdout
    NewFile.write(dtype(TempTrace))
    NewFile.close()

    return True

