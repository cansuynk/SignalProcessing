import numpy as np
import matplotlib.pyplot as plt


N = 1048

x = np.linspace(0, 1, N)

signal = lambda t: 2 + (4*np.cos(500*np.pi*t) +(5/6*np.pi))-3* np.sin(60*np.pi*t)+ (3*np.cos(250*np.pi*t) +(-0.25*np.pi))  #x(t) signal

f = np.array(signal(x))
F = np.fft.fft(f)
Fo = F.copy()       # for printing the unfiltered spectrum
freq = np.fft.fftfreq(len(f), 1/N)



ff = np.fft.ifft(F)


plt.plot(freq, abs(Fo)/N, label='phase of the complex amplitudes')
plt.axis(xmin=-300, xmax=300)	#limit x_axis from -300 to 300
plt.axis(ymin=0, ymax=2)		#limit y_axis from 0 to 2
plt.legend() #line information


plt.show()