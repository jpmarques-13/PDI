import numpy as np
import cv2
from scipy.stats import mode


img = cv2.imread('ruido.jpg',0) # imagem tons de cinza
def median_filter(image,n):
    output = np.zeros_like(image)
    padded_x = image.shape[0] + (n- 1)
    padded_y = image.shape[1] + (n - 1)
    image_padded = np.zeros((padded_x,padded_y))
    w_x = int((n - 1)/2)
    w_y = int((n - 1)/2)
    image_padded[w_x:-w_x, w_y:-w_y] = image
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            y_end = y+n
            x_end = x+n
            output[x,y]=np.max(image_padded[x:x_end,y:y_end])
    return output
gray_image = median_filter(img,3)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey(0)
