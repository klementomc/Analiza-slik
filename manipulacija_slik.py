import cv2 
import numpy as np
import os
import matplotlib.pyplot as plt
import slika

slike_raw = os.listdir()
slike = []
for file in slike_raw:
    if file.endswith(".png"):
        slike.append(file)


slike_modificirane = []
for slika in slike:
    img = cv2.imread(slika, cv2.IMREAD_GRAYSCALE)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
            if img[i][j] > 30:
                img[i][j] = 255
            else:
                img[i][j] = 0
    slike_modificirane.append(img)
    plt.imshow(img, cmap='gray')
    plt.show()
    






