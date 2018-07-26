"""
This python utiltiy extracts reads video feed from webcam

Code is self explanatory.

Author: Deep Doshi
"""


# import libraries
import cv2

# read video feed from any USB camera
feed = cv2.VideoCapture(0)      # 0 denotes in-built Webcam

if not feed.isOpened():
    raise IOError("Webcam cannot be opened")

while True:

    ret, frame = cv2.read()
    
    # show run-time video feed on console
    cv2.imshow("input", frame)
    
    # exit video feed on ESC keystroke
    e = cv2.waitKey(1)
    if e == 27:
        break

feed.release()

cv2.destroyAllWindows
