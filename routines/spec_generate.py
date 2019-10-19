#FINAL SPECTRUM GENERATON
import glob
import spec_from_file as spc
import numpy as np

specpath='/home/atom/2018_07_27 TLE Jaisalmer/2018_07_28 TLE Jaisalmer spectro data'+\
         '/Fire Cap/'
         
savepath='/home/atom/2018_07_27 TLE Jaisalmer/Analysis/spectra/'

typs={0:'_Right',1:'_Prime',2:'_Left'}

txtlist=[]
for i in range(len(typs)):    
    txtlist.append(sorted(glob.glob(specpath+'*'+typs[i]+'*'+'.txt')))

fitlist=[[] for i in range(len(typs))]
for i in range(len(typs)):
    for j in range(len(txtlist[i])):
        fitlist[i].append(sorted(glob.glob(txtlist[i][j].replace('.txt','*.fit'))))    

i=2
lamb=np.arange(400.,700.1,0.1)
spctrm=np.vstack((lamb,np.zeros(lamb.shape)))
 
for j in [1,2,3]:
   for k in range(len(fitlist[i][j])):
        spec=spc.spec(fitlist[i][j][k])
        spctrm[1]+=spec[1]


spctrm[1] *= 100000/np.max(spctrm[1])

#np.savetxt(savepath+'spec'+typs[i]+'_2',np.transpose(spctrm),delimiter='\t')       
