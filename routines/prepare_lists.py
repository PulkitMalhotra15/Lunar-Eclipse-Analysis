#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 21:10:03 2018

@author: sid
"""

# Prepares time-sorted lists of image series (filenames)

import astropy.io.fits as fit
import glob
import datetime

paths = ['/home/atom/2018_07_27 TLE Jaisalmer/2018_07_27 Lunar Ecipse Expedition Jaisalmer/',
         '/home/atom/2018_07_27 TLE Jaisalmer/2018_07_27 Lunar Ecipse Expedition Jaisalmer_001/',
         '/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer/']

def slists(lists):
    
    sl=[[] for i in range(len(lists))]
    
    for i in range(len(sl)):
        for j in range(len(lists[i])): 
            data=fit.open(lists[i][j])
            head=data[0].header
            time=head['DATE-OBS']
            binn=head['XBINNING']
            d=datetime.datetime.strptime(time,'%Y-%m-%dT%H:%M:%S')
            s=d.strftime('%s')
            if binn == 2:
                sl[i].append((lists[i][j],s))
        sl[i] = sorted(sl[i],key=lambda lst: lst[1])
    return sl

lists=[[],[],[],[]]

for i in range(len(paths)):
    lists[0] += glob.glob(paths[i]+'*bl*.fit')
    lists[1] += glob.glob(paths[i]+'*IR*.fit')
    lists[2] += glob.glob(paths[i]+'*HA*.fit')
    lists[3] += glob.glob(paths[i]+'*HB*.fit')

slist=slists(lists)

list_bl = slist[0]
list_IR = slist[1]
list_HA = slist[2]
list_HB = slist[3]

def llists():
    return [list_bl,list_IR,list_HA,list_HB]


    
