import matplotlib.pyplot as plt
import numpy as np



t = np.arange(-0.2, 0.4, 0.00001)
W=10 * np.pi  #I select W = 10xpi

z1 = np.cos( W * t -(np.pi/3) )  		# z1 signal
z2 = 3 * np.sin(W * t -(5 * np.pi/4) ) 	# z2 signal
z3 = 2 * np.cos(W * t -4.7124 )			# z3 signal
x  = 4.17 * np.cos(W * t +51.1)			# x(t) = z1 + z2 + z3

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(7, 7)) #I display the graphs as a 2x2 matrix 



# plot time signals:
axes[0,0].set_title("z1 Signal")           #plotting z1 signal  
axes[0,0].plot(t, z1, color='C0')
axes[0,0].set_ylabel("Amplitude")
axes[0,0].set_ylim([-5,5])


axes[0,1].set_title("z2 Signal")			#plotting z2 signal 
axes[0,1].plot(t, z2, color='C1')
axes[0,1].set_ylim([-5,5])

axes[1,0].set_title("z3 Signal")
axes[1,0].plot(t, z3, color='C2')		#plotting z3 signal 
axes[1,0].set_xlabel("Time")
axes[1,0].set_ylabel("Amplitude")
axes[1,0].set_ylim([-5,5])

axes[1,1].set_title("x(t) Signal")
axes[1,1].plot(t, x, color='C3')		#plotting x(t) (x(t) = z1 + z2 + z3)
axes[1,1].set_xlabel("Time")
axes[1,1].set_ylim([-5,5])


plt.show()