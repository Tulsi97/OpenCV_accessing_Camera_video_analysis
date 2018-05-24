# -*- coding: utf-8 -*-
"""
Created on Wed May 23 23:46:32 2018

@author: hp-u
"""

import cv2
 
def main():
    windowName = "Live Video Feed"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
        
    else:
        ret = False
        
    while ret:
        ret , frame = cap.read()
        
        
        cv2.imshow(windowName,frame)
        if cv2.waitKey(1) == 10:
            break
        
    cv2.destroyAllWindows(windowName)
    cap.release()

if __name__ == "__main__":
    main()
        