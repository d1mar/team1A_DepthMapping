import freenect
import cv2
import frame_convert2
import csv

#function to get depth as csv file, 11 bit
def get_depth_11bit():
    #saving as 11 bit for csv file 
    frame = freenect.sync_get_depth()[0]
    return frame

#function to get depth as jpg
def get_depth():
    #good for displaying and saving depth image
    frame = frame_convert2.pretty_depth_cv(freenect.sync_get_depth()[0])
    return frame

#live feed of video and depth
def display():
    while 1:
        #display depth
        cv2.imshow('Depth', get_depth())
        #display video
        cv2.imshow('Video', get_video())
        if cv2.waitKey(10) == 27:
            break

#function to get video as jpg
def get_video():
    frame = frame_convert2.video_cv(freenect.sync_get_video()[0])
    return frame

#will save depth as an 11bit csv file
def save_csv(depth_frame_11bit):
    with open('depthcapture.csv', 'w+') as csv_file:
        file_writer = csv.writer(csv_file, delimiter = ',')
        for i in range(len(depth_frame_11bit)):
            file_writer.writerow(depth_frame_11bit[i])

def snapshot():
    #loading vid and depth instance
    depth_frame = get_depth()
    depth_frame_11bit = get_depth_11bit()
    video_frame = get_video()
    #saving depth and video as jpg
    cv2.imwrite('vidcapture.jpg',video_frame)
    cv2.imwrite('depthcapture.jpg',depth_frame)
    #at every snapshot iteration also saving depth as csv file
    save_csv(depth_frame_11bit)                #not sure if you can pass argument like this if not then save snapshot and csv file concurrently in one function.
