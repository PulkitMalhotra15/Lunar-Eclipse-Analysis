#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 19:48:57 2019

@author: atom
"""

#APERTURE PHOTOMTRY
import numpy as np
import matplotlib.pyplot as plt
import glob
import astropy.io.fits as fit
import photutils.aperture as apphot
import datetime

images = '/home/atom/2018_07_27 TLE Jaisalmer/Analysis/images/final for phot/'

save_in = '/home/atom/2018_07_27 TLE Jaisalmer/pul/'

types={0:'bl',1:'IR',2:'HA',3:'HB'}

lists=[[],[],[],[]]

for i in range(len(lists)):
    lists[i]=sorted(glob.glob(images+'*'+types[i]+'/*.fit'))

features=['C_Langrenus', 'C_Aristarchus', 'C_Copernicus', 'C_Grimaldi', 
          'C_Tycho', 'C_Plato', 'M_Crisium', 'M_Humorum', 'M_Imbrium', 
          'M_Seremtalis', 'M_Traquillatis', 'M_Nectaris', 'M_Fecunditatis']

ap1=apphot.EllipticalAperture((397,145),5,9,-60)    # C. Langrenus
ap2=apphot.EllipticalAperture((102,349),4,4,0)   # C. Aristarchus
ap3=apphot.EllipticalAperture((160,281),9,9,0)      # C. Copernicus
ap4=apphot.EllipticalAperture((20,255),4,9,0)   #C. Grimaldi
ap5=apphot.EllipticalAperture((410,240),16,27,0)    # M. Crisium   
ap6=apphot.EllipticalAperture((154,90),10,10,0)    # C. Tycho
ap7=apphot.EllipticalAperture((246,397),8,5,0)    # C. Plato
ap8=apphot.EllipticalAperture((78,260),11,11,0)    # C. Kepler ***
ap9=apphot.EllipticalAperture((410,240),20,32,0)    # M. Crisium
ap10=apphot.EllipticalAperture((80,170),22,22,0)    # M. Humorum
ap11=apphot.EllipticalAperture((200,350),75,55,0)    # M. Imbrium
ap12=apphot.EllipticalAperture((305,300),45,40,60)    # M. Seremtalis
ap13=apphot.EllipticalAperture((335,220),45,40,0)    # M. Traquillatis
ap14=apphot.EllipticalAperture((325,140),13,15,0)    # M. Nectaris
ap15=apphot.EllipticalAperture((380,165),20,35,0)    # M. Fecunditatis

ap16=apphot.EllipticalAperture((400,300),20,32,0)    # Br Crisium
ap17=apphot.EllipticalAperture((125,80),22,22,0)    # Br Humorum    
ap18=apphot.EllipticalAperture((210,80),75,55,0)    # Br Imbrium
ap19=apphot.EllipticalAperture((290,80),45,40,0)    # Br Traquillatis

ap20=apphot.EllipticalAperture((170,350),40,30,0)    # M. Imbrium pt1
ap21=apphot.EllipticalAperture((230,350),40,30,-np.pi/18)    # M. Imbrium pt2
ap22=apphot.EllipticalAperture((180,80),40,30,0)    # Br Imbrium pt1
ap23=apphot.EllipticalAperture((170,80),40,30,0)    # Br Imbrium pt2
ap24=apphot.EllipticalAperture((280,100),45,40,60)    # Br. Seremtalis
ap25=apphot.EllipticalAperture((320,110),13,15,0)    # br. Nectaris
ap26=apphot.EllipticalAperture((365,100),15,25,50)   # br. Fecunditatis o1
ap27=apphot.EllipticalAperture((370,100),10,25,0)    # br. Fecunditatis o2




apertures=[ap1,ap2,ap3,ap4,ap5,ap6,ap7,ap8,ap9,ap10,ap11,ap12,ap13,ap14,ap15,ap16,ap17,
           ap18,ap19,ap20, ap21,ap22, ap23,ap24,ap25, ap26, ap27]


plt.imshow(img1,cmap='gray',origin='lower');apertures[23].plot(color='white')
apertures[24].plot(color='white')

plt.imshow(img2,cmap='gray',origin='lower');apertures[22].plot(color='white')
apertures[20].plot(color='white')





K=24
name="Br_Imbrium_pt2_"
lcurves=[np.zeros((2,2)) for i in range(4)]
for I in range(len(lists)):
    for J in range(len(lists[I])):
        fil=lists[I][J]
        img=fit.open(fil)[0].data
        hdr=fit.open(fil)[0].header
        dt=hdr['DATE-OBS']
        tsep=datetime.datetime.strptime(dt,'%Y-%m-%dT%H:%M:%S')
        time=np.int(tsep.strftime('%s'))
        phot=apphot.aperture_photometry(img,apertures[K])
        sums=float(phot['aperture_sum'])/hdr['EXPTIME']
        lcurves[I]=np.vstack((lcurves[I],np.array([time,sums])))
    lcurves[I]=np.delete(lcurves[I],0,axis=0)
    lcurves[I]=np.delete(lcurves[I],0,axis=0)
    plt.plot(lcurves[I][:,0],lcurves[I][:,1]);plt.yscale('log')
    plt.savefig(save_in+"plots/"+name+types[I])
    plt.close()
    np.savetxt(save_in+name+types[I],lcurves[I])


plt.savefig(save_in+"B_Imbrium_bl")

#plt.plot(lcurves[0][:,0],lcurves[0][:,1]);plt.yscale('log')
np.savetxt(save_in+"B_Imbrium_bl",lcurves[0])
np.savetxt(save_in+"B_Imbrium_IR",lcurves[1])
np.savetxt(save_in+"B_Imbrium_HA",lcurves[2])
np.savetxt(save_in+"B_Imbrium_HB",lcurves[3])

c=np.loadtxt(save_in+"Br_Fecunditatis_pt1bl")
#e=np.loadtxt(save_in+"Br_Fecunditatis_pt2bl")
d=np.loadtxt(save_in+"M_Fecunditatis_bl")
plt.plot(c[:,0],c[:,1]/d[:,1],'r-')
#plt.plot(e[:,0],e[:,1]/d[:,1],'b-')
plt.plot(c[:,0],c[:,1],'k-')
plt.plot(c[:,0],d[:,1],'g-')
#plt.plot(c[:,0],e[:,1])
plt.yscale('log')


img1=fit.open(lists[0][55])[0].data
img2=fit.open(lists[0][69])[0].data
img3=fit.open(lists[0][78])[0].data
plt.subplot(131);plt.imshow(img1,cmap='gray',origin='lower')
plt.subplot(132);plt.imshow(img2,cmap='gray',origin='lower')
plt.subplot(133);plt.imshow(img3,cmap='gray',origin='lower')



