#!/usr/bin/env python
import freenect
import cv2
import frame_convert2

#cv2.namedWindow('Depth')
#cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    frame = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    return frame 

def get_video():
    frame = frame_convert2.video_cv(freenect.sync_get_video()[0])
    #cv2.imwrite('video_frame.jpg', frame)
    return frame

while 1:
    cv2.imshow('Depth', get_depth())
    cv2.imshow('Video', get_video())
    if cv2.waitKey(10) == 27:
        break
