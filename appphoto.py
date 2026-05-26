#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:25:43 2019

@author: atom
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import astropy.io.fits as fit
import photutils.aperture as apphot

images = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/final for phot/'

types={0:'bl',1:'IR',2:'HA',3:'HB'}

lists=[[],[],[],[]]

for i in range(len(lists)):
    lists[i]=sorted(glob.glob(images+'*'+types[i]+'/*.fit'))

ap1=apphot.EllipticalAperture((397,145),5,9,-60)
ap2=apphot.EllipticalAperture((160,281),9,6,0)
ap3=apphot.EllipticalAperture((102,349),4,4,0)
ap4=apphot.EllipticalAperture((160,280),8,5,0)
ap5=apphot.EllipticalAperture((20,255),4,9,0)


apertures=[ap2]

phot = apphot.aperture_photometry(img, apertures)

plt.imshow(img,origin='lower');ap3.plot(color='white')

plt.matshow(img[340:355,95:110])