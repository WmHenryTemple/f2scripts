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
        ax[i,k].set_ylim([0,.2])
        ax[i,k].grid()
 #       ax[i,k].set_xticks(np.arange(2500,3200,100))
#        ax[i,k].set_yticks(np.arange(.95,1.05,.01))
        ax[i,k].text(.9, -.3, 'Run #',
        horizontalalignment='center',
        verticalalignment='bottom',
        transform=ax[i,k].transAxes)

ax[0,0].title.set_text("-9$<\delta<$-6.75") 
ax[0,1].title.set_text("-6.75$<\delta<$-4.5") 
ax[1,0].title.set_text("-4.5$<\delta<$-2.25") 
ax[1,1].title.set_text("-2.25$<\delta<$0") 
ax[2,0].title.set_text("0$<\delta<$2.25") 
ax[2,1].title.set_text("2.25$<\delta<$4.5") 
ax[3,0].title.set_text("4.5$<\delta<$6.75") 
ax[3,1].title.set_text("6.75$<\delta<$9") 

#%matplotlib qt


ax1.errorbar(run,m1,s1,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax2.errorbar(run,m2,s2,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax3.errorbar(run,m3,s3,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax4.errorbar(run,m4,s4,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax5.errorbar(run,m5,s5,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax6.errorbar(run,m6,s6,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax7.errorbar(run,m7,s7,marker='.',linestyle='none',elinewidth=.3,ecolor='black')
ax8.errorbar(run,m8,s8,marker='.',linestyle='none',elinewidth=.3,ecolor='black')

#%matplotlib qt
plt.show()
# plt.savefig('meanVSrun.pdf')
#%matplotlib inline


# In[42]:


x=np.arange(2000,3000,1)


# In[43]:


x


# In[ ]:




