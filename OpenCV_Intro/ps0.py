#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 09:46:57 2018

@author: bhargav
"""

import cv2
import numpy as np
import os.path

#Problem 1
img1=cv2.imread('Input/lena.jpg',cv2.IMREAD_COLOR)
cv2.imwrite('Output/ps0-1-a-1.png',img1)
img2=cv2.imread('Input/feral.jpeg',cv2.IMREAD_COLOR)
cv2.imwrite('Output/ps0-1-a-2.jpg',img2)

#problem 2
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

temp=img1[:,:,0]
img1[:,:,0],img1[:,:,2]=img1[:,:,2],temp
cv2.imshow("swapped",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img1_red=img1[:,:,0]
img2_red=img2[:,:,0]

#Problem 3
window_length=100
centre_img1=np.asarray(img1.shape[0:2])//2
sub_image=img1_red[centre_img1[0]-window_length//2:centre_img1[0]+window_length//2,centre_img1[1]-window_length//2
               :centre_img1[1]+window_length//2]

centre_img2=np.asarray(img2.shape[0:2])//2

img2_red[centre_img2[0]-window_length//2:centre_img2[0]+window_length//2,centre_img2[1]-window_length//2
               :centre_img2[1]+window_length//2]=sub_image
cv2.imshow("interchange",img2_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Output/ps0-1-c-1.jpg',img2_red)

#Problem 4

img1_red_diff=cv2.subtract(img1_red,img1_red.mean())
img1_div=cv2.divide(img1_red_diff,img1_red.std())
img1_final=cv2.multiply(img1_div,30)

cv2.imshow('Arithmetic',img1_final)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Output/ps0-1-d-1.jpg',img1_final)


#Problem 5
noise=img1_red.copy()
cv2.randn(noise,0,100)
img1_noisy_red=cv2.add(img1_red,noise)
cv2.imshow('noisy',img1_noisy_red)
cv2.waitKey(0)
cv2.destroyAllWindows()