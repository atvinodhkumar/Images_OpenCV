"""
This script resizes images from a folder. The edited image can be viewed during 
the run-time and saved in another folder with the same image name using OpenCV. 

Syntax to resize an image:
      
    cv2.resize(image, None, fx, fy, interpolation) 
     
    fx = scale factor along the horizontal axis
    
    fy = scale factor along the vertical axis

Reference:
    
    https://docs.opencv.org/2.4/modules/imgproc/doc/geometric_transformations.html?highlight=getrotationmatrix2d#resize

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
        
        image = cv2.resize(RGB_image, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)   
        
        cv2.imwrite(image_name, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        cv2.imshow('Image', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        # cv2.waitKey(0)
        
        
if __name__ == '__main__':
    main()
