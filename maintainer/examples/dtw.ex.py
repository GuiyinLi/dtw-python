

>>> import numpy as np
>>> from dtwr import *

A noisy sine wave as query

>>> idx = np.linspace(0,6.28,num=100)
>>> query = np.sin(idx) + np.random.uniform(size=100)/10.0

A cosine is for reference; sin and cos are offset by 25 samples

>>> reference = np.cos(idx)

Find the best match

>>> alignment = dtw(query,reference)

Display the mapping, AKA warping function - may be multiple-valued
Equivalent to: plot(alignment,type="alignment")

>> plot(alignment$index1,alignment$index2,main="Warping function");


Partial alignments are allowed.

>>> alignmentOBE = dtw(query[44:88], reference,
...                      keep_internals=True,
...                      step_pattern=asymmetric,
...                      open_end=True,open_begin=True);

>> plot(alignmentOBE,type="two",off=1);


Subsetting allows warping and unwarping of
timeseries according to the warping curve. 
See first example below.

Most useful: plot the warped query along with reference 
>> plot(reference)
>> lines(query[alignment$index1]~alignment$index2,col="blue")

Plot the (unwarped) query and the inverse-warped reference
>> plot(query,type="l",col="blue")
>> points(reference[alignment$index2]~alignment$index1)





Contour plots of the cumulative cost matrix
similar to: plot(alignment,type="density") or
dtwPlotDensity(alignment)
See more plots in ?plot.dtw 
keep = True so we can look into the cost matrix


>>> alignment = dtw(query,reference,keep_internals=True);


>>> contour(alignment$costMatrix,col=terrain_colors(100),x=1:100,y=1:100,
>>> xlab="Query (noisy sine)",ylab="Reference (cosine)");


>>> lines(alignment$index1,alignment$index2,col="red",lwd=2);





A hand-checkable example

>>> ldist = np.ones((6,6))             # Matrix of ones
>>> ldist[1,] = 0; ldist[,4] = 0;      # Mark a clear path of zeroes
>>> ldist[1,4] = .01;		       # Forcely cut the corner

>>> ds = dtw(ldist);			 # DTW with user-supplied local

>>> da = dtw(ldist,step_pattern=asymmetric);	 # Also compute the asymmetric 

Symmetric: alignment follows the low-distance marked path
>> plot(ds$index1,ds$index2,pch=3)

Asymmetric: visiting 1 is required twice
>> points(da$index1,da$index2,col="red");  

>>> ds.distance
>>> da.distance

