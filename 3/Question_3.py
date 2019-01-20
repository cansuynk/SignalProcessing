import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack


N = 100.0					# Sampling rate (Number of samplepoints)

T = 1.0 / (2*N)				# Sampling interval (sample spacing)
x = np.linspace(0.0, N*T, N)
signal_1=2*np.sin(10.0 * 2.0 * np.pi * x)				#Example signals: First Signal
signal_2=10*np.sin(10.0 * 2.0 * np.pi * x + np.pi/3)	#Second Signal
signal_3=5*np.cos(25.0 * 2.0 * np.pi * x - np.pi/2)		#Third Signal


fig, (ax_1, ax_2, ax_3, ax_4) = plt.subplots(4, 1, sharex=True) #There are 4 graphs

ax_1.plot(signal_1)				#All signals on a graph
ax_1.plot(signal_2)
ax_1.plot(signal_3)
ax_1.set_title('Signals')

signal_1_fft=scipy.fftpack.fft(signal_1)	#FFTs of the Signals
signal_2_fft=scipy.fftpack.fft(signal_2)
signal_3_fft=scipy.fftpack.fft(signal_3)

ax_2.plot(signal_1_fft)		#All FFTs of the signals on a graph
ax_2.plot(signal_2_fft)
ax_2.plot(signal_3_fft)
ax_2.set_title('Signals\' FFT')

y_1=signal_1_fft+signal_2_fft+signal_3_fft		#sum of FFT of the signals
ax_3.plot(y_1)
ax_3.set_title('Sum of FFT of Signals')

y_2=signal_1+signal_2+signal_3		#sum of the signals
y_fft = scipy.fftpack.fft(y_2)		#then take FFT of the sum of the signals
ax_4.plot(y_fft)					#and plot
ax_4.set_title('FFT of Sum of Signals')

plt.show()


