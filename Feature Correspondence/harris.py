#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 16:22:50 2018

@author: bhargav
"""

import cv2
import numpy as np


def harris_value(img,window=3,kernel=3,alpha=0.04):
    #Compute gradient in x and y directions
    grad_x=cv2.Sobel(img,cv2.CV_64F,1,0,kernel)
    grad_y=cv2.Sobel(img,cv2.CV_64F,0,1,kernel)
    #Compute gradient direction
    grad_mag=np.sqrt(grad_x**2+grad_y**2)
    #gradient direction
    grad_dir=np.arctan(grad_y,grad_x)
    #second order gradients
    grad_xx=grad_x**2
    grad_xy=grad_x*grad_y
    grad_yy=grad_y**2
    #Kernel Uniform filter
    kernel=np.ones((window,window),np.float32)/(window**2)
    harris_scores=np.zeros(img.shape,dtype=np.float32)
    
    #loop through each pixel
    for index_x in range(window//2,img.shape[0]-window//2):
        left_x=max(0,index_x-window//2)
        right_x=min(img.shape[0],left_x+window)
        for index_y in range(window//2,img.shape[1]-window//2):
            left_y=max(0,index_y-window//2)
            right_y=min(img.shape[1],left_y+window)
            Ixx_current=grad_xx[left_x:right_x,left_y:right_y]
            Iyy_current=grad_yy[left_x:right_x,left_y:right_y]
            Ixy_current=grad_xy[left_x:right_x,left_y:right_y]
            M11=(kernel*Ixx_current).sum()
            M12=(kernel*Ixy_current).sum()
            M21=(kernel*Ixy_current).sum()
            M22=(kernel*Iyy_current).sum()
            harris_matrix=np.reshape(np.array([M11,M12,M21,M22]),[2,2])
            harris_val=np.linalg.det(harris_matrix)-alpha*harris_matrix.trace()**2
            harris_scores[index_x,index_y]=harris_val
            return harris_scores
            
def harris_corners(img,window,kernel,alpha,threshold,supress_size):
    if len(img.shape)>2:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    scores=harris_value(img,window,kernel,alpha)
    #Thresholding
    scores=scores*(scores>(threshold*scores.max()))
    #Non maximal surpression
    final_scores=np.zeros(scores.shape,dtype=np.float32)
    r,c=np.nonzero(scores)
    for row,column in zip(r,c):
        min_row=max(0,row-supress_size//2)
        max_row=min(img.shape[0],min_row+supress_size)
        min_column=max(0,column-supress_size//2)
        max_column=min(img.shape[1],min_column+supress_size)
        if scores[row,column]==max(scores[min_row:max_row,min_column:max_column]):
            final_scores[row,column]=scores[row,column]
    return(final_scores)