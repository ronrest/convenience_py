""" PIPELINE FOR USING OPEN CV TO PROCESS VIDEO FILE
    Optionally save to a video output file
"""
from __future__ import print_function, division
import numpy as np
import cv2
import os


################################################################################
#                                                                       SETTINGS
################################################################################
# FILE PATHS
videos_dir = "/path/to/par_dir"
video_name = "video.mp4"
video_path = os.path.join(videos_dir, video_name)

# # FOR SAVING VIDEO
# # file to save output to
# out_video_path = "test.avi"
#
# # taken from: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out_vid_dims = (640, 480)
# out = cv2.VideoWriter(out_video_path,fourcc, 20.0, out_vid_dims)

################################################################################
#                                                            START VIDEO STREAM
################################################################################
cap = cv2.VideoCapture(video_path)
while(cap.isOpened()):
    ret, image = cap.read()
    if ret == True:
        image = cv2.resize(image, (640,  480))
        if image is None:
            print("NO IMAGE!!!!")

        # ---------------------------------
        # MANIPULATIONS
        # ---------------------------------
        # Blurred
        blured = cv2.GaussianBlur(image, (31, 31), 0)

        # grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grayscale
        gray3 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)  # back to 3 chanels

        # Local Contrast - Only works on grayscale images
        clahe = cv2.createCLAHE(clipLimit=30, tileGridSize=(5, 5))
        contrast = clahe.apply(gray)
        contrast = cv2.cvtColor(contrast, cv2.COLOR_GRAY2BGR)  # back to 3 chanels

        # ---------------------------------
        # Stack videos into single frame
        stack = np.hstack((image, blured, gray3, contrast))
        stack = cv2.resize(stack, (320*5,  240))
        cv2.imshow('Stack', stack)

        # SAVE THE FRAME TO VIDEO FILE
        # outvid = cv2.resize(stack, out_vid_dims)
        # out.write(outvid)

        # Quit if Escape button pressed
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
