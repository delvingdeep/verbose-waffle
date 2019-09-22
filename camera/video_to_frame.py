"""
This python utiltiy extracts frames from the video. 
Code is self explanatory.

Author: Deep Doshi
"""

# import
import time
import cv2
import os

# input video
input_video = "path_to_video_file.extension"

# output image directory
output_video = "path_to_directory"

# Log the time
time_start = time.time()
    
# Start capturing the feed
cap = cv2.VideoCapture(input_video)

# Find the number of frames
video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
print ("Number of frames: ", video_length)
count = 0
print ("Converting video..\n")

# Start converting the video
while cap.isOpened():
    
    # Extract the frame
    ret, frame = cap.read()
        
    # Write result back to output directory
    cv2.imwrite(output_video + "/%#05d.jpg" % (count+1), frame)
    count = count + 1
    
    # If there are no more frames left
    if (count > (video_length-1)):
        # Log the time again
        time_end = time.time()
            
        # Release the feed
        cap.release()
            
        # Print stats
        print ("Done extracting frames.\n%d frames extracted" % count)
        print ("It took %d seconds for conversion." % (time_end-time_start))
        break
