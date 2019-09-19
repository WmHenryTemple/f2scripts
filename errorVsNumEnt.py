#!/usr/bin/env python

import math as ma
import numpy as np
import scipy as sc
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
#from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)

data=np.loadtxt("deltaSlicesMean.dat")
dataEnt=np.loadtxt("numEnt.dat")
data.shape

#Find a better way
ent1=dataEnt[:,1]
ent2=dataEnt[:,2]
ent3=dataEnt[:,3]
ent4=dataEnt[:,4]
ent5=dataEnt[:,5]
ent6=dataEnt[:,6]
ent7=dataEnt[:,7]
ent8=dataEnt[:,8]

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
        ax[i,k].set_ylabel('Error on Mean')
        ax[i,k].set_xlim([2400,3200])
        ax[i,k].grid()
        ax[i,k].set_xticks(np.arange(2500,3200,100))
        ax[i,k].text(.9, -.3, r'$\frac{\sqrt{N}}{N}$',
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

ax1.plot(ent1,s1,marker='.',linestyle='none')
ax2.plot(ent2,s2,marker='.',linestyle='none')
ax3.plot(ent3,s3,marker='.',linestyle='none')
ax4.plot(ent4,s4,marker='.',linestyle='none')
ax5.plot(ent5,s5,marker='.',linestyle='none')
ax6.plot(ent6,s6,marker='.',linestyle='none')
ax7.plot(ent7,s7,marker='.',linestyle='none')
ax8.plot(ent8,s8,marker='.',linestyle='none')

plt.show()
