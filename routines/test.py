#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 11:48:23 2018

@author: atom
"""
import numpy as np
import matplotlib.pyplot as plt

path='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/ratio plots/'

i=10

fname='ratio_lr_'+str(i)

rat=np.loadtxt(path+fname)

plt.plot(rat[:,0],rat[:,1])
plt.savefig(path+fname+'.png',dpi=600)