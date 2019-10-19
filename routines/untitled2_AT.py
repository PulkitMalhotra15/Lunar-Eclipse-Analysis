#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 15:53:49 2018

@author: atom
"""
import matplotlib.pyplot as plt
import numpy as np
spec_L_1=open('/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/spec_Left_1',
              'r')
matt=spec_L_1.readlines()
matrix=[[],[]]
for i in range(3001):
    matrix[0].append(float(matt[i][0:24]))
    matrix[1].append(float(matt[i][25:-1]))
