#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:10:03 2018

@author: sid
"""

import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fit
import prepare_lists as pl

llists = pl.llists()

dpath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/dark_and_flat/'

savepath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/df corrected/'

dark={0.001:'001', 0.002:'002',0.005:'005',0.01:'01',0.02:'02',0.05:'05',
      0.1:'1',0.2:'2',0.5:'5',1.0:'1s',2.0:'2s',5.0:'5s',10.0:'10s',20.0:'20s'}

flat={0:'bl',1:'IR',2:'HA',3:'HB'}

# Explanation: This script applies dark frame and flat frame corrections 
# to the data. The final .fit file is normalised for exposure time.

for i in range(len(llists)):
    for j in range(len(llists[i])):
        raw=fit.open(llists[i][j][0])
        exp=raw[0].header['EXPTIME']
        img=raw[0].data
        if exp==1.5:
            dfr=fit.open(dpath+'dark_'+dark[1.0]+'.fit')[0].data+ \
                fit.open(dpath+'dark_'+dark[0.5]+'.fit')[0].data
        elif exp==0.75:
            dfr=fit.open(dpath+'dark_'+dark[0.5]+'.fit')[0].data+ \
                fit.open(dpath+'dark_'+dark[0.2]+'.fit')[0].data+ \
                fit.open(dpath+'dark_'+dark[0.05]+'.fit')[0].data
        elif exp==3.0:
            dfr=fit.open(dpath+'dark_'+dark[2.0]+'.fit')[0].data+ \
                fit.open(dpath+'dark_'+dark[1.0]+'.fit')[0].data
        elif exp==15.0:
            dfr=fit.open(dpath+'dark_'+dark[10.0]+'.fit')[0].data+ \
                fit.open(dpath+'dark_'+dark[5.0]+'.fit')[0].data
        else:
            dfr=fit.open(dpath+'dark_'+dark[exp]+'.fit')[0].data
        ffr=fit.open(dpath+'flat_'+flat[i]+'.fit')[0].data
        ffr/=np.max(ffr)
        img=(img-dfr)/(ffr*exp)
        fit.writeto(savepath+'dfcorr_'+flat[i]+'_'+format(j,'03d')+'.fit',
                    img,header=raw[0].header)



