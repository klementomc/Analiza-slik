import cv2 
import numpy as np
import os
import matplotlib.pyplot as plt

class Slika:


    def __init__(self, ime_slike):
        self.ime_slike = ime_slike

    def preberi_sliko_GREY(self):
        self.slika = cv2.imread(str(self.ime_slike), cv2.IMREAD_GRAYSCALE)
        return self.slika
    
    def transformiraj_crno_belo(self, prag):
        for i in range(0, self.slika.shape[0]):
            for j in range(0, self.slika.shape[1]):
                if self.slika[i][j] > prag:
                    self.slika[i][j] = 255
                else:
                    self.slika[i][j] = 0
        return self.slika
    
    def find_edges(self):
        edges = cv2.Canny(self.slika, 50, 150)
        mask = np.zeros_like(edges)
        height, width = mask.shape[:2]
        polygons = np.array([[(0, height), (width, height), (width, height*2/3), (0, height*2/3)]], dtype=np.int32)
        cv2.fillPoly(mask, polygons, (255, 255, 255))

        self.slika = cv2.bitwise_and(self.slika, mask)
        return self.slika

    
    def prikazi_sliko(self, slika):
        plt.imshow(self.slika, cmap='gray')
        plt.show()


slika = Slika("S00010000015.png")
slika.preberi_sliko_GREY()
slika.transformiraj_crno_belo(30)
slika.find_edges()
slika.prikazi_sliko(slika.slika)