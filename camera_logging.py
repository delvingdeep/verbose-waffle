"""
This python utiltiy extracts reads video feed from webcam
and writes the individual frame to the local system

Code is self explanatory.

Author: Deep Doshi
"""


# import libraries
import cv2

# output image directory
output_video = "path_to_directory"

count = 0  # variable to count frames for logging

# read video feed from any USB camera
feed = cv2.VideoCapture(0)      # 0 denotes in-built Webcam

if not feed.isOpened():
    raise IOError("Webcam cannot be opened")

while True:
    
    # Extract frames
    ret, frame = cv2.read()
    
    # show run-time video feed on console
    cv2.imshow("input", frame)
    
    # write image frame to local system
    cv2.imwrite(output_video + "/%#05d.jpg" % (count+1), frame)
    count = count + 1
    
    # exit video feed on ESC keystroke
    e = cv2.waitKey(1)
    if e == 27:
        break

# release the feed        
feed.release()

cv2.destroyAllWindows
