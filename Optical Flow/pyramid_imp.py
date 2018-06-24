#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:19:07 2018

@author: bhargav
"""

import cv2



def reduce(img):
    return cv2.pyrDown(img)

def expand(img):
    return cv2.pyrUp(img)

def gaussian_pyramid(img,num_levels=4):
    #Compute the Gassuian pyramid decomposition of image to the prescribed number of levels
    gpyramid=[img]
    for count in range(num_levels):
        gpyramid.append(reduce(gpyramid[-1]))
    return gpyramid
    
    
    
def laplacian_pyramid(img,num_levels=4):
    #Compute the laplacian pyramid decomposition to the prescribed number of levels in the image
    lpyramid=[img]
    gpyramid_list=[img]
    for count in range(num_levels):
        gpyramid=gaussian_pyramid(gpyramid_list[-1],1)[-1]
        gpyramid=expand(gpyramid)
        row_diff,col_diff=gpyramid.shape[0]-img.shape[0],gpyramid.shape[1]-img.shape[1]
        if row_diff>0:
            gpyramid=gpyramid[0:img.shape[0],:]
            row_diff=0
            
        if col_diff>0:
            gpyramid=gpyramid[:,:img.shape[1]]
            col_diff=0
            
        gpyramid=cv2.copyMakeBorder(gpyramid,0,-row_diff,0,-col_diff,cv2.BORDER_REPLICATE)
        lpyramid.append(gpyramid_list[-1]-gpyramid)
        gpyramid_list.append(gpyramid)
    return lpyramid

    


    
    
