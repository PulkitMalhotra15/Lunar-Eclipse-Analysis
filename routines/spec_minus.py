#SPECTRUM ANISOTROPY
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sp
import scipy.fftpack as fft

def ff_filt(x):
    W=fft.fftfreq(x.size,d=3000)
    f_x=fft.rfft(x)
    cut_f_x = f_x.copy()
    cut_f_x[(W>1e-6)]=0
    
    return fft.irfft(cut_f_x)
    
def sm(x):
    return 2*sp.gaussian_filter(x,50)

typs={0:'_Right',1:'_Prime',2:'_Left'}

specpath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/' #path from where data has to be taken

savepath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/minus plots/' #path where data has to be stored

anisopath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/anisotropy/'

l,r,p=7,7,7

ls='_'+str(l)
rs='_'+str(r)
ps='_'+str(p)

specl=np.loadtxt(specpath+'spec'+typs[2]+ls) #load spectrum of left polarized 
specp=np.loadtxt(specpath+'spec'+typs[1]+ps) ##load spectrum of prime polarized 
specr=np.loadtxt(specpath+'spec'+typs[0]+rs) #load spectrum of right polarized 

specl_ff = ff_filt(specl[:,1])
specl_ff+=np.max(specl[:,1])-np.max(specl_ff)
specr_ff = ff_filt(specr[:,1])
specr_ff+=np.max(specr[:,1])-np.max(specr_ff)
specp_ff = ff_filt(specp[:,1])
specp_ff+=np.max(specp[:,1])-np.max(specp_ff)

Dspecl=specl[:,1]-specl_ff
Dspecr=specr[:,1]-specr_ff
Dspecp=specp[:,1]-specp_ff

aniso_D_lp = np.abs((Dspecl-Dspecp)/(Dspecl+Dspecp)) #take l-p anisotropy

aniso_D_rp = np.abs((Dspecr-Dspecp)/(Dspecr+Dspecp)) #take r-p anisotropy

aniso_D_rl = np.abs((Dspecr-Dspecl)/(Dspecr+Dspecl)) #take r-l anisotropy

plot=plt.subplots(3,1,sharex='col',sharey='row')
plot[1][0].plot(specl[:,0],aniso_D_lp,'r-')
plot[1][1].plot(specl[:,0],aniso_D_rp,'b-')
plot[1][2].plot(specl[:,0],aniso_D_rl,'g-')
for i in range(len(plot[1])):
    plot[1][i].set_xlim([420,680])
    plot[1][i].set_ylim([0,5])
    plot[1][i].set_aspect(8)
    plot[1][i].plot([589,589],[0,5],'k--') # Na
    plot[1][i].plot([517,517],[0,5],'k--') # Mg, Fe
    plot[1][i].plot([496,496],[0,5],'k--') # Fe
    plot[1][i].plot([467,467],[0,5],'k--') # Fe
    plot[1][i].plot([432,432],[0,5],'k--') # Ca, Fe

#d=np.zeros(len(aniso_rl))
#d=aniso_rl


plt.plot(specl[:,0],specl[:,1],'b-')
plt.plot(specl[:,0],specr[:,1],'r-')
plt.plot(specl[:,0],specp[:,1],'g-')

aniso_lp = (specl[:,1]-specp[:,1])/(specl[:,1]+specp[:,1]) #take l-p anisotropy

aniso_rp = (specr[:,1]-specp[:,1])/(specr[:,1]+specp[:,1]) #take r-p anisotropy

aniso_rl = (specr[:,1]-specl[:,1])/(specr[:,1]+specl[:,1]) #take r-l anisotropy

#d=np.zeros(len(aniso_rl))
#d=aniso_rl

#plt.plot(specl[:,0],((aniso_lp-d)),'b-')
plt.plot(specl[:,0],(ff_filt(aniso_rp-d)),'r-')
#plt.plot(specl[:,0],(ff_filt(aniso_rl-d)),'g-')
plt.plot([589,589],[-1,1],'k--') # Na
plt.plot([517,517],[-1,1],'k--') # Mg, Fe
plt.plot([496,496],[-1,1],'k--') # Fe
plt.plot([467,467],[-1,1],'k--') # Fe
plt.plot([432,432],[-1,1],'k--') # Ca, Fe
plt.xlim([420,680])
ymax=max(np.max((aniso_rp-d)[200:2500]),np.max((aniso_lp-d)[200:2500]))
ymin=min(np.min((aniso_rp-d)[200:2500]),np.min((aniso_lp-d)[200:2500]))
plt.ylim([ymin,ymax])

c=1e-3

   
plt.savefig(anisopath+'l'+ls+'_r'+rs+'_p'+ps+'.png',dpi=300,bbox_inches='tight')

np.savetxt(anisopath+'aniso_R'+rs+'_L'+ls,aniso_rl)
np.savetxt(anisopath+'aniso_R'+rs+'_P'+ps,aniso_rp)
np.savetxt(anisopath+'aniso_L'+ls+'_P'+ps,aniso_lp)




#np.savetxt(savepath+'minus_lp_18',np.transpose(np.vstack((specl[:,0],minus_lp)))) #saves left to prime minus

#np.savetxt(savepath+'minus_rp_18',np.transpose(np.vstack((specl[:,0],minus_rp)))) #saves right to prime minus

#np.savetxt(savepath+'minus_rl_18',np.transpose(np.vstack((specl[:,0],minus_rl)))) #saves left to right minus

#plt.plot(specl[:,0],minus_lp,'r-') #plots the graph of L-P

#plt.plot(specl[:,0],minus_rp,'b-') #plots the graph of R-P

#plt.plot(specl[:,0],minus_rl,'g-') #plots the graph of R-L

#plt.savefig(savepath+'minus_18') #saves all the three graph

#plt.savefig(savepath+'minus_rp_'+ns)

#plt.savefig(savepath+'minus_rl_'+ns)

