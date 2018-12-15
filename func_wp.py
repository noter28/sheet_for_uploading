import os, sys
from PIL import Image #Python image library
directory =         'Chromophoto_IC' #first source

def wp(width,pix,b1,b2,height,img):
    pix3 = 0  #reset counter
    #if b2 == height:
     #   break
    for i in range(0, width):
        print(width)
        for j in range(b1, b2):
            q = (sum(pix[i, j]))
            if q!=765:
                break
            pix3+=q  #counter sum colours of all pixels in line
            print(pix3)
            #print(b1)
            return pix3