#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 10:16:22 2018

@author: bhargav
"""

import cv2
import numpy as np

def lk_optic_flow(img1,img2,smoothing_kernel=3,flow_window=3):
    #img1-image at time instant t1
    #img2 image at time instant 2
    #smoothing kernel-gaussian 
    #flow window- numer of pixels assumed to have the same optical flow
    #assumptions in optical flow:
    #1)pixel intensities do not change between successive frames
    #2)Neighbouring pixels have similar motion
    grad_x=cv2.Sobel(img1,cv2.CV_16F,1,0,ksize=smoothing_kernel)
    grad_y=cv2.Sobel(img1,cv2.CV_16F,0,1,ksize=smoothing_kernel)
    grad_t=cv2.subtract(img2,img1).astype(np.float32)
    #Prepare for inversion
    grad_xx=grad_x**2
    grad_yy=grad_y**2
    grad_xt=grad_x*grad_t
    grad_yt=grad_y*grad_t
    grad_xy=grad_x*grad_y
    #gradient accumulations for each pixel
    #filter 
    Ixx=cv2.boxFilter(grad_xx,-1,ksize=flow_window,normalize=True)
    Iyy=cv2.boxFilter(grad_yy,-1,kize=flow_window,normalize=True)
    Ixy=cv2.boxFilter(grad_xy,-1,ksize=flow_window,normalize=True)
    Ixt=cv2.boxFilter(grad_xt,-1,ksize=flow_window,normalize=True)
    Iyt=cv2.boxFilter(grad_yt,-1,ksize=flow_window,normalize=True)
    ##Displacement matrixes
    #System running out of memory
    #delete unwanted variables
    del grad_xx,grad_yy,grad_xt,grad_yt,grad_xy,grad_x,grad_y,grad_t
    #compute flow for each pixel
    rows,columns=img1.shape
    lk_flow=np.zeros((rows,columns,2),dtype=np.float32)
    
    for r in rows:
        for c in columns:
            b=np.array([Ixt[r,c],Iyt[r,c]],dtype=np.float32).shape(2,1)
            a=np.array([Ixx[r,c],Ixy[r,c],Ixy[r,c],Iyy[r,c]]).reshape(2,2)
            lk_flow[r,c,:]=np.linalg.lstsq(a,b)[0]
    return lk_flow