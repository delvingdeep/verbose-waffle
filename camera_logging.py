"""
This python utiltiy extracts reads video feed from webcam
and writes the individual frame to the local system

Code is self explanatory.

Author: Deep Doshi
"""


# import libraries
import csv
import cv2
import pandas as pd

# output image directory
output_test = "path_to_directory"

count = 0  # variable to count frames for logging

# dimensions to crop the image frame
y1=0
x1=0
y2=500  
x2=500  

# read video feed from any USB camera
feed = cv2.VideoCapture(0)      # 0 denotes in-built Webcam

if not feed.isOpened():
    raise IOError("Webcam cannot be opened")

while True:
    
    # Extract frames
    ret, frame = cv2.read()
    
    # show run-time video feed on console
    cv2.imshow("input", frame)
    
    # crop image to user-defined size
    cropped_image = frame[y1:y2,x1:x2]
    
    # write frame to the local system
    cv2.imwrite(output + "/%#05d.jpg" % (count+1), cropped_image)
    
    # get path of the saved frame
    path = output + "/%#05d.jpg" % (count+1)
    
    count = count + 1
    
    # get time from system time for each frame logging
    hour = pd.datetime.now().hour
    minute = pd.datetime.now().minute
    second = pd.datetime.now().second
    millisecond = int(pd.datetime.now().microsecond / 1000)
    
    time_ms = str(hour) + ":" + str(minute) + ":" + str(second) + ":" + str(millisecond)
    
    # csv write
    data = [path, time_ms]
    
    with open(r'camera_log.csv','a') as wrt:
        writer = csv.writer(wrt)
        writer.writerow(data)
    
    # exit video feed on ESC keystroke
    e = cv2.waitKey(1)
    if e == 27:
        break

# release the feed        
feed.release()

cv2.destroyAllWindows
