import cv2
import numpy as np

def disparity_ncorr(L, R,block_size=5):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))
    
    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """


    # TODO: Your code here
    rows,columns=L.shape
    d_map=np.zeros(L.shape,dtype=float32)
    
    for r in range(block_size//2,rows-block_size//2):
        min_r=max(0,r-block_size//2)
        max_r=min(rows,r+block_size//2)
        for c in range(block_size//2,columns-block_size//2):
            min_c=max(0,c-block_size//2)
            max_c=min(columns,c+block_size//2)
            template=L[min_r:max_r,min_c:max_c]
            #Choose the strip in the other image
            R_strip=R[min_r:max_r,0:columns]
            #Apply temlate matching
            res=cv2.matchTemplate(R,template,'cv2.TM_CCORR_NORMED')
            [~,~,~,maximum]=cv2.minMaxLoc(res)
            d_map[r,c]=maximum[1]-c
            
     return(d_map)           