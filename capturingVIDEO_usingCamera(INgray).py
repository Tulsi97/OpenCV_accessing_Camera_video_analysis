# -*- coding: utf-8 -*-
"""
Created on Thu May 24 00:01:04 2018

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
        
        output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow(windowName,output)
        if cv2.waitKey(1) == 10:
            break
        
    cv2.destroyAllWindows(windowName)
    cap.release()

if __name__ == "__main__":
    main()
        