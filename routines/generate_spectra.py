# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 15:38:42 2018

@author: atom
"""

import scipy.ndimage as sp
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fit

def spec(img):
    imgr=sp.interpolation.rotate(img,-2)    
    # Rotation angle of 2 deg determined from one single spectrum
    specr=np.array([np.sum(imgr[:,i]) for i in range(len(imgr[0]))])
    lam=np.zeros(specr.shape)    
    for i in range(len(specr)):
        lam[i] = -2.50833*i+7063.94
    specr=np.vstack((lam,specr))
    return specr
    
raw=fit.open('/home/atom/2018_07_27 TLE Jaisalmer'+
             '/2018_07_28 TLE Jaisalmer spectro data/Fire Cap'+
             '/001932_Right_0002.fit')

img=raw[0].data

spectrum=spec(img)
spectrum[1]=sp.filters.gaussian_filter(spectrum[1],sigma=2)

plt.plot(spectrum[0],spectrum[1])
plt.savefig('bhairavi',dpi=12000)
#plt.xlim(5500,6000)