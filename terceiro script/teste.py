import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ruido.jpg')
gaussian = cv2.GaussianBlur(img,(5,5),0)
compare = np.concatenate((img, median), axis=1) #side by side comparison
plt.figure(10 10)
plt.imshow(numpy.hstack((img, gaussian)), cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
