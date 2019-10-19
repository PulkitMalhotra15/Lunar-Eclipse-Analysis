#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:23:59 2018

@author: sid
"""

import numpy as np
import astropy.io.fits as fit
import glob

wdir = '/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer/dark frames/'

lists = [[],[],[],[]]

lists[0] += glob.glob(wdir+'flat_bl*.fit')
lists[1] += glob.glob(wdir+'flat_IR*.fit')
lists[2] += glob.glob(wdir+'flat_HA*.fit')
lists[3] += glob.glob(wdir+'flat_HB*.fit')

flats=['bl','IR','HA','HB']

for i in range(len(lists)):
    flat = np.zeros((1335,2003))     
    for j in range(len(lists[i])): 
        data=fit.open(lists[i][j])
        hdr=data[0].header
        img=data[0].data
        flat += img
    fit.writeto('/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/dark_and_flat/'
                +'flat_'+flats[i]+'.fit',flat,header=hdr)
