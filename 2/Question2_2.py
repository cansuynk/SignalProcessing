import wave
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

#I am not sure this code is correct or not. I tried to take the coefficients of the fourier transforms of my voices and reduce their dimensions by using pca. 
#I did a lot of research and I worked on it. I do not know that my code is okay or not. That's why I was able to do just that.
#My voice records

wr1 = wave.open('1.wav', 'r')
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

#I read the names of the voice files from a array called "name"
name=[wr1,wr2,wr3,wr4,wr5,wr6,wr7,wr8,wr9,wr10,wr11,wr12,wr13,wr14,wr15,wr21,wr22,wr23,wr24,wr25,wr26,wr27,wr28,wr29,wr30,wr31,wr32,wr33,wr34,wr35]

sz = 44100 # Read and process 1 second at a time.
period=1
time=1
N=100


def cn(n):												
   c = lf1[n]
   return c.sum()/c.size

def f(x, Nh):
   f = np.array([1/period*cn(i)*np.exp(-1j*2*i*np.pi*x/period) for i in range(1,Nh+1)])   #Finding the coefficients of the Fourier Transform of "ONE"
   return f.sum()

def cn2(n):
   c = lf2[n]
   return c.sum()/c.size

def f2(x, Nh):
   f = np.array([1/period*cn2(i)*np.exp(-1j*2*i*np.pi*x/period) for i in range(1,Nh+1)])  #Finding the coefficients of the Fourier Transform of "TWO"
   return f.sum()  
   
da = np.fromstring(name[0].readframes(sz), dtype=np.int16)			 #convert wav file to the readable signal of "ONE"
left1 = da[0::2]													 #select left to plot a figure of the sound and the frequencies of the left channel
lf1 = np.fft.rfft(left1)											 #Taking Fourier Transform of the signal
y2 = np.array([f(t,N).real for t in range(0,N)])					 #Finding the coefficients of the Fourier Transform

da2 = np.fromstring(name[15].readframes(sz), dtype=np.int16)		#convert wav file to the readable signal of "TWO"
left2= da2[0::2]													#select left to plot a figure of the sound and the frequencies of the left channel
lf2 = np.fft.rfft(left2)											#Taking Fourier Transform of the signal
y1 = np.array([f2(t,N).real for t in range(0,N)])					#Finding the coefficients of the Fourier Transform

a = plt.subplot(311)												#Plotting the coefficients of the Fourier Transform of "ONE" and "TWO"
plt.plot(y2,'bo',color='r')
a.set_title('The coefficients of the Fourier Transform of "One"')	
a = plt.subplot(312)
plt.plot(y1,'bo',color='b')
a.set_title('The coefficients of the Fourier Transform of "Two"')	


for i in range(0,15):			#reduce dimension for the voices of "ONE"

	da = np.fromstring(name[i].readframes(sz), dtype=np.int16)
	left1 = da[0::2]
	lf1 = np.fft.rfft(left1)
	y2 = np.array([f(t,N).real for t in range(0,N)])

	
	test = y2.reshape(10, 10)           #reshape the coefficients' array

	pca = PCA(n_components=5)			#select the number of pca components
	pca.fit(test)

	X_pca = pca.transform(test)			#reduce dimension

	X_new = pca.inverse_transform(X_pca)
	
	a = plt.subplot(313)
	a.set_title('Dimension reduction of the first and second graphs')
	plt.scatter(X_new, X_new, alpha=0.8,color='r')


for i in range(15,30):		#reduce dimension for the voices of "TWO"

	da2 = np.fromstring(name[i].readframes(sz), dtype=np.int16)
	left2 = da2[0::2]
	lf2 = np.fft.rfft(left2)
	y1 = np.array([f2(t,N).real for t in range(0,N)])

	test = y1.reshape(10, 10)		#reshape the coefficients' array

	pca = PCA(n_components=5)		#select the number of pca components
	pca.fit(test)

	X_pca = pca.transform(test)		#reduce dimension
	
	X_new = pca.inverse_transform(X_pca)

	a = plt.subplot(313)
	plt.scatter(X_new, X_new, alpha=0.8,color='b')

plt.show()



