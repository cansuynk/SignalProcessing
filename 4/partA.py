import wave
import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 44100		#use sampling rate 44.1 kHz
#since the best test signal have lots of vowels, I recorded "idea".

s = wave.open('idea.wav', 'r')	#open wav file

#convert it to signal
s_t = np.fromstring(s.readframes(sampling_rate), dtype=np.int16)
s_t = s_t[0::2]

fig, plots = plt.subplots(nrows=2, ncols=1, figsize=(7, 7))

plots[0].set_title("Waveform of s(t)")	#plot the signal
plots[0].plot(s_t)
plt.xlabel('Time')
#I choose 10000 as beginning point and 25000 as end point
beginning_pt = 10000
end_pt = 25000


#plot significant speech activity 
plots[1].set_title("Significant Speech Activity")
plots[1].plot(s_t,  color='C1')
plots[1].set_xlim(beginning_pt, end_pt)

plt.show()
s.close()