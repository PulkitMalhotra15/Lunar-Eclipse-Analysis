#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 16:37:10 2019

@author: atom
"""
#IMAGE POSTPROCESS
import numpy as np
import matplotlib.pyplot as plt
import glob
import field_rotation as frot
import astropy.io.fits as fit
import datetime
import scipy.ndimage as sp
from skimage import feature as ft
import prepare_lists as prep

def rotang(time):
    if time < 1532694247:
        return 0.
    elif time < 1532703113:
        return 0.002026123501998*time-3105429.38550305
    elif time < 1532709903:
        return 17.
    else:
        return -0.002180487003623*time+3342069.95218186

images = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/rot and crop images/'

save_in = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/final for phot/'

types={0:'bl',1:'IR',2:'HA',3:'HB'}

lists=[[],[],[],[]]

N=20

for i in range(len(lists)):
    lists[i]=sorted(glob.glob(images+'*'+types[i]+'/*.fit'))

##CREATING MASKS##
masks=np.zeros([450,450,N])

#M. Crisium
for i in range(200,300):
    for j in range(350,450):
        yc,xc=np.float(i-242),np.float(j-410)
        ao,ai,bo,bi=25.,23.,35.,33.
        if (xc/ao)**2+(yc/bo)**2 <= 1 and (xc/ai)**2+(yc/bi)**2 >= 1:
            masks[i,j,0]=1

#C. Aristarchus
for i in range(330,370):
    for j in range(80,120):
        yc,xc=np.float(i-348),np.float(j-102)
        ao,ai,bo,bi=15.,13.,15.,13.
        if (xc/ao)**2+(yc/bo)**2 <= 1 and (xc/ai)**2+(yc/bi)**2 >= 1:
            masks[i,j,0]=1
            
#C. Grimaldi
for i in range(220,280):
    for j in range(0,50):
        yc,xc=np.float(i-255),np.float(j-22)
        ao,ai,bo,bi=15.,13.,25.,23.
        if (xc/ao)**2+(yc/bo)**2 <= 1 and (xc/ai)**2+(yc/bi)**2 >= 1:
            masks[i,j,0]=1        

#C. Tycho
for i in range(60,120):
    for j in range(100,200):
        yc,xc=np.float(i-89),np.float(j-154)
        ao,ai,bo,bi=25.,23.,25.,23.
        if (xc/ao)**2+(yc/bo)**2 <= 1 and (xc/ai)**2+(yc/bi)**2 >= 1:
            masks[i,j,0]=1  
      

for i in range(1,N):
    masks[:,:,i]=sp.rotate(masks[:,:,0],1*i,reshape=False)
        
thetas=[[] for i in range(4)]



for I in range(4):
    ##For Cropping to the center##
    for J in range(len(lists[I])):
        dat=fit.open(lists[I][J])
        img=dat[0].data
        hdr=dat[0].header
        sobx=sp.sobel(img,axis=0);soby=sp.sobel(img,axis=1);sob=np.hypot(sobx,soby)
        if np.max(sob[250,:50])>np.max(sob[250,450:]):
            lef=np.argmax(sob[250,:50])-5
            rig=lef+450
        else:
            rig=np.argmax(sob[250,450:])+455
            lef=rig-450
        if np.max(sob[:50,250])>np.max(sob[450:,250]):
            top=np.argmax(sob[10:50,250])-5
            bot=top+450
        else:
            bot=np.argmax(sob[450:490,250])+455
            top=bot-450
        cropimg=img[top:bot,lef:rig]
        dt=hdr['DATE-OBS']
        tsep=datetime.datetime.strptime(dt,'%Y-%m-%dT%H:%M:%S')
        time=np.int(tsep.strftime('%s'))
        
        
       # rang=rotang(time)
        #rotimg=sp.rotate(cropimg,-rang,reshape=False)
        
        #plt.savefig(save_in+types[I]+'/'+format(J,"03")+'.png') 

        #fit.writeto(save_in+types[I]+'/'+format(J,"03")+'.fit',
                    rotimg,header=hdr)
        
#        cann=ft.canny(cropimg,7)
#        
#        if (J==0 and I==0) :
#            cann1=np.copy(cann)
        
        #sobx=sp.sobel(cropimg,axis=0)
        #soby=sp.sobel(cropimg,axis=1)
        #sob=np.hypot(sobx,soby)


        #mask_val=np.array([np.sum(masks[:,:,i]*sob) for i in range(N)])
        
        #thetas[I].append(np.argmax(mask_val))
        
        



    
    
    
    


        