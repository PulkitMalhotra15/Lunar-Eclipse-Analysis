#SPECTRUM GENERATION
import astropy.io.fits as fit
import scipy.ndimage as sp
import scipy.stats as st
import numpy as np
import datetime
import matplotlib.pyplot as plt
import scipy.interpolate as spin
import time


dfpath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/dark and flat/'

darks={0.0001:'dark_0001.fit',1.:'dark_1s.fit',3.:'dark_3s.fit',5.:'dark_5s.fit',
       6.:'dark_6s.fit',8.:'dark_8s.fit',10.:'dark_10s.fit',20.:'dark_20s.fit',
       50.:'dark_50s.fit'}
       
flats={'L':'flat_L.fit','R':'flat_R.fit','P':'flat_P.fit'}

def spec(rawfile):
    raw=fit.open(rawfile)
    raw_img=raw[0].data
    tobs=raw[0].header['DATE-OBS']
    texp=raw[0].header['EXPTIME']
    dar=fit.open(dfpath+darks[np.float(texp)])
    dar_img=dar[0].data
    flt=fit.open(dfpath+flats[rawfile[90]])
    flt_img=flt[0].data
    if np.count_nonzero(flt_img)<1228800:
        flt_img+=1
    flt_frm=flt_img/np.max(flt_img)
    corr_frm=(raw_img-dar_img)/flt_frm
    crot_frm=sp.interpolation.rotate(corr_frm,-2.2)
    spec_uncal=np.array([np.sum(crot_frm[250:750,i]) for i in range(len(crot_frm[0]))])
    sspc_uncal=sp.gaussian_filter1d(spec_uncal,sigma=2)
    rois=[[(180,220),656.28],[(450,500),589.30],[(700,740),527.04],[(850,900),486.13],
           [(1080,1120),430.78]]
    ordin=np.array([])
    abcis=np.array([])
    for i in range(len(rois)):
        ordin=np.append(ordin,np.argmin(sspc_uncal[rois[i][0][0]:rois[i][0][1]])
                        +rois[i][0][0])
        abcis=np.append(abcis,rois[i][1])
    parm=st.linregress(ordin,abcis)
    lamb=np.array([])
    for i in range(len(sspc_uncal)):
        lamb=np.append(lamb,parm[0]*i+parm[1])
    conv=spin.interp1d(lamb,sspc_uncal)
    lami=np.arange(400.,700.1,0.1)
    spcl=conv(lami)
    spctrm=np.vstack((lami,spcl))           
    return spctrm
    
#dt='/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer spectro data/Fire Cap/000025_Right_0000.fit'
#
#spectrum=spec(dt)
#plt.plot(spectrum[0],spectrum[1])    