# ps2
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

## 1-a
# Read images
L = cv2.imread(os.path.join('input', 'pair0-L.png'), 0) 
R = cv2.imread(os.path.join('input', 'pair0-R.png'), 0) 

# Compute disparity (using method disparity_ssd defined in disparity_ssd.py)
from disparity_ssd import disparity_ssd
D_L = disparity_ssd(L, R)
cv2.imshow('trail',D_L)
cv2.waitKey(0)
cv2.destroyAllWindows()
D_R = disparity_ssd(R, L)

# TODO: Save output images (D_L as output/ps2-1-a-1.png and D_R as output/ps2-1-a-2.png)
# Note: They may need to be scaled/shifted before saving to show results properly

stereo=cv2.StereoBM_create(numDisparities=20,blockSize=15)
disparity=stereo.compute(L,R)
plt.imshow(disparity,'gray')
plt.show()

# TODO: Rest of your code here
