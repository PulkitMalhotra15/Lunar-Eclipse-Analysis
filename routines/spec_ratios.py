#SPECTRUM RATIOS
import numpy as np

typs={0:'_Right',1:'_Prime',2:'_Left'}

specpath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/' #path from where data has to be taken

savepath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/ratio plots/' #path where data has to be stored



specl=np.loadtxt(specpath+'spec'+typs[2]+'_6') #load spectrum of left polarized 

specp=np.loadtxt(specpath+'spec'+typs[1]+'_6') ##load spectrum of prime polarized 

specr=np.loadtxt(specpath+'spec'+typs[0]+'_6') #load spectrum of right polarized 



ratio_lp = specl[:,1]/specp[:,1] #take ratio of left to prime

ratio_rp = specr[:,1]/specp[:,1] #take ratio of right to prime

ratio_lr = specl[:,1]/specr[:,1] #take ratio of left to right

np.savetxt(savepath+'ratio_lp_6',np.transpose(np.vstack((specl[:,0],ratio_lp)))) #saves left to prime ratio

np.savetxt(savepath+'ratio_rp_6',np.transpose(np.vstack((specl[:,0],ratio_rp)))) #saves right to prime ratio

np.savetxt(savepath+'ratio_lr_6',np.transpose(np.vstack((specl[:,0],ratio_lr)))) #saves left to right ratio
