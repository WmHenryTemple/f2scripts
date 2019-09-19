#!/usr/bin/env python
# coding: utf-8

# In[50]:


#!/usr/bin/env python

import math as ma
import numpy as np
import scipy as sc
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

#%matplotlib inline

data=np.loadtxt("deltaSlicesSigma.dat")
data1=np.loadtxt("numEntries.dat")
data.shape

#Find a better way
run=data[:,0]
m1=data[:,1]
s1=data[:,2]
m2=data[:,3]
s2=data[:,4]
m3=data[:,5]
s3=data[:,6]
m4=data[:,7]
s4=data[:,8]
m5=data[:,9]
s5=data[:,10]
m6=data[:,11]
s6=data[:,12]
m7=data[:,13]
s7=data[:,14]
m8=data[:,15]
s8=data[:,16]

#NUmber of entries
e0=data1[:,0]
e1=data1[:,1]
e2=data1[:,2]
e3=data1[:,3]
e4=data1[:,4]
e5=data1[:,5]
e6=data1[:,6]
e7=data1[:,7]
e8=data1[:,8]

plt.tight_layout()




fig, ax=plt.subplots(4,2)#,sharey=True,sharex=True)

left = 0.125  # the left side of the subplots of the figure
right = 0.9   # the right side of the subplots of the figure
bottom = 0.1  # the bottom of the subplots of the figure
top = 0.9     # the top of the subplots of the figure
wspace = 0.2  # the amount of width reserved for space between subplots,
              # expressed as a fraction of the average axis width
hspace = 0.4  # the amount of height reserved for space between subplots,
              # expressed as a fraction of the average axis height

plt.subplots_adjust(left,bottom,right,top,wspace,hspace)

ax1 = ax[0,0]
ax2 = ax[0,1]
ax3 = ax[1,0]
ax4 = ax[1,1]
ax5 = ax[2,0]
ax6 = ax[2,1]
ax7 = ax[3,0]
ax8 = ax[3,1]

for i in range(4):
    for k in range(2):
#        print('Hello',i,k)
        ax[i,k].set_ylabel('Sigma')
#        ax[i,k].set_xlabel('Run')
#        ax[i,k].set_xlim([2400,3200])
        ax[i,k].set_ylim([0,.1])
        ax[i,k].grid()
#        ax[i,k].set_xticks(np.arange(2500,3200,100))
        ax[i,k].set_yticks(np.arange(0,.1,.02))
        ax[i,k].text(.9, -.3, '# of Events',
        horizontalalignment='center',
        verticalalignment='bottom',
        transform=ax[i,k].transAxes)

ax[0,0].title.set_text("-12.5$<\delta<$-7.5") 
ax[0,1].title.set_text("-7.5$<\delta<$-2.5") 
ax[1,0].title.set_text("-2.5$<\delta<$2.5") 
ax[1,1].title.set_text("2.5$<\delta<$7.5") 
ax[2,0].title.set_text("7.5$<\delta<$12.5") 
ax[2,1].title.set_text("12.5$<\delta<$17.5") 
ax[3,0].title.set_text("17.5$<\delta<$22.5") 
ax[3,1].title.set_text("22.5$<\delta<$27.5") 

#%matplotlib qt


ax1.errorbar(e1,m1,0,marker='.',linestyle='none')
ax2.errorbar(e2,m2,0,marker='.',linestyle='none')
ax3.errorbar(e3,m3,0,marker='.',linestyle='none')
ax4.errorbar(e4,m4,0,marker='.',linestyle='none')
ax5.errorbar(e5,m5,0,marker='.',linestyle='none')
ax6.errorbar(e6,m6,0,marker='.',linestyle='none')
ax7.errorbar(e7,m7,0,marker='.',linestyle='none')
ax8.errorbar(e8,m8,0,marker='.',linestyle='none')

#%matplotlib qt
plt.show()
# plt.savefig('meanVSrun.pdf')
#%matplotlib inline


# In[42]:


x=np.arange(2000,3000,1)


# In[43]:


x


# In[ ]:




