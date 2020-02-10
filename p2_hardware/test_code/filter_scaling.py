import math
import numpy as np



#converting distance to raw values
def conversion(x):
    x *= 0.3048000097536
    raw = 2842.5*(math.atan(x/0.1236) - 1.1863)
    return raw

#normalizing array for cube display
def norm(cube, minimum, max_rage, arr):
	arr = ((arr - minimum)*( cube -1))/max_range
	return arr

#main filtering algorithm
def filt_scale():
	depth_data = []
	temp = np.loadtxt('depthcapture.csv',delimiter=',')
	depth_data = temp.astype(int)
	depth_data = np.asarray(depth_data)
	raw_depth_data = np.copy(depth_data)

	#upper and lower depth bounds in feet
	ft_lo_depth = 1.5
	ft_u_depth = 3
	#converting value to integer (do not want decimal) and printing to check value
	lo_depth = conversion(ft_lo_depth)
	u_depth = conversion(ft_u_depth)

	
	#making depth_data into a 1D array
	depth_data = depth_data.flatten()
	
	#function prints x,y cordinate pairs of valid values
	#don't have to flatten array this way can use raw_depth_data
	cordinates2 = list(zip(*np.where((raw_depth_data>lo_depth) & (raw_depth_data<u_depth))))

	#filtering depth_data between lo and u depth values
	#will keep original values satisfying condition and zero out the rest
	depth_data = np.where((depth_data>lo_depth) & (depth_data<u_depth),depth_data,0)
	#deleting all occurences of 0 in filtered array
	depth_data = depth_data[depth_data != 0]

	#seperating x,y,z coordinates
	x,y = zip(*cordinates2)
	x_arr = x                  # All the x-values (from 0 to 639) where depth_data fits the depth bounds
	y_arr = y                  # All the y-values (from 0 to 479) where depth_data fits the depth bounds
	z_arr = depth_data    # All the z or depth values (11-bit) where depth_data fits the depth bounds

	r = max(x_arr)
	le = min(x_arr)
	u = min(y_arr)
	lo = max(y_arr)
	b = max(z_arr)
	f = min(z_arr)

	x_range = r - le  # potential legnth of cube
	y_range = lo - u  # potential length of cube
	z_range = u_depth - lo_depth

	max_range = max(x_range,y_range)   	# find the maximum range between x and y.  A square will be formed around the maximum range which our object will be placed in
	x_mid = r - x_range/2    			# calculate the midpoint of the x-axis of the object
	y_mid = lo - y_range/2   	 		# calculate the midpoint of the y-axis of the object

	#when running sometimes get negative value for u. Not sure if correct or should be zero
	# Make an if else statement
	if x_range > y_range:
    	u = y_mid-max_range/2
    	lo = y_mid+max_range/2
	elif x_range < y_range:
    	le = x_mid-max_range/2
    	r = x_mid+max_range/2

    cube_length = 6
	x_arr = np.asarray(x_arr)
	y_arr = np.asarray(y_arr)
	z_arr = np.asarray(z_arr)

	#normalizing
	x_new = norm(cube_length, le, max_range, x_arr)
	y_new = norm(cube_length, u, max_range, y_arr)
	z_new = norm(cube_length, lo_depth, z_range, z_arr)

	#filtered tuple numpy array
	filtered_depth = list(zip(x_new,y_new,z_new))
	filtered_depth = np.array(filtered_depth)

	return filtered_depth