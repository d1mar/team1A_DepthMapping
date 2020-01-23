import freenect
import cv2
import frame_convert2
import csv

def get_depth():
    frame = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    #cv2.imwrite('depthcapture.jpg', frame)
    print('\nframeDepth =\n')
    print(frame)
    return frame

def get_video():
    frame = frame_convert2.video_cv(freenect.sync_get_video()[0])
    #cv2.imwrite('vidcapture.jpg', frame)
    print('\nframeVideo =\n')
    print(frame)
    return frame
#def image_data():
    

#while 1:
    #display depth
    #cv2.imshow('Depth', get_depth())
    #display video
    #cv2.imshow('Video', get_video())
    #if cv2.waitKey(10) == 27:
       # break
depth_frame = get_depth()
video_frame = get_video()
#saving depth and video as jpg
cv2.imwrite('vidcapture.jpg',video_frame)
cv2.imwrite('depthcapture.jpg',depth_frame)
#saving depth and video as csv

#image_data('depthcapture.csv',get_depth)
#image_data('vidcapture.csv',get_video)
