"""
ECE196 Depth Mapping Project
Author: Will Chen
Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2
import numpy as np
# TODO: Edit this function
def process_image():
    # reading image
    img = cv2.imread('../team1A_DepthMapping/geisel.jpg',0)
    
    # updating image dimensions
    print('original dimensions: ', img.shape)       #printing old dimensions
    scale_factor = 50                               #reducing by 1/2
    width = int(img.shape[1] * scale_factor / 100)
    height = int(img.shape[0] * scale_factor / 100)
    dim = (width, height)
    resize_img = cv2.resize(img, dim)
    print('resized dimensions: ', resize_img.shape) #printing new dimensions
    
    # drawing 100x100 white box
    topCorner = (int(width/2) - 50, int(height/2) + 50)
    bottomCorner = (int(width/2) + 50, int(height/2) - 50)
    cv2.rectangle(resize_img, (topCorner), (bottomCorner), (255,255,255), 3)
    
    # display image
    cv2.imshow('geisel bw, resized', resize_img)

    # saving image
    #status = cv2.imwrite('../team1A_DepthMapping/geisel_bw.jpg', resize_img)
    #print('Image written to file-system: ', status)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
    hello_world()
    process_image()
    return


if(__name__ == '__main__'):
    main()
