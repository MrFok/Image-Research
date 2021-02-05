# Ricky Fok
# Image Processing and Retrieval Research 
# Led by Dr. Korah
# Class to generate Scale Space

import cv2
import numpy as np
import copy
import os
import matplotlib.pyplot as plt

class OctaveGenerator:

    def __init__(self, img, blurNum, sigma):
        self.img = img
        self.sigma = sigma
        self.blurNum = blurNum
        self.blur_ksize = (15,15) 
        self.arrData = np.asarray(self.img)
        self.space = [0] * blurNum   # array representing octaves with blur levels

    def displayOGImg(self):
        plt.imshow(self.img, cmap='gray')
        plt.show()

    def createOctaves(self):
        initialImg = self.img
        tempSig = self.sigma
        for x in range(self.blurNum):
            if x == 0:
                print(f"Blur {self.blurNum} Generated")
                self.space[x] = initialImg
                x += 1
            else:
                tempImg = cv2.GaussianBlur(initialImg, self.blur_ksize, sigmaX=self.sigma*1.6, sigmaY=self.sigma*1.6)
                self.space[x] = tempImg
                tempSig = tempSig * (2 ** 0.5)  #sigma differ by factor of root 2
                x += 1

        for y in range(len(self.space)):
            k = cv2.waitKey(0) & 0xFF
            if(k == 32):
                cv2.imshow(self.space[y])   
            y += 1
        cv2.waitKey(0)
        cv2.destroyAllWindows()



