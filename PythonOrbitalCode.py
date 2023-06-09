import numpy as np
import math
from scipy.special import sph_harm, genlaguerre
from colorspacious import cspace_converter
#from aquarel import load_theme
import os

import matplotlib.pyplot as plt
import cmasher as cmr


# function to provide stationary state solutions to Schrodingers equation for
# nonrelativistic Hydrogen atom ie wavefunctions
def HydrogenWF(n,l,m,X,Y,Z):
    R = np.sqrt(X**2+Y**2+Z**2)  #conversion form cartesian to spherical coordinates
    Theta = np.arccos(Z/R)
    Phi = np.arctan2(Y,X)

    Rho = 2.0*R/n # define parts; NB a0 constant dropped as only shape important
    SphericalHarm = sph_harm(m, l, Phi, Theta)
    LaguerrePoly = genlaguerre(n-l-1,2*l+1)(Rho)
    Prefactor = np.sqrt((2.0/n)**3*math.factorial(n-l-1)/(2.0*n*math.factorial(n+l)))
    # WaveFunction
    Psi = Prefactor*np.exp(-Rho/2.0)*Rho**l*SphericalHarm*LaguerrePoly
    Psi = np.nan_to_num(Psi) # remove infinities
    return Psi

# arrange grid
dz = 0.25 #Adjust this for finer image grains
zmin = -45 #Adjust to fit plot to probability cloud size
zmax = 45
x=y=z = np.arange(zmin,zmax,dz)
X,Y,Z = np.meshgrid(x,y,z)

# Quantum Numbers - Change these to change which orbital to plot.
# Rules:  where n=1,2,3... l=0,1,2,...,n-1 m=-l,...,l
# e.g for n=2 allowable m/l are: l=1 m=-1,0,1 / l=0 m=0
n = 3
l = 2
m = 1
#print(n,l,m)

#data = HydrogenWF(n,l,m,X,Y,Z)
#data = abs(data)**2 #probability density of electron is Psi squared
# Produces 3d numpy array size (n, n, n) where n is zmin +zmax 
        


for i in range(1,5):
    for j in range(0,i):
        for k in range(0,j+1):
        
            data = HydrogenWF(i,j,k,X,Y,Z)
            data = abs(data)**2 #probability density of electron is Psi squared
            # Produces 3d numpy array size (n, n, n) where n is zmin +zmax 
                   
            print(i,j,k)
            indexSlice=round((zmax*2*(1.0/dz))/2)
            dataslice=data[indexSlice]#*1e10   
            #plt.imshow(dataslice)
            
            maxcutoff=0# NOTEchanging this allows low probability shells to be seen in visualisation for visual reference
            
            logdata=np.log(dataslice)#takes log of array not great practice but useful to see what shape it should be
            
            #cmap = cmr.rainforest                   # CMasher
            #cmap = plt.get_cmap('cmr.blues')
            cmapname='jet'
            fig=plt.pcolormesh(logdata,vmin=None, vmax=maxcutoff, cmap=cmapname, norm=None)#
            #plt.colorbar(fig)
            plt.axis('off')
            N='nlm=%i' %i
            L='%i' %j
            M='%i' %k
            #plt.suptitle(N + L + M)
            name = N + L + M
            folder='newrainbowBIGGERrrrr'
            #os.mkdir("C://Users/BSULoan/Desktop/orbitals/PreparedMatter/%s" %(folder))
            #filename = "%s.png" % name
            #f = open(filename , 'wb')string % (name, age)
            
            plt.savefig("C://Users/BSULoan/Desktop/orbitals/PreparedMatter/%s/%s.png" %(folder,name), bbox_inches='tight', pad_inches = 0)
            plt.show()
            



            
#plot(dataslice)

# NOTES ON ELECTRONS
# Electrons exist as standing waves. Lowest states like fundamental frequency,
# higher energy states like harmonics.
# Electrons are never in single point location, probability of interacting with
# electron at single point found from the electron's wave function.
# The number of electrons orbiting a nucleus can be only an integer.
# Electrons jump between orbitals when energy lost or gained - discrete amounts.
