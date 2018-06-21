#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:24:57 2018

@author: bhargav
"""

from harris import *

import cv2
import os
import sys


images_list=['transA.jpg','transB.jpg','simA.jpg','simB.jpg']


def ps4_1():
    for idx,images in enumerate(images_list):
        img=cv2.imread('input/'+images,cv2.IMREAD_GRAYSCALE)
        Rs=harris_corners(img,window=3,kernel=3,alpha=0.04,threshold=0.02,supress_size=5)
        cv2.imwrite('output/ps4-1'+str(idx)+'.jpg',Rs) 
        print('Finished Harris Corners')
def ps4_2():
    return
 
ps4_list={"1":ps4_1,"2":ps4_2}

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] in ps4_list:
            print('\nExecuting task %s\n=================='%sys.argv[1])
            ps4_list[sys.argv[1]]()
        else:
            print('\nGive argument from list {1,2,3}\
                  for the corresponding task.')
    else:
        print('\n * Executing all tasks: * \n')
        for idx in range(len(ps4_list)):
            print('\nExecuting task: %s\n=================='%
                  list(ps4_list.keys())[idx])
            list(ps4_list.values())[idx]()
