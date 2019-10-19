#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 09:36:21 2018

@author: sid
"""
import numpy as np
import astropy.io.fits as fit
import glob

wdir = '/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer/dark frames/'

lists = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

lists[0] += glob.glob(wdir+'*.001')
lists[1] += glob.glob(wdir+'*_002_*.fit')
lists[2] += glob.glob(wdir+'*_005_*.fit')
lists[3] += glob.glob(wdir+'*_01_*.fit')
lists[4] += glob.glob(wdir+'*_02_*.fit')
lists[5] += glob.glob(wdir+'*_05_*.fit')
lists[6] += glob.glob(wdir+'*_1_*.fit')
lists[7] += glob.glob(wdir+'*_2_*.fit')
lists[8] += glob.glob(wdir+'*_5_*.fit') 
lists[9] += glob.glob(wdir+'*_1s_*.fit')
lists[10] += glob.glob(wdir+'*_2s_*.fit')
lists[11] += glob.glob(wdir+'*_5s_*.fit')
lists[12] += glob.glob(wdir+'*_10s_*.fit')
lists[13] += glob.glob(wdir+'*_20s_*.fit')

darks=['001','002','005','01','02','05','1','2','5','1s','2s','5s','10s','20s']

for i in range(len(lists)):
    stack = np.zeros((len(lists[i]),1335,2003))
    dark = np.zeros((1335,2003))        
    for j in range(len(lists[i])): 
        data=fit.open(lists[i][j])
        hdr=data[0].header
        img=data[0].data
        stack[j] = img
    for k in range(1335):
        for l in range(2003):
            dark[k,l] = np.median(stack[:,k,l])
    #fit.writeto('/home/atom/2018_07_27 TLE Jaisalmer/Bhairavi/'
      #          +'dark_'+darks[i]+'.fit',dark,header=hdr)




        


