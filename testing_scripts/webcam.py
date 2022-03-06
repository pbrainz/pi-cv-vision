import numpy as np
import cv2


# List available devices and their IDs
'''
Linux:
run the following command: ls /dev/ | grep video
Will be listed as a video device with and integer such as video0, video1, video2
ex usage: cv2.VideoCapture("/dev/video0")

Windows: 
Will just be an integer such as 0,1,2...
ex usage: cv2.VideoCapture(0)
'''

# point to the device ID of the camera to use
device = "/dev/video0" # this is a USB cam with linux

cap = cv2.VideoCapture(device)
while(True):
    ret, frame = cap.read()
    # make picture gray, for testing simplicity
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow('frame',gray)
    # click on the pop-up camera window and press 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
cap.release()
cv2.destroyAllWindows()