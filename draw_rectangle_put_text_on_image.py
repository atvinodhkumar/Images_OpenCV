"""
This script draws a rectangle and puts text anywhere on the image using OpenCV. 
The edited image can be viewed during the run-time and saved in the desired location.

Syntax to draw a rectangle on an image:
    cv2.rectangle(image, starting_point_coordinates, ending_point_coordinates, color, thickness)
    cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 0), 5)

Reference:
    https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga07d2f74cadcf8e305e810ce8eed13bc9

Syntax to put a text on an image:
    cv2.putText(image, 'text', coordinates, font, fontScale, color, thickness, lineType) 
    cv2.putText(image, 'text', (xmin, ymin), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2, cv2.LINE_AA)

Reference:
    https://docs.opencv.org/master/d6/d6e/group__imgproc__draw.html#ga5126f47f883d730f633d74f07456c576
    
Dimension of the image used here is 1024 * 500
"""


import os
import cv2


def main():
    
    path = "C:/Users/Desktop/" 
    
    BGR_image = cv2.imread(path + r"python_logo.png")
    RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_RGB2BGR)
    
    RGB_image = cv2.rectangle(RGB_image, (594, 400), (984,460), (255,0,0), 3)
    RGB_image = cv2.putText(RGB_image, 'Enter Text', (604, 450), cv2.FONT_HERSHEY_TRIPLEX, 2, (255,0,0), 2, cv2.LINE_AA)
    
    cv2.imwrite(os.path.join(path, 'python_logo_text.png'), cv2.cvtColor(RGB_image, cv2.COLOR_RGB2BGR))
    cv2.imshow('Image', cv2.cvtColor(RGB_image, cv2.COLOR_RGB2BGR))
    # cv2.waitKey(0)      
    
    
if __name__ == '__main__':
    main()
