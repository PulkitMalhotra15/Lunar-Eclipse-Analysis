# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 18:47:56 2018

@author: atom
"""

import spec_lists as slst
import spec_from_file as sprd

path='/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/'

slists=slst.slists(path)

for i in range(len(slists)):
    for j in range(slists[i]):
        temp=sprd.spec(slists[i][j][0])
        