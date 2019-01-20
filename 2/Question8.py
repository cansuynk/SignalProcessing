from scipy import signal
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


image = Image.open('noisyCameraman.png').convert('L')


kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9.0
				   

con_imag = signal.convolve2d(image, kernel, 'valid')


fig, (orig_imag, new_imag) = plt.subplots(1, 2, figsize=(50, 50))

orig_imag.imshow(image, cmap='gray')
orig_imag.set_title('Original Image')
new_imag.imshow(con_imag, cmap='gray')

plt.show()
