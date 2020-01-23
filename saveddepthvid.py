import freenect
import cv2
import frame_convert2

def get_depth():
    frame = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    cv2.imwrite('depthcapture.jpg', frame)
    print('frameDepth = [%d]\n' % (frame))
    return frame

def get_video():
    frame = frame_convert2.video_cv(freenect.sync_get_video()[0])
    cv2.imwrite('vidcapture.jpg', frame)
    print('frameVideo = [%d]\n' % (frame))
    return frame

while 1:
    cv2.imshow('Depth', get_depth())
    cv2.imshow('Video', get_video())
    if cv2.waitKey(10) == 27:
        break
