from Tkinter import *
import base64
import urllib

import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
from scipy import ndimage


img = cv2.imread("e.jpg",0)       
img2 = cv2.imread("e.jpg",0)

#img3 = cv2.resize(img3,(350,250))
n_rows = img.shape[0]
n_cols = img.shape[1]
#n_colrs = img.shape[2]

 
          

            #grab random intesity region         
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
          
           
         
        if img[x,y] >= 180 and img[x+1,y] < 50:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
              
               
        if img[x,y] <= 230 and img[x+1,y] > 240:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
              
               
               
        if img[x,y] < 150 and img[x+1,y] > 180:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               
               
        if img[x,y] < 10 and img[x+1,y] > 230:
               #print img[x,y] - img[x+1,y] 
               img[x,y] = 255
               
               
def soblex(img,p,n,z):
    for x in range(n_rows-1):
        for y in range(n_cols-1):
            #define points in the image to set a center pixel to
            #x,y center x-1,y left x+1,y right x,y+1 up x,y-1 down.. so on
            # n represents the factor the pixel is multipled by
            
            up = img[x,y+1]*z
            down = img[x,y-1]*z
            center = img[x,y]*z
            left = img[x-1,y]*(2*n)
            right = img[x+1,y]*(p*2)
            topleft = img[x-1,y+1]*p
            topright  = img[x+1,y+1]*p
            bottomleft = img[x-1,y-1]*n
            bottomright = img[x+1,y-1]*p
            
            newCenter = (center + up + down + left + right + bottomleft + bottomright + topleft + topright )
            
            img[x,y] = newCenter
def sobley(img,p,n,z):
    for x in range(n_rows-1):
        for y in range(n_cols-1):
            #define points in the image to set a center pixel to
            #x,y center x-1,y left x+1,y right x,y+1 up x,y-1 down.. so on
            # n represents the factor the pixel is multipled by
            center = img[x,y]*z
            left = img[x-1,y]*z
            right = img[x+1,y]*z
            
            down = img[x,y-1]*n
            bottomleft = img[x-1,y-1]*(2*n)
            bottomright = img[x+1,y-1]*n
            
            up = img[x,y+1]*(2*p)
            topleft = img[x-1,y+1]*p
            topright  = img[x+1,y+1]*p
            
            
            newCenter = (center + up + down + left + right + bottomleft + bottomright + topleft + topright )
            
            img[x,y] = newCenter
def MSS3x(img,n,p,z): 
     for x in range(n_rows-1):
        for y in range(n_cols-1):
            
            #get the blue green red values in an area of 3x3
            #blue blow
            bc = img[x,y,0]   *z  
            bl = img[x-1,y,0] *2*n
            br = img[x+1,y,0]*2*p
            
            bur = img[x+1,y+1,0]*p
            bul = img[x-1,y-1,0]*p
            bup = img[x,y+1,0]*z
            
            bdr = img[x+1,y-1,0]*p
            bdl = img[x-1,y-1,0]*n
            bdown = img[x,y-1,0]*z
            
            
            #greeen blow
            gc = img[x,y,1]   *z  
            gl = img[x-1,y,1] *2*n
            gr = img[x+1,y,1]*2*p
            
            gur = img[x+1,y+1,1]*p
            gul = img[x-1,y-1,1]*p
            gup = img[x,y+1,1]*z
            
            gdr = img[x+1,y-1,1]*p
            gdl = img[x-1,y-1,1]*n
            gdown = img[x,y-1,1]*z
            
           
            #red blow
            rc = img[x,y,2]   *z  
            rl = img[x-1,y,2] *2*n
            rr = img[x+1,y,2]*2*p
            
            rur = img[x+1,y+1,2]*p
            rul = img[x-1,y-1,2]*p
            rup = img[x,y+1,2]*z
            
            rdr = img[x+1,y-1,2]*p
            rdl = img[x-1,y-1,2]*n
            rdown = img[x,y-1,2]*z
            
            
            #total values from the 3x3 section
            bTotal = bc+bdl+bdown+bdr+bl+br+bul+bup+bur/9
            rTotal = rc+rdl+rdown+rdr+rl+rr+rul+rup+rur/9
            gTotal = gc+gdl+gdown+gdr+gl+gr+gul+gup+gur/9
            #set center pixel to the totals
            img[x,y] = (bTotal,gTotal,rTotal)
            img[x,y+1] = (bTotal,gTotal,rTotal)
            img[x,y-1] = (bTotal,gTotal,rTotal)
            img[x-1,y] = (bTotal,gTotal,rTotal)
            img[x+1,y] = (bTotal,gTotal,rTotal)
            img[x,y-1] = (bTotal,gTotal,rTotal)
            img[x,y+1] = (bTotal,gTotal,rTotal)
            img[x-1,y-1] = (bTotal,gTotal,rTotal)
                        
          
def MSS3y(img,n,p,z): 
     for x in range(n_rows-1):
        for y in range(n_cols-1):
            
            #get the blue green red values in an area of 3x3
            #blue blow
            bc = img[x,y,0]   *z  
            bl = img[x-1,y,0] *z
            br = img[x+1,y,0]*z
            
            bur = img[x+1,y+1,0]*n
            bul = img[x-1,y-1,0]*2*n
            bup = img[x,y+1,0]*n
            
            bdr = img[x+1,y-1,0]*p
            bdl = img[x-1,y-1,0]*p
            bdown = img[x,y-1,0]*p
            
            
            #greeen blow
            gc = img[x,y,1]*z 
            gl = img[x-1,y,1]*z 
            gr = img[x+1,y,1]*z 
            
            gur = img[x+1,y+1,1]*n
            gul = img[x-1,y-1,1]*2*n
            gup = img[x,y+1,1]*n
            
            gdr = img[x+1,y-1,1]*p
            gdl = img[x-1,y-1,1]*p
            gdown = img[x,y-1,1]*p
            #red blow
            rc = img[x,y,2]*z
            rl = img[x-1,y,2]*z
            rr = img[x+1,y,2]*z
            
            rur = img[x+1,y+1,2]*n
            rul = img[x-1,y-1,2]*2*n
            rup = img[x,y+1,2]*n
            
            rdr = img[x+1,y-1,2]*p
            rdl = img[x-1,y-1,2]*p
            rdown = img[x,y-1,2]*p
            #total values from the 3x3 section
            bTotal = bc+bdl+bdown+bdr+bl+br+bul+bup+bur
            rTotal = rc+rdl+rdown+rdr+rl+rr+rul+rup+rur
            gTotal = gc+gdl+gdown+gdr+gl+gr+gul+gup+gur
            #set center pixel to the totals
            img[x,y] = (bTotal,gTotal,rTotal)
            img[x,y+1] = (bTotal,gTotal,rTotal)
            img[x,y-1] = (bTotal,gTotal,rTotal)
            img[x-1,y] = (bTotal,gTotal,rTotal)
            img[x+1,y] = (bTotal,gTotal,rTotal)
            img[x,y-1] = (bTotal,gTotal,rTotal)
            img[x,y+1] = (bTotal,gTotal,rTotal)
            img[x-1,y-1] = (bTotal,gTotal,rTotal)

            
            
          

            
            #set the kernel values to be multiplied by small values
def avgSegColorIMG(img):
 for x in range(n_rows):
     for y in range(n_cols):
         for z in range(n_colrs):
            if img[x,y,z] <= 25 :
                #determine main color
                    img[x,y,z] = 25
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
                     
                               
def corners(img,l,c,r):
    for x in range(n_rows-1):
        for y in range(n_cols-1):
            #[leftbgr,centerbgr,rightbgr]
            #[ -1/2         0        1/2
            
            bc = img[x,y,0]   
            bl = img[x-1,y,0] 
            br = img[x+1,y,0]
           
            gc = img[x,y,1]   
            gl = img[x-1,y,1] 
            gr = img[x+1,y,1]

            rc = img[x,y,2]   
            rl = img[x-1,y,2] 
            rr = img[x+1,y,2]
            
            center = (bc + rc + gc) *l
            left =   (bl + rl + gl)  *c
            right =  (br + gr + rr)  *r
            val = (center ,left , right)
            img[x,y]= val
            img[x+1,y+1]= val
            img[x-1,y-1]= val
            img[x+1,y-1]= val
            img[x-1,y+1]= val
def bwCorner(img):
    for x in range(n_rows-1):
        for y in range(n_cols-1):
                
                center =img[x,y]*-.2
                right = img[x-1,y]*.2
                totVal = center + right
                if totVal != 0:
                    img[x,y] = totVal
                    img[x+1,y] =totVal
                    img[x-1,y] =totVal
                else:
                    img[x,y] = -85
                
def fourValue(img):
    for x in range(n_rows-1):
        for y in range(n_cols-1):
                
                #  x    idea
                #  1|2
                #  ---
                #  3|4
                #check pixel difference and set all pixels to 
                #value if they ly in a close range
                
                one =img[x,y]
                two = img[x+1,y]
                three = img[x,y-1]
                four = img[x+1,y-1]
                
                val12 = one - two
                val13 = one - three
                val14 = one - four
                
                img[x,y] = val14
                img[x+1,y] = val14
                img[x+1,y-1]= val14
                img[x,y-1] = val14
                
                
                                
                
#arr = np.array([[1,2,3,1,2,3],
#                [2,3,4,5,6,7]])              
arr = img                
cls = arr.shape[0]
rws = arr.shape[1]            

for x in range(cls-1):
    for y in range(rws-1):
       # print arr[x,y], arr[x+1,y]
        if arr[x,y] >50:
            arr[x,y] = 30
        
       
          
            

            
           

#fourValue(img)

#.16 is highest for mss3x
#MSS3x(img,.14,.14,0)
#avgSegColorIMG(img)


cv2.imshow("img",img)
#.05 -.6 highest for mss3y     
#MSS3y(img,.11,.11,0)     


                  
            
                
               
                
        