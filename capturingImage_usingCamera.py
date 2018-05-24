# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:29:10 2018

@author: hp-u
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret,frame = cap.read()
        print(ret)
        print(frame)
        
    else:
        ret = False
        
    img1 = cv2.cvtColor(frame,cv2.COLOR_BGRA2RGB)

    plt.imshow(img1)
    plt.title('Color Image')
    plt.xticks([])
    plt.yticks([])
    
    cap.release()  
    
cv2.waitKey(0)
cv2.destroyAllWindows()     
if __name__ == "__main__":
    main()