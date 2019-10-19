#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 00:05:58 2018

@author: sid
"""

# Moon altitude and azimuth data generated from "www.mooncalc.org"
 
import numpy as np
import datetime

raw = np.loadtxt('/home/atom/2018_07_27 TLE Jaisalmer/Analysis/routines/'\
                 +'Moon Altitude and Azimuth TLE Jaisalmer.csv',skiprows=1) 

inter = np.array([0,0,0])

for i in range(len(raw)):
    YR = np.int(raw[i][0])
    MT = np.int(raw[i][1])
    DT = np.int(raw[i][2])
    HR = np.int(raw[i][3])
    MN = np.int(raw[i][4])
    SC = 0
    dt = datetime.datetime(YR,MT,DT,HR,MN,SC)
    ut=np.int(dt.strftime('%s'))-19800                  # Converted to UT sec
    alt = raw[i][5]
    azi = raw[i][6]
    inter=np.vstack((inter,np.array([ut,alt,azi])))
    
inter = np.delete(inter,(0),axis=0)

def alt(time):
    return np.interp(time,inter[:,0],inter[:,1])

def azi(time):
    return np.interp(time,inter[:,0],inter[:,2])



