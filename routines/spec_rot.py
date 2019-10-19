#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:40:52 2018

@author: sid
"""

import scipy.interpolate as sprot
import scipy.ndimage as spim
import numpy as np
import astropy.io.fits as fit
import matplotlib.pyplot as plt
import glob

path='/home/sid/2018_07_27 TLE Jaisalmer data'+ \
     '/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/'

