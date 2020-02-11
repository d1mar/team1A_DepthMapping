#importing my python files
import vid_depth
import filter_scaling
#importing plotly
import plotly.offline as py
from plotly import graph_objs as go
import numpy as np

def plot(filtered_depth,name):
    #plotting 2d scatter plot
    filtered_depth = np.array(filtered_depth)
    filtered_depth = filtered_depth.astype(int)
    x,y,z = filtered_depth[:,0], filtered_depth[:,1], filtered_depth[:,2]
    plots = [go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=2), connectgaps=False)]
    file_name = name  #the name of your file
    py.plot(plots,filename=file_name,auto_open=False)

def plot_heatmap(filtered_depth):
    #ploting heat map
    filtered_depth = np.array(filtered_depth)
    filtered_depth = filtered_depth.astype(int)
    x,y,z = filtered_depth[:,0], filtered_depth[:,1], filtered_depth[:,2]
    plots = [go.Heatmap(x=x, y=y, z=z)]
    file_name = 'Heatmap_filtered_depth.html' #the name of your file
    py.plot(plots,filename=file_name,auto_open=False)

def main():
    #displaying realtime video/depth feed
    #vid_depth.display()

#might automate this process so that when we upload to LED cube
    #taking picure and saving jpg of video and depth, as csv file of depth 
    #every time snapshot is ran it alters same files writing over them 
    #vid_depth.snapshot()
    #filtering and scaling
    filt_array, raw_array = filter_scaling.filt_scale()
    #print(filt_array)
    #print(raw_array)
    print('filtering performed')
    #plot(filt_array,'Scatter_filtered_depth.html')
    #plot(raw_array,'Scatter_raw_depth.html')
    #plot_heatmap(filt_array)
    print('ploting performed')

#return used when sender implemented so that sender file has access to filtered array
    return filt_array
#main()
