import matplotlib.pyplot as plt
import numpy as np


t = np.arange(-250,250)
n = np.zeros((500,), dtype=complex) #n is array and type is complex
n[50:60] = 2 + 4*np.exp(1j*5/4*np.pi) - 3*np.exp(1j*(-np.pi)/2) + 3*np.exp(1j*np.pi*(-0.25)) #x(t) signal
s = np.fft.ifft(n)


plt.plot(t, s.real, 'b-', t, s.imag, 'r--') #real is straight line, imaginary is dashed line
plt.legend(('real', 'imaginary'))	#lines information
plt.axis(xmin=-300, xmax=300)    	#limit x_axis from -300 to 300
plt.show()