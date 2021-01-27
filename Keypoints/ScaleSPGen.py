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

    def __init__(self, img, blurNum):
        self.img = img
        self.arrData = np.asarray(self.img)
        self.space = [0] * blurNum   # 2D array representing octaves with blur levels

    def displayOGImg(self):
        plt.imshow(self.img, cmap='gray')
        plt.show()

    # def createOctaves():


