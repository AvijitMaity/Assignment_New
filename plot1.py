'''
Author :Avijit Maity
Date and Time: 06/11/2019
This progam verfies the CMB data with theory
'''
import numpy as np
import matplotlib.pyplot as plt

def Bnewbar2_725K(f): #this fucntion calculates the Spectral Iiradiance of a BB at 2.725K
	h = 6.626 * 10**-34.0 #units Js
	c = 3.0*10**8.0 # units ms^-1
	kB = 1.38064852 * 10**-23.0 # S.I units
	T = 2.725 #K

	val = (2.0*h*c*f**3.0)/((np.exp((h*c*f)/(kB*T))-1.0))*10**20 # unit MJy/sr
	return val
'''
This sections creates data poins for plotting BB radiation of a BB at 2.725K
'''
wavno = np.arange(2.20,22.20,0.01) # units cm^-1
plt.xlabel("Wave Number 1/λ (in $cm^-$)")
plt.ylabel("Intenity B$_λ$ (in MJy/sr)")
'''
This section finds the wavenumber at which the BB peaks
'''

I = Bnewbar2_725K(100*wavno)
maxval = "The peak value at "+str(wavno[np.where(I == np.amax(I))[0]])

'''
This section plots the data from NASA
'''

wavno_data = np.loadtxt("C:/Users/USER/Documents/nasa.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (0))
Irradiance_data = np.loadtxt("C:/Users/USER/Documents/nasa.txt",dtype = 'float',comments = '#',delimiter = None,usecols = (1))

plt.scatter(wavno_data , Irradiance_data, color = 'red', label='NASA Data', s = 12.0)
plt.plot(wavno, Bnewbar2_725K(100.0*wavno),label='Planck\'s Law at T = 2.725K', color = 'green')
plt.legend(loc = 'upper right', frameon = True, shadow = True)
plt.title("Comparing CMB background with 2.725K BB")
plt.text(12.5,200,maxval)
plt.grid(True)
plt.show()