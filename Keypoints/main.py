# Ricky Fok
# Image Processing and Retrieval Research 
# Led by Dr. Korah
# Class to generate Scale Space

import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from ScaleSPGen import OctaveGenerator

def main(): # main method
    oNum = 4    # input("How many octave levels: ") #number of octaves
    bNum = 5    # input("How many blur levels: ")   #number of blurs
    sigNum = 0.707103   #input("Sigma Value: ") #TODO check sigma value
    mainImg = readImg()
    scaleSpace = OctaveGenerator(mainImg, int(bNum), float(sigNum))
    scaleSpace.createOctaves()
    #scaleSpace.displayOGImg()

def readImg():  # reads in image
    img = cv2.imread('cat_image.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #allows for correct matplotlib display since in RGB instead of BGR
    img = cv2.resize(img, (0,0), fx = 2, fy = 2) #doubles image size
    img = cv2.GaussianBlur(img, (3,3), sigmaX=0.707103, sigmaY=0.707103)    #anti-alliasing TODO: check sigma values
    return img

if __name__ == '__main__':
    main()
