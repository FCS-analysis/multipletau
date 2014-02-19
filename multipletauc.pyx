# -*- coding: utf-8 -*-
""" Multiple Tau Algorithms
    Paul Müller, Biotec - TU Dresden
"""

import os
import numpy as np

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
DTYPEfloat64 = np.float64
DTYPEfloat32 = np.float32
# "ctypedef" assigns a corresponding compile-time type to DTYPE_t. For
# every type in the numpy module there's a corresponding compile-time
# type with a _t-suffix.
ctypedef np.uint32_t DTYPEuint32_t
ctypedef np.uint16_t DTYPEuint16_t
ctypedef np.float64_t DTYPEfloat64_t
ctypedef np.float32_t DTYPEfloat32_t

# Negative indices are checked for and handled correctly. The code is
# explicitly coded so that it doesn’t use negative indices, and it (hopefully) 
# always access within bounds. We can add a decorator to disable bounds checking:
cimport cython
#@cython.boundscheck(False) # turn of bounds-checking for entire function
#def function():

@cython.cdivision(True)
@cython.boundscheck(False) # turn of bounds-checking for entire function
def ACFromArray(np.ndarray[DTYPEfloat32_t] trace, double deltat, int m=16, copy=False):
    """ Apply the multiple tau algorithm to a float64 numpy array *trace*
        with time differences float *deltat*. Set copy to True to not
        manipulate the incoming *trace*. If set to False, this will
        help save memory. *m* is the number of bins to use for first
        *m* values of the correlation function.
        Needs trace array: Times in *deltat* and countrate in [kHz]

        Returns two arrays of tuples. 
        G: First element is the lagtime
           (same dimension as deltat) and second element is autocorrelation
           function.
        Trace: Times [s] and countrate [kHz]
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    G = []
    cdef int N = len(trace)
    cdef double traceavg = trace.mean(dtype="float")
    cdef int n, step, j
    cdef double Gtmp
    cdef np.ndarray[DTYPEfloat32_t] newtrace
    # We calculate the Autocorrelation function from deviations from zero
    trace -= traceavg
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(trace) must be larger than 2m")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(m):
        Gtmp = 0
        #Gtmp = np.sum(trace[:N-(n+1)]*trace[(n+1):], dtype=np.float64)
        for j in range(N-(n+1)):
            Gtmp += trace[j]*trace[j+n+1]
        # Normalize G(n)
        # Sutract 1, because we calculated G from signal,
        # not from signal deviations.
        Gtmp = 1.*Gtmp/((N-n-1)*traceavg**2)
        # Append to array
        G.append((deltat*(n+1), Gtmp))
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next few elements.
    if copy != False:
        # Create a copy of the trace instead of binning the given one.
        trace = 1.*trace
    ## Calculate how many times we may perform binning migth increase 
    ## performance ? No, we bin less than 10000 times.
    step = 0
    ## Bin the countrate array.
    # Add up every second element
    # Check if len(trace) is even:
    if N%2 == 1:
        N = N-1
    #trace = (trace[:N:2]+trace[1:N+1:2])/2.
    newtrace = np.zeros(N/2, dtype=np.float32)
    for j in range(N/2):
        newtrace[j] = (trace[2*j]+trace[2*j+1])/2.
    del trace
    trace = newtrace
    N = N/2
    while N >= m:
        step += 1
        # Check, if we could save the trace now
        # Get the next m/2 values of the trace
        for n in range(m/2):
            Gtmp = 0
            # We only need elements from m/2 on.
            # This saves computing time.
            ## Might be faster with arrays?
            #Gtmp = np.sum(trace[:N-(n+1+m/2)]*trace[(n+1+m/2):])
            for j in range(N-(n+1+m/2)):
                Gtmp += trace[j]*trace[j+n+1+m/2]
            # Normalize G(n)
            # Sutract 1, because we calculated G from signal,
            # not from signal deviations.
            Gtmp = 1.*Gtmp/((N-n-1-m/2)*traceavg**2)
            # Append to array
            G.append((deltat*(n+1+m/2)*2**step, Gtmp))
        # We put this in the end, because we want to break the while
        # loop when we will not be able to perform it anymore.
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N = N-1
        #trace = (trace[:N:2]+trace[1:N+1:2])/2.
        newtrace = np.zeros(N/2, dtype=np.float32)
        for j in range(N/2):
            newtrace[j] = (trace[2*j]+trace[2*j+1])/2
        del trace
        trace = newtrace
        N = N/2
    return np.array(G)

@cython.cdivision(True)
@cython.boundscheck(False) # turn of bounds-checking for entire function
def CCFromArray(np.ndarray[DTYPEfloat32_t] a, np.ndarray[DTYPEfloat32_t] b, double deltat, int m=16, copy=False):
    """ Apply the multiple tau algorithm to a float64 numpy array *trace*
        with time differences float *deltat*. Set copy to True to not
        manipulate the incoming *trace*. If set to False, this will
        help save memory. *m* is the number of bins to use for first
        *m* values of the correlation function.
        Returns two arrays of tuples. 
        G: First element is the lagtime
           (same dimension as deltat) and second element is autocorrelation
           function.
        Trace: Times [s] and intensities [kHz]
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    G = []
    cdef int N = len(a)
    cdef double traceavga = a.mean(dtype="float")
    cdef double traceavgb = b.mean(dtype="float")
    cdef int n, step, j
    cdef double Gtmp
    cdef np.ndarray[DTYPEfloat32_t] newtracea, newtraceb
    # We calculate the Autocorrelation function from deviations from zero
    a -= traceavga
    b -= traceavgb
    if N < 2*m:
        # Otherwise the following for-loop will fail:
        raise ValueError("len(trace) must be larger than 2m")
    ## Calculate autocorrelation function for first m bins
    # Discrete convolution of m elements
    for n in range(m):
        Gtmp = 0
        #Gtmp = np.sum(trace[:N-(n+1)]*trace[(n+1):], dtype=np.float64)
        for j in range(N-(n+1)):
            Gtmp += a[j]*b[j+n+1]
        # Normalize G(n)
        # Sutract 1, because we calculated G from signal,
        # not from signal deviations.
        Gtmp = 1.*Gtmp/((N-n-1)*traceavga*traceavgb)
        # Append to array
        G.append((deltat*(n+1), Gtmp))
    ## Now that we calculated the first m elements of G, let us
    ## go on with the next few elements.
    if copy != False:
        # Create a copy of the trace instead of binning the given one.
        a = 1.*a
        b = 1.*b
    ## Calculate how many times we may perform binning migth increase 
    ## performance ? No, we bin less than 10000 times.
    step = 0
    ## Bin the countrate array.
    # Add up every second element
    # Check if len(trace) is even:
    if N%2 == 1:
        N = N-1
    #trace = (trace[:N:2]+trace[1:N+1:2])/2.
    newtracea = np.zeros(N/2, dtype=np.float32)
    newtraceb = np.zeros(N/2, dtype=np.float32)
    for j in range(N/2):
        newtracea[j] = (a[2*j]+a[2*j+1])/2.
        newtraceb[j] = (b[2*j]+b[2*j+1])/2.
    del a
    del b
    a = newtracea
    b = newtraceb
    N = N/2
    while N >= m:
        step += 1
        # Check, if we could save the trace now
        # Get the next m/2 values of the trace
        for n in range(m/2):
            Gtmp = 0
            # We only need elements from m/2 on.
            # This saves computing time.
            ## Might be faster with arrays?
            #Gtmp = np.sum(trace[:N-(n+1+m/2)]*trace[(n+1+m/2):])
            for j in range(N-(n+1+m/2)):
                Gtmp += a[j]*b[j+n+1+m/2]
            # Normalize G(n)
            # Sutract 1, because we calculated G from signal,
            # not from signal deviations.
            Gtmp = 1.*Gtmp/((N-n-1-m/2)*traceavga*traceavgb)
            # Append to array
            G.append((deltat*(n+1+m/2)*2**step, Gtmp))
        # We put this in the end, because we want to break the while
        # loop when we will not be able to perform it anymore.
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N = N-1
        #trace = (trace[:N:2]+trace[1:N+1:2])/2.
        newtracea = np.zeros(N/2, dtype=np.float32)
        newtraceb = np.zeros(N/2, dtype=np.float32)
        for j in range(N/2):
            newtracea[j] = (a[2*j]+a[2*j+1])/2.
            newtraceb[j] = (b[2*j]+b[2*j+1])/2.
        del a
        del b
        a = newtracea
        b = newtraceb
        N = N/2
    return np.array(G)


@cython.cdivision(True)
@cython.boundscheck(False) # turn of bounds-checking for entire function
def BinTraceFromTrace(np.ndarray[DTYPEfloat32_t] trace, double deltat, length):
    """ Get traces with maximal resonable *length* from a file.
        This function is gets the traces corresponding to the
        correlation functions created by *ACFromFile*.
        *deltat* in seconds.
        Returns trace with time in seconds and trace in kHz
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    cdef int i, N, number_of_operations, step
    cdef np.ndarray[DTYPEfloat32_t] newtrace
    step = 0
    while len(trace) > length:
        # Half the length of the trace
        N = int(np.floor(len(trace)/2))
        newtrace = np.zeros(N, dtype=np.float32)
        for i in range(N):
            newtrace[i] = (trace[2*i]+trace[2*i+1])/2.
        del trace
        trace = newtrace
        step += 1
    T = np.zeros((len(trace), 2))
    T[:,1] = trace/deltat/1e3 # in kHz
    T[:,0] = np.arange(len(trace))*deltat*2**step
    return T


@cython.cdivision(True)
@cython.boundscheck(False) # turn of bounds-checking for entire function
def ACFromFile(filename, double deltat, int m=16, maxfilesize = 500):
    """ Apply the multiple tau algorithm to an intensity file.
        The file should be straight 16 uint. *m* is the number of bins 
        to use for first *m* values of the correlation function.
        Returns a list with tuple arrays G. The length of
        the list depend on the filesize of *filename*. If the file is
        larger than maxfilesize [MB], multiple correlation functions
        will be created from the chunked file.
        G: First element is the lagtime
           (same dimension as deltat) and second element is autocorrelation
           function.
        
        The code was tested using exponentially correlated noise.
        File format should be binary 16bit uint.
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    cdef int n, step, j, k, number_of_operations, N
    cdef double traceavg
    cdef double Gtmp
    cdef np.ndarray[DTYPEfloat32_t] trace, newtrace
    # Check size of file. If file is too large, we cannot work with it in RAM.
    # maxfilesize is set in MB 
    read_16bit_num = maxfilesize*2**19 # 1024**2/2 - We read two bytes
    filesize = os.path.getsize(filename)/1024.**2
    number_of_operations = int(np.ceil(filesize/maxfilesize))
    File = open(filename, 'rb')
    G_list = list()
    G = list()
    for k in range(number_of_operations):
        trace = np.array(np.fromfile(File, dtype="uint16", count=read_16bit_num), dtype="float32")
        N = len(trace)
        traceavg = trace.mean(dtype="float")
        # This alorithm only works with deviations from zero
        trace = trace - traceavg
        if N < 2*m:
            # Otherwise the following for-loop will fail:
            raise ValueError("len(trace) must be larger than 2m")
        ## Calculate autocorrelation function for first m bins
        # Discrete convolution of m elements
        for n in range(m):
            Gtmp = 0
            #Gtmp = np.sum(trace[:N-(n+1)]*trace[(n+1):], dtype=np.float64)
            for j in range(N-(n+1)):
                Gtmp += trace[j]*trace[j+n+1]
            # Normalize G(n)
            # Sutract 1, because we calculated G from signal,
            # not from signal deviations.
            Gtmp = 1.*Gtmp/((N-n-1)*traceavg**2)
            # Append to array
            G.append((deltat*(n+1), Gtmp))
        ## Now that we calculated the first m elements of G, let us
        ## go on with the next few elements.
        ## Calculate how many times we may perform binning migth increase 
        ## performance ? No, we bin less than 10000 times.
        step = 0
        ## Bin the countrate array.
        # Add up every second element
        # Check if len(trace) is even:
        if N%2 == 1:
            N = N-1
        #trace = (trace[:N:2]+trace[1:N+1:2])/2.
        newtrace = np.zeros(N/2, dtype=np.float32)
        for j in range(N/2):
            newtrace[j] = (trace[2*j]+trace[2*j+1])/2.
        del trace
        trace = newtrace
        N = N/2
        while N >= m:
            step += 1
            # Get the next m/2 values of the trace
            for n in range(m/2):
                Gtmp = 0
                # We only need elements from m/2 on.
                # This saves computing time.
                ## Might be faster with arrays?
                #Gtmp = np.sum(trace[:N-(n+1+m/2)]*trace[(n+1+m/2):])
                for j in range(N-(n+1+m/2)):
                    Gtmp += trace[j]*trace[j+n+1+m/2]
                # Normalize G(n)
                # Sutract 1, because we calculated G from signal,
                # not from signal deviations.
                Gtmp = 1.*Gtmp/((N-n-1-m/2)*traceavg**2)
                # Append to array
                G.append((deltat*(n+1+m/2)*2**step, Gtmp))
            # We put this in the end, because we want to break the while
            # loop when we will not be able to perform it anymore.
            ## Bin the countrate array.
            # Add up every second element
            # Check if len(trace) is even:
            if N%2 == 1:
                N = N-1
            #trace = (trace[:N:2]+trace[1:N+1:2])/2.
            newtrace = np.zeros(N/2, dtype=np.float32)
            for j in range(N/2):
                newtrace[j] = (trace[2*j]+trace[2*j+1])/2
            del trace
            trace = newtrace
            N = N/2
        G_list.append(np.array(G))
        G = list()
    File.close()
    return G_list


@cython.cdivision(True)
@cython.boundscheck(False) # turn of bounds-checking for entire function
def BinTracesFromFile(filename, double deltat, length, maxfilesize = 500):
    """ Get traces with maximal resonable *length* from a file.
        This function is gets the traces corresponding to the
        correlation functions created by *ACFromFile*.
    """
    # Code was adapted from a C script from Fabian Heinemann.
    #
    # Autocorrelation function is a list of tuples
    cdef int k, i, N, number_of_operations, step
    cdef np.ndarray[DTYPEfloat32_t] trace
    # Check size of file.
    read_16bit_num = maxfilesize*2**19 # 1024**2/2 - We read two bytes
    filesize = os.path.getsize(filename)/1024.**2
    number_of_operations = int(np.ceil(filesize/maxfilesize))
    File = open(filename, 'rb')
    Traces = list()
    step = 0
    for k in range(number_of_operations):
        trace = np.array(np.fromfile(File, dtype="uint16", count=read_16bit_num), dtype="float32")
        T = BinTraceFromTrace(trace, deltat, length)
        Traces.append(T)
    File.close()
    return Traces


__version__ = "0.1.2"

if __name__ == "__main__":
    print "Module multipletau v."+__version__





