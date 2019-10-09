"""
This script extracts frames from a video using OpenCV. The frames are saved in 
another folder with the image naming convention. 

The frame rate (frames per second or FPS) can be customized, it can be either 
the default frame rate of the video or custom frame rate.

default frame rate: It is the orginal frame rate of the video.

custom frame rate: It can change the number of frames taken per second in the video.

Example:
    To get only 20 frames per second, give custom_frame_rate = 0.05 -> (1/20 = 0.05)
    OR
    To get only 25 frames per second, give custom_frame_rate = 0.04 -> (1/25 = 0.04)
    
Reference:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
    https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html
    https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
"""

import os
import cv2


source = r"C:/Users/Desktop/Timelapse.mp4"

destination = r"C:/Users/Desktop/frames"

video = cv2.VideoCapture(source)

frames_per_second = video.get(cv2.CAP_PROP_FPS)

default_frame_rate = 1/round(frames_per_second)
custom_frame_rate = 0.05  # 20 frames per second -> (1/20 = 0.05)

frame_rate = default_frame_rate  # Change the type of frame rate here   

second = 0
count = 1
is_frame = True


while is_frame:
    
    second = round((second + frame_rate), 2)
    video.set(cv2.CAP_PROP_POS_MSEC, second*1000)
    
    is_frame, frame = video.read() 
    
    if is_frame:
        frame_name = "%04d.png" % count  # Save frame as PNG file with image naming convention
        cv2.imwrite(os.path.join(destination,  frame_name), frame)
        count = count + 1
        