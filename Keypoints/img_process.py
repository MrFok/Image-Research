# Ricky Fok
# Image Processing and Retrieval Research 2020
# Led by Dr. Korah
# SIFT Scale Space. Loads images and presents user with 4 octaves and 4 blur levels 


import cv2
import numpy as np
import copy
import os

def printOctave(image, oNumLvl, bNumLvl):
    tempImg = image
    cv2.imshow('Octave ' + str(oNumLvl), tempImg)
    blurLvlNum = 3  # starting blur level
    blurIncr = 4    # blurring increment amount
    levelNum = 1
    listOfImg = [image] * (bNumLvl + 1)

    for x in range(bNumLvl):
        tempImg = cv2.GaussianBlur(tempImg, (blurLvlNum, blurLvlNum), 0)
        listOfImg[levelNum] = tempImg
        k = cv2.waitKey(0) & 0xFF
        if k == 32:
            cv2.imshow('Octave ' + str(oNumLvl) + ': Blur ' + str(levelNum), tempImg)
            levelNum = levelNum + 1
            blurLvlNum = blurLvlNum + blurIncr
        elif k == 27:
            cv2.destroyAllWindows()
    cv2.waitKey(0)
    getDoG(listOfImg, oNumLvl, bNumLvl)    #DoG portion
    cv2.destroyAllWindows()

def getDoG(listImg, oNumLvl, bNumLvl):
    x = 0
    tempArr = [listImg] * (bNumLvl)
    while x < (len(listImg) - 1):  # below is turing img to grayscale and subtracting to get DoG image
        dogImg = cv2.cvtColor(listImg[x], cv2.COLOR_BGR2GRAY) - cv2.cvtColor(listImg[x + 1], cv2.COLOR_BGR2GRAY) 
        tempArr[x] = dogImg
        k = cv2.waitKey(0) & 0xFF
        if k == 32:
           cv2.imshow('DoG Octave ' + str(oNumLvl) + ': Blur ' + str(x) + ' - Blur ' + str(x + 1), dogImg)
           x = x + 1
        elif k == 27:
            cv2.destroyAllWindows()
    cv2.waitKey(0)
    print("Number of DoGs: " + str(len(tempArr)))
    return tempArr

def locateApxKeypoints(imgT, imgC, imgB):    #locating approx. keypoints and com
    rows, cols = imgT.shape #grabbing image sizes
    #apxArr = [arrLen[0]] * (arrLen / 3)
    tempImage = np.zeros((cols, rows, 3), np.uint8) #creating image to put min and max points
    
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            
    


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


             
