# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:14:01 2018

@author: atom
"""

import astropy.io.fits as fit
import numpy as np
import glob

darkpath='/home/atom/2018_07_27 TLE Jaisalmer'+\
         '/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/Dark/'

darknames={0:['043700','dark_1s'],1:['043807','dark_3s'],2:['044019','dark_5s'],
           3:['044247','dark_6s'],4:['044631','dark_8s'],5:['045015','dark_10s'],
           6:['045635','dark_20s'],7:['050230','dark_50s'],8:['052338','dark_0001'],
           9:['060935','spec_R'],10:['061252','spec_P'],11:['061514','spec_L'],
           12:['062326','flat_R'],13:['062615','flat_P'],
           14:['062804','flat_L']}

darklists=[[] for i in range(len(darknames))]

for i in range(len(darklists)):
    darklists[i] = glob.glob(darkpath+'*'+darknames[i][0]+'*.fit')
    stack = np.zeros((len(darklists[i]),960,1280)) #stacks all the dark frames
    dark = np.zeros((960,1280)) #stores the above stack as dark        
    for j in range(len(darklists[i])): 
        data=fit.open(darklists[i][j])
        hdr=data[0].header
        img=data[0].data
        stack[j] = img
    for k in range(960):
        for l in range(1280):
            dark[k,l] = np.median(stack[:,k,l])
    fit.writeto('/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/dark and flat/'+\
                darknames[i][1]+'.fit',dark,header=hdr)

                
                
                
                
                
                
                
                
                
                
                
                
                