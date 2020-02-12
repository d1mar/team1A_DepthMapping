import serial
import time
import io
#importing test.py which performs all computations
import test

ser = serial.Serial(
	port = '/dev/serial0',
	baudrate = 115200,
	bytesize = serial.EIGHTBITS,
	timeout = 0)

#running main in test.py will return filtered array
str_list2 = test.main()
str_list = [(0,0,0), (1,1,1), (2,2,2), (3,3,3), (4,4,4), (5,5,5), (6,6,6), (7,7,7), (8,8,8), (9,9,9)]


'''
The following line of code send every element of str_list
via serial port
'''
for i in str_list:
	for j in i:
		#t = str(j) + '\0'
		t = str.encode(str(j))
		ser.write(t)


t = str.encode('\0')
ser.write(t)

ser.close()
