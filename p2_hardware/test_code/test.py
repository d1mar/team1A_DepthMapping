import freenect
import cv2
import frame_convert2
import csv
import math
import numpy as np

import plotly.offline as py
from plotly import graph_objs as go
#to install plotly run 
    #sudo pip install plotly

#importing functions from other py files
from vid_depth import display, snapshot
from filter_scaling import filt_scale

def plot(filtered_depth):
	#plotting 2d scatter plot
	x, y, z = filtered_depth[:, 0], filtered_depth[:, 1], filtered_depth[:, 2]
	plots = [go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=2), connectgaps=False)]
	file_name = 'Scatter_filtered_depth' #the name of your file
	py.plot(plots,filename=file_name,auto_open=True)

def plot(filtered_depth):
	#ploting heat map
	x, y, z = filtered_depth[:, 0], filtered_depth[:, 1], filtered_depth[:, 2]
	plots = [go.Heatmap(x=x, y=y, z=z)]
	file_name = 'Heatmap_filtered_depth' #the name of your file
	py.plot(plots,filename=file_name,auto_open=True)

def main():
	#displaying realtime video/depth feed
	#display()
	
#might automate this process so that when we upload to LED cube
	#taking picure and saving jpg of video and depth, as csv file of depth 
	#every time snapshot is ran it alters same files writing over them 
	snapshot()
	#filtering and scaling
	filt_array = filt_scale()

	plot(filt_array)
	plot_heatmap(filt_array)