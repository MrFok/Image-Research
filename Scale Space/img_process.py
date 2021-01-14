# Ricky Fok
# Image Processing and Retrieval Research 2020
# Led by Dr. Korah
# SIFT Scale Space. Loads images and presents user with 4 octaves and 4 blur levels 


import cv2
import numpy as np
import copy
import os

global img
global images
global oNum
global bNum

def main():
    img = cv2.imread('cat_image.jpg')
    img = cv2.resize(img, (0,0), fx = 2, fy = 2)    #double initial image
    
    oNum = input("How many octave levels: ") #number of octaves
    bNum = input("How many blur levels: ")   #number of blurs

    rows, cols, _channels = map(int, img.shape)     #retrieves rows and cols

    scalingImg = img
    printOctave(img, 1, int(bNum))
    x = 2
    while x <= int(oNum):
        scalingImg = cv2.pyrDown(scalingImg, dstsize = (cols // 2, rows // 2))    #halfs image size
        rows, cols, _channels = map(int, scalingImg.shape)     #updates rows and cols
        printOctave(scalingImg, x, int(bNum))
        x = x + 1
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def printOctave(image, oNumLvl, bNum):
    tempImg = image
    cv2.imshow('Octave ' + str(oNumLvl), tempImg)
    blurLvlNum = 3
    levelNum = 1

    for x in range(bNum):
        tempImg = cv2.GaussianBlur(tempImg, (blurLvlNum, blurLvlNum), 0)
        k = cv2.waitKey(0) & 0xFF
        if k == 32:
            cv2.imshow('Octave ' + str(oNumLvl) + ': Blur ' + str(levelNum), tempImg)
            levelNum = levelNum + 1
            blurLvlNum = blurLvlNum + 2
        elif k == 27:
            cv2.destroyAllWindows()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()

             
