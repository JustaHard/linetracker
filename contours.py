import cv2 as cv
import numpy as np

vid = cv.VideoCapture(0)
while(vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        thresh = 127
        frame_bin = cv.threshold(gray_frame, thresh, 255, cv.THRESH_BINARY)[1]
        contours, hierarchy = cv.findContours(frame_bin, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        black = np.zeros_like(frame)
        contour = cv.drawContours(black, contours, -1, (0,255,0), 2)
        #black = np.zeros_like(frame)
        # frame_bin[gray_frame>thresh] = 255
        cv.imshow("aboba", contour)
        k = cv.waitKey(20)
        if (k == 113):
            break
    else:
        break
print (frame.shape)
vid.release()
cv.destroyAllWindows()