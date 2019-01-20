import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal
import scipy.io.wavfile

sampling_rate = 44100

beginning_pt = 10000
end_pt = 25000

s = wave.open('idea.wav', 'r')
s_t = np.fromstring(s.readframes(sampling_rate), dtype=np.int16)
s_t = s_t[0::2]
#read .mat file
firfilter = scipy.io.loadmat('firFilter_b_Coeffs.mat')

filter = firfilter['b'] 	#read data in the .mat file
filter = filter.ravel()		#convert it to 1D array

#Compute the frequency response of the filter whose coefficients
w, h = signal.freqz(filter)


#since I will study in frequency domain, I convert the signal to discrete signal
s_t = np.fft.fft(s_t)	


#in frequency domain convolution turns into multiplication 
#equalize length of the arrays to do multiplication
#I added 0 to the end of w until arrays were equal.
w = np.pad(w, (0, len(s_t)-len(w)), 'constant')
x_f = s_t * w


T = 1.0		#duration
x = np.linspace(0.0, sampling_rate*T, T)

#I chose 8.5 kHz(between 8 kHz and 9 kHz : carrier frequency)
fc = 8500	
y = np.cos(2.0*np.pi*fc*x)
y = np.fft.fft(y)	#take FFT of cos
y_f =  1/(2*np.pi)*signal.convolve(y, x_f, mode='full')	#the frequency domain of multiplication
y_t =  np.fft.ifft(y_f)	#take inverse FFT


#I chose a different carrier frequency: 9.5 kHz
fc2 = 9500
phase = 45 #We have phase
ww = np.cos(2.0*np.pi*fc2*x+phase)
ww = np.fft.fft(ww)
w_f = 1/(2*np.pi)*signal.convolve(ww, y_f, mode='full')

w_t = np.fft.ifft(w_f)

v_f = w_f * w  #multiply with the filter.

v_t = np.fft.ifft(v_f) #converted discrete signal to time domain.

fig, plots = plt.subplots(nrows=4, ncols=1, figsize=(7, 7))

plots[0].set_title("After second cosine with the phase")
plots[0].plot(w_t, color='C5')
plots[0].set_xlim(beginning_pt, end_pt)


plots[1].plot(abs(w_t), color='C5')
plots[1].set_xlim(beginning_pt, end_pt)

plots[2].set_title("The Signal After Filtering")
plots[2].plot(v_t, color='C4')
plots[2].set_xlim(beginning_pt, end_pt)


plots[3].plot(abs(v_t), color='C4')
plots[3].set_xlim(beginning_pt, end_pt)

plt.show()
s.close()