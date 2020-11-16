from __future__ import print_function
import cv2 as cv



backSub_knn = cv.createBackgroundSubtractorKNN()
backSub_mog2 = cv.createBackgroundSubtractorMOG2()

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read() 

    
    fgMask_knn = backSub_knn.apply(frame)
    fgMask_mog2 = backSub_mog2.apply(frame)
    
    cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
    cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
    cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    
    cv.imshow('Frame', frame)
    cv.imshow('FG Mask knn', fgMask_knn)
    cv.imshow('FG Mask mog2', fgMask_mog2)

    
    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break