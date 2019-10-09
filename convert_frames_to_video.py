"""
This script converts frames to a video using OpenCV. The video is saved in 
another folder. The frames per second can be customized according to user requirements. 
    
Reference:
    https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
    https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html
    https://www.geeksforgeeks.org/python-create-video-using-multiple-images-using-opencv/
"""


import cv2
import glob

source = r"C:/Users/Desktop/frames"

destination = r"C:/Users/Desktop/Timelapse.mp4"

frames_per_second = 25
mean_frame_height = 0
mean_frame_width = 0

frames = [cv2.imread(frame) for frame in glob.glob(source + "/*.png")]
total_frames = len(frames)

for frame in frames: 
    frame_height, frame_width, channel = frame.shape
    mean_frame_height += frame_height 
    mean_frame_width += frame_width
    
mean_frame_height = int(mean_frame_height / total_frames)
mean_frame_width = int(mean_frame_width / total_frames) 

resized_frames = [cv2.resize(frame, (mean_frame_width, mean_frame_height), interpolation = cv2.INTER_AREA) for frame in frames]

video = cv2.VideoWriter(destination, cv2.VideoWriter_fourcc(*'DIVX'), frames_per_second, (mean_frame_width, mean_frame_height))

for frame in resized_frames:
    video.write(frame)
    
video.release()
