import freenect
import cv2
import frame_convert2
import csv

def get_depth():
    #saving as 11 bit for csv file 
    frame = freenect.sync_get_depth()[0]
    #good for displaying and saving depth image
    #frame = frame_convert2._depth_cv(freenect.sync_get_depth()[0])
    #print('\nframeDepth =\n')
    #print(frame)
    return frame

def get_video():
    frame = frame_convert2.video_cv(freenect.sync_get_video()[0])
    #print('\nframeVideo =\n')
    #print(frame)
    return frame  

def main():
    #display image and depth windows in while loop:
#    while 1:
        #display depth
#        cv2.imshow('Depth', get_depth())
        #display video
#        cv2.imshow('Video', get_video())
#        if cv2.waitKey(10) == 27:
#            break

    #once windows are closed last image is captured and saved
    depth_frame = get_depth()
    video_frame = get_video()
    #saving depth and video as jpg
    cv2.imwrite('vidcapture.jpg',video_frame)
    cv2.imwrite('depthcapture.jpg',depth_frame)
    #saving depth and video as csv    
    with open('depthcapture.csv', 'w+') as csv_file:
        file_writer = csv.writer(csv_file, delimiter = ',')
        for i in range(len(depth_frame)):
            file_writer.writerow(depth_frame[i])
    with open('vidcapture.csv', 'w+') as csv_file:
        file_writer = csv.writer(csv_file, delimiter = ',')
        for i in range(len(video_frame)):
            file_writer.writerow(video_frame[i])


main()
print('finished')
