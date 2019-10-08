"""
This script crops images from a folder. The edited image can be viewed during 
the run-time and saved in another folder with the same image name using OpenCV. 

Syntax to crop an image:
    
    image[height_start : height_end, width_start : width_end]
    
Dimension of the image used here is 1024 * 500
"""


import os
import cv2
import glob


source = r"C:/Users/Desktop/source"

destination = r"C:/Users/Desktop/destination"


def main():
    
    for files in glob.glob(source + "/*.png"):
        
        filename, file_extension = os.path.splitext(files)
        image_name = os.path.join(destination, os.path.basename(filename) + '.png')
        
        BGR_image = cv2.imread(files)
        RGB_image = cv2.cvtColor(BGR_image, cv2.COLOR_RGB2BGR)
        
        image = RGB_image[140:410, 50:1000].copy()   
                   
        cv2.imwrite(image_name, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        cv2.imshow('Image', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        # cv2.waitKey(0)
        
        
if __name__ == '__main__':
    main()
