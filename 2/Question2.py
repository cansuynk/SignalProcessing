import wave
import numpy as np
import matplotlib.pyplot as plt

#this code shows the graphs of the Fourier Transform of my voices("One" and "Two")

wr1 = wave.open('1.wav', 'r')						#My voice records
wr2 = wave.open('2.wav', 'r')
wr3 = wave.open('3.wav', 'r')
wr4 = wave.open('4.wav', 'r')
wr5 = wave.open('5.wav', 'r')
wr6 = wave.open('6.wav', 'r')
wr7 = wave.open('7.wav', 'r')
wr8 = wave.open('8.wav', 'r')
wr9 = wave.open('9.wav', 'r')
wr10 = wave.open('10.wav', 'r')
wr11 = wave.open('11.wav', 'r')
wr12 = wave.open('12.wav', 'r')
wr13 = wave.open('13.wav', 'r')
wr14 = wave.open('14.wav', 'r')
wr15 = wave.open('15.wav', 'r')
wr16 = wave.open('16.wav', 'r')
wr17 = wave.open('17.wav', 'r')
wr18 = wave.open('18.wav', 'r')
wr19 = wave.open('19.wav', 'r')
wr20 = wave.open('20.wav', 'r')
wr21 = wave.open('21.wav', 'r')
wr22 = wave.open('22.wav', 'r')
wr23 = wave.open('23.wav', 'r')
wr24 = wave.open('24.wav', 'r')
wr25 = wave.open('25.wav', 'r')
wr26 = wave.open('26.wav', 'r')
wr27 = wave.open('27.wav', 'r')
wr28 = wave.open('28.wav', 'r')
wr29 = wave.open('29.wav', 'r')
wr30 = wave.open('30.wav', 'r')
wr31 = wave.open('31.wav', 'r')
wr32 = wave.open('32.wav', 'r')
wr33 = wave.open('33.wav', 'r')
wr34 = wave.open('34.wav', 'r')
wr35 = wave.open('35.wav', 'r')
wr36 = wave.open('36.wav', 'r')
wr37 = wave.open('37.wav', 'r')
wr38 = wave.open('38.wav', 'r')
wr39 = wave.open('39.wav', 'r')
wr40 = wave.open('40.wav', 'r')

sz = 44100 # Read and process 1 second at a time.            I read the names of the voice files from a array called "name"
name=[wr1,wr2,wr3,wr4,wr5,wr6,wr7,wr8,wr9,wr10,wr11,wr12,wr13,wr14,wr15,wr16,wr17,wr18,wr19,wr20,wr21,wr22,wr23,wr24,wr25,wr26,wr27,wr28,wr29,wr30,wr31,wr32,wr33,wr34,wr35,wr36,wr37,wr38,wr39,wr40]

for i in range(0,40):
	readd = np.fromstring(name[i].readframes(sz), dtype=np.int16)   #convert wav file to the readable signal
	left= readd[0::2]												#select left to plot a figure of the sound and the frequencies of the left channel

	lf = np.fft.rfft(left)											#Taking Fourier Transform of the signal
	
	if(i<21):														#There is 4 subplots.First 2 is about "One", last 2 is about "Two"
		plt.figure(1)
		a = plt.subplot(411)										#the graph of Fourier Transform "ONE"
		r = 2**16/2													#setting x and y axises.
		a.set_ylim([-r, r])
		a.set_title('The voice of One')								#name labels
		a.set_xlabel('time [s]')
		a.set_ylabel('sample value [-]')
		plt.plot(left)

		b = plt.subplot(412)										#the graph of amplitude "ONE"
		b.set_xscale('log')
		b.set_xlabel('frequency [Hz]')
		b.set_ylabel('|amplitude|')
		plt.plot(abs(lf))

	else:
		plt.figure(1)
		a = plt.subplot(413)										#the graph of Fourier Transform of "TWO"
		r = 2**16/2
		a.set_ylim([-r, r])											#setting x and y axises.
		a.set_title('The voice of Two')
		a.set_xlabel('time [s]')
		a.set_ylabel('sample value [-]')
		plt.plot(left)

		b = plt.subplot(414)										#the graph of amplitude of "TWO"
		b.set_xscale('log')
		b.set_xlabel('frequency [Hz]')
		b.set_ylabel('|amplitude|')
		plt.plot(abs(lf))

mng = plt.get_current_fig_manager()									#setting plot window
mng.resize(*mng.window.maxsize())
plt.show()
