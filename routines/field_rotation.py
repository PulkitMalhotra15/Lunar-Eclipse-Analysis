#FIELD ROTATION
import numpy as np
import Moon_alt_azi as aa
import datetime
import matplotlib.pyplot as plt

Lat = 26.906053

Ang_vel = 15.04106858                   # degree per hour

f = np.pi/180

def rrot(time):
    K = Ang_vel*np.cos(Lat*f)           # Formula from "calgary.rasc.ca"
    alt = aa.alt(time)                  # Data from "www.mooncalc.org"
    azi = aa.azi(time)                  #
    
    return K*np.cos(alt*f)/np.cos(azi*f)

ut0 = np.int(datetime.datetime(2018,7,27,14,0).strftime('%s'))

ut1 = np.int(datetime.datetime(2018,7,28,0,40).strftime('%s'))

L = ut1-ut0+1

fr = np.array([0,0])

rot=0

for i in range(L):
    if i != 0:
        rot += rrot(ut0+i-1)/3600
    temp = np.array([ut0+i,rot])
    fr = np.vstack((fr,temp))

fr = np.delete(fr,(0),axis=0)

#plt.plot(fr[:,0],fr[:,1])

def frot(time):
    adrot=0
    if time>1532703600:                 # Telescope was moved ca. 20.30 UT
        adrot=-4.4
    for i in range(len(fr)):
        if time == fr[i,0]:
            return fr[i,1]+adrot

