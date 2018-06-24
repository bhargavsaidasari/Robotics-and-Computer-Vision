#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 11:03:10 2018

@author: bhargav
"""

import numpy as np
from lk_optic_flow import *
from pyramid_imp import *
import matplotlib.pyplot as plt
import sys

import cv2

def ps5_p1():
    #Compute Optical Flow between successive frames
    frame1=cv2.imread('input/DataSeq1/yos_img_01.jpg',cv2.IMREAD_GRAYSCALE)
    frame2=cv2.imread('input/DataSeq1/yos_img_02.jpg',cv2.IMREAD_GRAYSCALE)
    
def ps5_p2():
    #Compute pyramid representation of 
    image1=cv2.imread('input/DataSeq2/0.png',cv2.IMREAD_GRAYSCALE).astype(np.float32)
    output_gaussian=gaussian_pyramid(image1,3)
    output_laplacian=laplacian_pyramid(image1,3)
    
    #plot gaussian pyramid
    plt.figure(1)
    
    for index,img in enumerate(output_gaussian):
        subplot_index=index+1
        plt.subplot(2,2,subplot_index)
        plt.imshow(img,cmap='gray')
    plt.show()
    #plot the laplacian images
    plt.figure(2)    
    for index,img in enumerate(output_laplacian):
        sublot_index=index+1
        plt.subplot(2,2,sublot_index)
        plt.imshow(img,cmap='gray')
    plt.show()
    
ps5_list={"1":ps5_p1,"2":ps5_p2}
    
if __name__=="__main__":
    if len(sys.argv)==2:
        if(sys.argv[1] in ps5_list):
            print("\n Executing task %s\n"%sys.argv[1])
            ps5_list[sys.argv[1]]()
        else:
            print("Unidentified identifier")
    else:
        for idx in range(len(ps5_list)):
            print("\n Executing task %s\n.................."%list
                  (ps5_list.keys())[idx])
            list(ps5_list.values())[idx]()
            
    
        
    
    