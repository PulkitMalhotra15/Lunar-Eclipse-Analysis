# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 12:46:07 2018

@author: atom
"""

import astropy.io.fits as fit
import glob
import datetime

path='/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/'

typs={0:'Left',1:'Prime',2:'Right'}


def slists(path):
    lsts=[[],[],[]]
    
    slsts=[[] for i in range(len(lsts))]
    
    for i in range(len(lsts)):
        lsts[i]=glob.glob(path+'*'+typs[i]+'*.fit')
        for j in range(len(lsts[i])):
            raw=fit.open(lsts[i][j])
            tm=raw[0].header['DATE-OBS']
            d=datetime.datetime.strptime(tm,'%Y-%m-%dT%H:%M:%S.%f')
            s=d.strftime('%s.%f')
            slsts[i].append((lsts[i][j],s))
        slsts[i] = sorted(slsts[i],key=lambda lst: lst[1])
    return slsts

    