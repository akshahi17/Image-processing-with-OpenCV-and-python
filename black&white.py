import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import ndimage

img = cv2.imread("temp.jpg",0)   
img = cv2.resize(img,(200,200))    

n_rows = img.shape[0]
n_cols = img.shape[1]
          
#segments greyscale images
def segIMG(matrix, iterations):
 count = iterations
 for rows in range(n_rows):
     for cols in range(n_cols):
        t1,t2,t3,t4,t5,t6, maxInt = 50, 80 , 115, 150, 200 , 220, 256
        
        if img[rows,cols] < t1:
            img[rows,cols] = t1/2
            t1 = t1/2
            
        if img[rows,cols] > t1 and img[rows,cols] < t2:
            img[rows,cols] = t2/2
            t2 =t1
            
        if img[rows,cols] > t2 and img[rows,cols] < t3:
            img[rows,cols] = t3/2
            t3 = t2
        if img[rows,cols] > t3 and img[rows,cols] < t4:
            img[rows,cols] = t4/2
            t4 = t3
        if img[rows,cols] > t4 and img[rows,cols] <t5:
            img[rows,cols] =t5/2 
            t5 = t4
        if img[rows,cols] > t5 and img[rows,cols] <t6:
            img[rows,cols] = t6/2
            t6 = t5
        if img[rows,cols] > t6 and img[rows,cols] <maxInt:
            img[rows,cols] = maxInt /2 
            maxInt = t6   
def segIMG2(matrix, iterations):
 count = iterations
 for rows in range(n_rows):
     for cols in range(n_cols):

        if img[rows,cols] <= 80:
            img[rows,cols] = 20

        if img[rows,cols] >80 and img[rows,cols] < 115:
            img[rows,cols] = 90
           
        if img[rows,cols] >= 115 and img[rows,cols] < 150:
            img[rows,cols] = 120
          
        if img[rows,cols] >= 150 and img[rows,cols] < 200:
            img[rows,cols] = 170
            
        if img[rows,cols] > 200 and img[rows,cols] <220:
            img[rows,cols] =210
def segIMG3(matrix, iterations):
 count = iterations
 for rows in range(n_rows):
     for cols in range(n_cols):

        if img[rows,cols] <= 20:
            img[rows,cols] = 0

        if img[rows,cols] >21 and img[rows,cols] < 90:
            img[rows,cols] = 90
           
        if img[rows,cols] >= 115 and img[rows,cols] < 150:
            img[rows,cols] = 120
          
        if img[rows,cols] >= 120 and img[rows,cols] < 170:
            img[rows,cols] = 130
            
        if img[rows,cols] > 170 and img[rows,cols] <210:
            img[rows,cols] =190  
def segIMG4(matrix, iterations):
 count = iterations
 for rows in range(n_rows):
     for cols in range(n_cols):

        if img[rows,cols] >=0 and img[rows,cols] < 90:
            img[rows,cols] = 20
           
        if img[rows,cols] >= 91 and img[rows,cols] < 120:
            img[rows,cols] = 50
          
        if img[rows,cols] >= 121 and img[rows,cols] < 130:
            img[rows,cols] = 80
            
        if img[rows,cols] > 130 and img[rows,cols] <210:
            img[rows,cols] =195
        if img[rows,cols] > 210:
            img[rows,cols] = 3000   
def intDif(img):
     for x in range(n_rows-1):
        for y in range(n_cols-1): 

            if img[x,y] <= 50:
                img[x,y] =   img[x/6,y/4] /6
            if img[x,y]> 50and  img[x,y] <= 90:
                img[x,y] =   img[x/2,y/6] /6   
            if img[x,y] > 90 and img[x,y] <= 120:
                img[x,y] = img[x/2,y/20]
                
                
     




def border(re2dg):
 for x in range(n_rows-1):
    for y in range(n_cols-1):
      
        if img[x,y] - img[x+1,y]  >= 240 and  img[x,y] - img[x+1,y] < 255:
               #print img[x,y] - img[x+1,y] 
           img[x,y] = 255
           img[x+1,y]  = 255
           img[x+1,y+1] = 255
           img[x,y+1] = 255
         
        if img[x,y] >= 180 and img[x+1,y] < 50:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               img[x+1,y]  = 255
               img[x+1,y+1] = 255
               img[x,y+1] = 255
        if img[x,y] <= 230 and img[x+1,y] > 240:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               img[x+1,y]  = 255
               img[x+1,y+1] = 255
               img[x,y+1] = 255
               
        if img[x,y] < 150 and img[x+1,y] > 180:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               img[x+1,y]  = 255
               img[x+1,y+1] = 255
               img[x,y+1] = 255
        if img[x,y] < 10 and img[x+1,y] > 230:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               img[x+1,y]  = 255
               img[x+1,y+1] = 255
               img[x,y+1] = 255

arr = img
#kernel = np.array([[1,2,3,4,2,3,4],
#                [5,6,7,8,4,5,3]])  
                
rws = arr.shape[0]
cls = arr.shape[1]

def combineVal(img):
 for x in range(rws-1):
    for y in range(cls-1):
        center,down = arr[x,y], arr[x+1,y]
        if center > down:
            arr[x+1,y] = center
        if down > center:
            arr[x,y] =arr[x+1,y]
def avgVal(img,distance):      
 for x in range(rws-distance):
    for y in range(cls-distance):
        center,down,right,diag = arr[x,y], arr[x+distance,y], arr[x,y+distance], arr[x+distance,y+distance]
        if right  <= center:
            if diag <= center:
                if down <= center:
                    avg = (center + down + diag + right )/distance
                    arr[x,y] = avg
                    arr[x+1,y] = avg
                    arr[x,y+1] = avg
                    arr[x+1,y+1] = avg

 
  
def triangleBound(img):      
 for x in range(rws-1):
    for y in range(cls-1):
        center,down,right,diag = arr[x,y], arr[x+1,y], arr[x,y+1], arr[x+1,y+1]
        if right  > center:
            if right > down:
                if right > diag:
                    arr[x,y] = right
                    arr[x+1,y] = right
                    arr[x,y+1] = right
                    arr[x+1,y+1] = right
        if center  > right:
            if center > down:
                if center > diag:
                    arr[x,y] = center
                    arr[x+1,y] = center
                    arr[x,y+1] = center
                    arr[x+1,y+1] = center
        if down  > center:
            if down > right:
                if down > diag:
                    arr[x,y] = down
                    arr[x+1,y] = down
                    arr[x,y+1] = down
                    arr[x+1,y+1] = down
        if diag  > center:
            if diag > down:
                if diag > right:
                    arr[x,y] = diag
                    arr[x+1,y] = diag
                    arr[x,y+1] = diag
                    arr[x+1,y+1] = diag
kernel = np.array([[1,0,1],
                   [0,1,0],
                   [1,0,1]])
kw = kernel.shape[0]
kh = kernel.shape[1]  
def Convo(img,kernel):
    
    for y in range(rws-1):
        for x in range(cls-1):
            for ky in range(kw-1):
                for kx in range(kh-1):
                    k0 = kernel[kx,ky]
                    k1 = kernel[kx+1,ky]
                    k2 = kernel[kx+1,ky+1]
                    k3 = kernel[kx-1,ky]
                    k4 = kernel[kx-1,ky-1]
                    k5 = kernel[kx-1,ky+1]
                    k6 = kernel[kx+1,ky-1]
                    k7 = kernel[kx,ky-1]
                    k8 = kernel[kx,ky+1] 
                    
                    img[x,y] = img[x,y]*k5 + img[x+1,y]*k6 + img[x+1,y+1]*k7 + img[x-1,y]*k8 + img[x-1,y-1]*k0 + img[x-1,y+1]*k1 + img[x+1,y-1]*k2 + img[x,y-1]*k3 + img[x,y+1]*k4
Convo(img,kernel)               
cv2.imshow("sdf",img)
                  
            
                
               
                
        