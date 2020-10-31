# Ricky Fok
# Image Processing and Retrieval Research 2020
# Led by Dr. Korah
# SIFT Scale Space. Loads images and presents user with 4 octaves and 4 blur levels 

import cv2
import numpy as np
import copy

def checkDestroy():     #check if needs to be destroyed
    k = cv2.waitKey(0) & 0xFF

    if k == 27:
        cv2.destroyAllWindows()

def calculateOctave(image):     #calculate each blur image in octave
    listOfImages[0] = image
    listOfImages[1] = cv2.GaussianBlur(image, (3,3), 0)
    listOfImages[2] = cv2.GaussianBlur(image, (5,5), 0)
    listOfImages[3] = cv2.GaussianBlur(image, (7,7), 0)
    listOfImages[4] = cv2.GaussianBlur(image, (9,9), 0)

def printOctave(theList, octave):    #prints octave with given starting image, list of blurred images, and octave level num
    blurLvl = 1
    cv2.imshow('Octave ' + str(octave), theList[0])    #deleting does now allow printing octave
    for x in range(1,5): 
        k = cv2.waitKey(0) & 0xFF
        if k == 32:
            cv2.imshow('Octave ' + str(octave) + ': Blur ' + str(blurLvl), theList[x])
            blurLvl = blurLvl + 1
        elif k == 27:
            cv2.destroyAllWindows()
    checkDestroy()    

octaveLvl = 0   #current octave
img = cv2.imread('cat_image.jpg')               # grabbing image
rows, cols, _channels = map(int, img.shape)     #retrieves rows and cols
blur1 = blur2 = blur3 = blur4 = img             #initializing blur images
listOfImages = [img, blur1, blur2, blur3, blur4] #initializing listOfImages


calculateOctave(img)
octaveLvl = octaveLvl + 1
printOctave(listOfImages, octaveLvl)
cv2.destroyAllWindows()

for i in range(1, 4):
    img = cv2.pyrDown(img, dstsize=(cols // 2, rows // 2)) #halfs image size
    rows, cols, _channels = map(int, img.shape)
    calculateOctave(img)
    octaveLvl = octaveLvl + 1
    printOctave(listOfImages, octaveLvl)
    cv2.destroyAllWindows()
    


