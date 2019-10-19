#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 20:23:05 2018

@author: sid
"""

import numpy as np
import matplotlib.pyplot as plt
import glob
import field_rotation as frot
import astropy.io.fits as fit
import datetime
import scipy.ndimage as sp
#import skimage.feature as sk
import prepare_lists as prep


source = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/df corrected/'

target = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/rot and crop images/'

types={0:'bl',1:'IR',2:'HA',3:'HB'}

olists=[[],[],[],[]]

for i in range(len(olists)):
    olists[i]=glob.glob(source+'*'+types[i]+'*.fit')

ranges=[0,0,0,0]

slist=prep.slists(olists)

def rotimg(df_file):
    dfcor=fit.open(df_file)
    hdr=dfcor[0].header
    dt=hdr['DATE-OBS']
    img=dfcor[0].data
    tsep=datetime.datetime.strptime(dt,'%Y-%m-%dT%H:%M:%S')
    time=np.int(tsep.strftime('%s'))
    rot=frot.frot(time)
    frimg=sp.interpolation.rotate(img,rot)
    return frimg,hdr
    
def cropimg(frimg,hdr):
    mask=np.zeros((500,500))
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if (i-250)**2+(j-250)**2<=52900 and (i-250)**2+(j-250)**2>=48400:
                mask[i,j]=1
    cm=np.array(sp.measurements.center_of_mass(frimg),dtype='int')
    sobx=sp.sobel(frimg,axis=0)
    soby=sp.sobel(frimg,axis=1)
    sob=np.hypot(sobx,soby)
    find=np.zeros(frimg.shape)
    maxi=np.zeros(frimg.shape)
    rx=(max(cm[0]-550,0),min(2*cm[0]-500,cm[0]+50,frimg.shape[0]-500))
    ry=(max(cm[1]-550,0),min(2*cm[1]-500,cm[1]+50,frimg.shape[1]-500))
    for k in range(rx[0],rx[1],10):
        for l in range(ry[0],ry[1],10):
            find[k:k+500,l:l+500]=mask
            mn=sp.measurements.mean(sob,labels=find,index=1)
            maxi[k+250,l+250]=mn
    ln=len(maxi[0])
    pn=np.argmax(maxi)
    posmax=np.array([pn/ln,pn%ln])
    cpimg=frimg[posmax[0]-250:posmax[0]+250,posmax[1]-250:posmax[1]+250]
    return cpimg,hdr


        