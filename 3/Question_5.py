import numpy as np
import matplotlib.pyplot as plt


w = np.arange(-np.pi, np.pi, 0.2)

y = (w*1j*np.exp(-2*1j*w)) / (0.2+w*1j);

magnitude = np.abs(y)
phase = np.angle(y)

fig, (ax_mag, ax_phase) = plt.subplots(2, 1, sharex=True)

ax_mag.set_title("Magnitude")
ax_mag.plot(w, magnitude, color='C0')
ax_mag.set_xlabel("W")
ax_mag.set_ylabel("Magnitude")

ax_phase.set_title("Phase")
ax_phase.plot(w, phase, color='C1')
ax_phase.set_xlabel("W")
ax_phase.set_ylabel("Phase")

plt.show()