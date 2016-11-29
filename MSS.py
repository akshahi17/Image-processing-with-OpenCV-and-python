import cv2
import numpy as np
import PIL as pl
from PIL import Image
import matplotlib.pyplot as plt


org = cv2.imread("char.jpg",1)
one = cv2.imread("char.jpg",1)
img = cv2.imread("char.jpg",1)
img2 = cv2.imread("char.jpg",1)
img3 = cv2.imread("char.jpg",1)
img4 = cv2.imread("char.jpg",1)
img5 = cv2.imread("char.jpg",1)
img6 = cv2.imread("char.jpg",1)
img7 = cv2.imread("char.jpg",1)
img8 = cv2.imread("char.jpg",1)
#cv2.imshow("img:" ,img)

#img = cv2.imread("flowers.jpg",1)
#cv2.pyrMeanShiftFiltering(img,.1,30)



#create a tuple of array vlaues from 0-255 to represent the intensity of
#the current colors

#define the width adn height and z because now its 
#treated as 3 dimesnional objects



no_rows = img.shape[0]
no_cols = img.shape[1]
no_colrs = img.shape[2]

def MSS2(img): 
     for x in range(no_rows-1):
        for y in range(no_cols-1):
            b = img[x,y,0]
            g = img[x,y,1]
            r = img[x,y,2]
            #grab random intesity region
            H = (img[50,50,0] + img[50,50,1] + img[50,50,2])
            Hlow = H/2
            Hhigh = H*4/1.5 
            #criteria for setting hues of colors for regions
            #define different colors to base it off of
            #so new color difference can be set based on color criteria from
            #the new color
            #        B   G   R 
            bnew = 0
            gnew = 0
            rnew = 0
            curColor = (b,g,r)
            newbC = (bnew,g,r)
            newgC = (b,gnew,r)
            newrC = (b,gnew,r)
            if b> r and b > g:
                bnew = 0
                
                newC = (bnew,g,r)
                newAvgColor = ((curColor[1] + newbC[1])/2),((curColor[0] + newbC[0])/2),((curColor[2] + newbC[2])/2)
                img[x,y] = newAvgColor
            if r >  g and r > b:
                rnew = 0
               
                newC = (b,g,rnew)
                newAvgColor = ((curColor[1] + newrC[1])/2),((curColor[0] + newrC[0])/2),((curColor[2] + newrC[2])/2)
                img[x,y] = newAvgColor
            if g> r and g> b:
                gnew = 0
                newAvgColor = ((curColor[1] + newgC[1])/2),((curColor[0] + newgC[0])/2),((curColor[2] + newgC[2])/2)
                img[x,y] = newAvgColor
            





def MSS(img): 
     for x in range(no_rows-1):
        for y in range(no_cols-1):
            b = img[x,y,0]
            g = img[x,y,1]
            r = img[x,y,2]
            #grab random intesity region
            H = (img[50,50,0] + img[50,50,1] + img[50,50,2])
            Hlow = H/2
            Hhigh = H*4/1.5 
            #criteria for setting hues of colors for regions
            #define different colors to base it off of
            #so new color difference can be set based on color criteria from
            #the new color
            #        B   G   R 
            bnew = 0
            gnew = 0
            rnew = 0
            if b <= Hlow:
                    bnew = Hlow
            if b >= H and b < Hhigh:
                    bnew = H
            if b >= Hhigh:
                    bnew = Hhigh            
            if r <= Hlow:
                    rnew = Hlow
            if r >= H and b < Hhigh:
                    rnew = H
            if r >= Hhigh:
                    rnew = Hhigh        
            if g <= Hlow:
                    gnew = Hlow
            if g >= H and b < Hhigh:
                    gnew = H
            if g >= Hhigh:
                    gnew = Hhigh   
            curColor = (bnew,gnew,rnew)
            img[x,y] = curColor

#this will create a new image with thresholds to a more segmented value
#next function will average out other pixels
def segColorIMG(img):
 for x in range(no_rows):
     for y in range(no_cols):
         for z in range(no_colrs):
            
            if img[x,y,z] <= 50 :
                #determine main color
                    img[x,y,z] = 25
            if img[x,y,z] > 70 and img[x,y,z] <= 80:
                     img[x,y,z] = 60
            if img[x,y,z] > 80 and img[x,y,z] <= 90:
                     img[x,y,z] = 95
            if img[x,y,z] > 90 and img[x,y,z] <= 110:
                     img[x,y,z] = 105
            if img[x,y,z] > 110 and img[x,y,z] <= 140:
                     img[x,y,z] = 145
            if img[x,y,z] > 140 and img[x,y,z] <= 150:
                     img[x,y,z] = 175
            if img[x,y,z] > 150 and img[x,y,z] <= 190:
                     img[x,y,z] = 195
            if img[x,y,z] > 190 and img[x,y,z] <= 210:
                     img[x,y,z] = 205
            if img[x,y,z] > 210 and img[x,y,z] <= 230:
                     img[x,y,z] = 225
            if img[x,y,z] > 230 and img[x,y,z] <= 255:
                     img[x,y,z] = 240
def avgSegColorIMG(img):
 for x in range(no_rows):
     for y in range(no_cols):
         for z in range(no_colrs):
            if img[x,y,z] <= 25 :
                #determine main color
                    img[x,y,z] = 0
            if img[x,y,z] > 26 and img[x,y,z] <=60 :
                     img[x,y,z] = 35
            if img[x,y,z] > 61 and img[x,y,z] <= 95:
                     img[x,y,z] = 80
            if img[x,y,z] > 96 and img[x,y,z] <= 105:
                     img[x,y,z] = 100
            if img[x,y,z] > 106 and img[x,y,z] <= 145:
                     img[x,y,z] = 120
            if img[x,y,z] > 146 and img[x,y,z] <= 175:
                     img[x,y,z] = 150
            if img[x,y,z] > 176 and img[x,y,z] <= 195:
                     img[x,y,z] = 180
            if img[x,y,z] > 196 and img[x,y,z] <= 205:
                     img[x,y,z] = 200
            if img[x,y,z] > 205 and img[x,y,z] <= 240:
                     img[x,y,z] = 210
def avgSegColorIMG2(img):
 for x in range(no_rows):
     for y in range(no_cols):
         for z in range(no_colrs):
            if img[x,y,z] >= 0 and img[x,y,z] <=80 :
                     img[x,y,z] = 45
            if img[x,y,z] > 81 and img[x,y,z] <= 150:
                     img[x,y,z] = 90
            if img[x,y,z] > 150 and img[x,y,z] <= 200:
                     img[x,y,z] = 140
            if img[x,y,z] > 200 and img[x,y,z] <= 210:
                     img[x,y,z] = 190
def avgSegColorIMG3(img):
 for x in range(no_rows):
     for y in range(no_cols):
         for z in range(no_colrs):
            if img[x,y,z] >= 0 and img[x,y,z] <= 90:
                     img[x,y,z] = 20
            if img[x,y,z] > 91 and img[x,y,z] <= 140:
                     img[x,y,z] = 50
            if img[x,y,z] > 141 and img[x,y,z] <= 190:
                     img[x,y,z] = 120
def avgSegColorIMG4(img):
 for x in range(no_rows):
     for y in range(no_cols):
         for z in range(no_colrs):
            if img[x,y,z] >= 0 and img[x,y,z] <= 50:
                     img[x,y,z] = 10
            if img[x,y,z] > 51 and img[x,y,z] <= 120:
                     img[x,y,z] = 25
            if img[x,y,z] > 121:
                     img[x,y,z] = 220
def avgSegColorIMG5(img):
 for x in range(no_rows-1):
     for y in range(no_cols-1):
         for z in range(no_colrs-2):
            if img[x+1,y+1,z+1] > 0 and img[x,y,z] <= 0:

                     img[x,y,z] = img[x+1,y+1,z+1]
                     
def didnotWork(img):
 img = Image.open('flowers.jpg')
 F = np.zeros(shape =(166500,333)) 
 rows = F.shape[0]
 cols = F.shape[1]
 for y in range(rows-1):
    for x in range(cols-1):
        rgb_img = img.convert('RGB')
        r, g, b = rgb_img.getpixel((x, y))
        #feature matrix
        F = np.append([r,g,b],[x,y])
        
        





img = cv2.blur(img,(4,4))
img2 = cv2.blur(img,(4,4))
img3 = cv2.blur(img,(4,4))
img4 = cv2.blur(img,(4,4))
#img5 = cv2.blur(img,(4,4))
#img6 = cv2.blur(img,(4,4))


#segColorIMG(one)
avgSegColorIMG(img)
avgSegColorIMG2(img2)
avgSegColorIMG3(img3)
avgSegColorIMG4(img4)
#MSS(img5)
#MSS2(img6)
#MSS(img7)
#MSS(img7)
#MSS2(img8)
#MSS2(img8)

#cv2.pyrMeanShiftFiltering(img,30,60)
#avgSegColorIMG4(img)
#avgSegColorIMG2(img)
#avgSegColorIMG3(img)
#avgSegColorIMG4(img)
#newapproach(img)
cv2.imshow("original", org)
#cv2.imshow("one",one)

#cv2.imshow("techniqueMSS", img5)
#cv2.imshow("techniqueMSS2", img6)
#cv2.imshow("techniqueMSSdouble", img7)
#cv2.imshow("techniqueMSS2double", img8)
print"done:"         
plt.subplot(2,5,1),plt.imshow(org,cmap = 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
######part 
plt.subplot(2,5,2),plt.imshow(img,cmap = 'gray')
plt.title(' first iteration'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,3),plt.imshow(img2,cmap = 'gray')
plt.title(' 2 iteration'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,4),plt.imshow(img3,cmap = 'gray')
plt.title(' 3 iteration'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,5),plt.imshow(img4,cmap = 'gray')
plt.title(' 4 iteration'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,6),plt.imshow(img5,cmap = 'gray')
plt.title(' MSS'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,7),plt.imshow(img6,cmap = 'gray')
plt.title(' MSS2'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,8),plt.imshow(img7,cmap = 'gray')
plt.title(' mss second'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,9),plt.imshow(img8,cmap = 'gray')
plt.title(' mss2 second iteration'), plt.xticks([]), plt.yticks([])

plt.subplot(2,5,10),plt.imshow(one,cmap = 'gray')
plt.title(' first segmented areas'), plt.xticks([]), plt.yticks([])
#plt.show()


