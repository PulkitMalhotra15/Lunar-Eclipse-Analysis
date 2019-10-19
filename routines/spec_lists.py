#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:44:59 2018

@author: sid
"""

import glob
import datetime
import astropy.io.fits as fit
import numpy as np

def slists(lists):
    
    sl=[[] for i in range(len(lists))]
    
    for i in range(len(sl)):
        for j in range(len(lists[i])): 
            data=fit.open(lists[i][j])
            head=data[0].header
            time=head['DATE-OBS']
            d=datetime.datetime.strptime(time,'%Y-%m-%dT%H:%M:%S.%f')
            s=np.int(d.strftime('%s'))-1532671000
            sl[i].append((lists[i][j],s))
        sl[i] = sorted(sl[i],key=lambda lst: lst[1])
    return sl


path='/home/atom/2018_07_27 TLE Jaisalmer'+\
     '/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/'
     
typs={0:'Right',1:'Prime',2:'Left'}

lsts=[[],[],[]]

for i in range(len(lsts)):
    lsts[i] = sorted(glob.glob(path+'*'+typs[i]+'*.fit'))

slsts = slists(lsts)

