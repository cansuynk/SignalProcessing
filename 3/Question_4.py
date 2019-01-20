from scipy import signal
import matplotlib.pyplot as plt
import numpy as np


#t = np.linspace(-1, 2, 200, endpoint=False)	#Create square wave 0<= t <=1
#sq_wave = np.repeat([0, 1, 0], 100)

t = np.linspace(0, 2, 200, endpoint=False)
sq_wave = np.repeat([1, 0], 100)

conva = signal.convolve(sq_wave, sq_wave, mode='same')/sum(sq_wave) #This is first convolution of the wave and itself

#I want to show 4 plots: original wave, convolution 1 times, convolution 10 times and convolution 100 times:
fig, (ax_wave, ax_con, ax_con_10, ax_con_100) = plt.subplots(4, 1, sharex=True)
ax_wave.plot(t, sq_wave)				#Plot original square wave

ax_wave.set_title('Square Wave')	#Set its title



ax_con.plot(t, conva)								#Plot first convolution
ax_con.set_title('Convolution with itself')		#Set its title


for i in range(0,10):							#convolution 10 times
	conva = signal.convolve(sq_wave, conva, mode='same')/sum(conva)
	ax_con_10.plot(t, conva)
	ax_con_10.set_title('Convolution with itself 10 times')	#Set plot title
	

for i in range(0,90):		#convolution 100 times(I have already take convolution 10 times we need 90 times more.)
	conva = signal.convolve(sq_wave, conva, mode='same')/sum(conva)
	ax_con_100.plot(t, conva)
	ax_con_100.set_title('Convolution with itself 100 times')  #Set plot title

plt.xlim(-3, 3)

plt.show()