import wave
import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from scipy import signal

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


x_t = np.fft.ifft(x_f) #inverse Fourier Transform
#singal in time domain
fig, plots = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))

plots[0].set_title("The signal after filtering in Time Domain")
plots[0].plot(x_t, color='C2')
plots[0].set_xlim(beginning_pt, end_pt)
plt.xlabel('Time')


plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

plots[1].set_title("Spectrogram of My Filtered Voice")
plots[1].specgram(abs(x_t), NFFT=128, Fs=sampling_rate, noverlap=0)

plt.show()
s.close()