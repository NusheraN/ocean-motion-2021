# script to turn w outputs into netcdf
import os
import numpy as np
import datetime
from netCDF4 import Dataset

num_lat = 158
num_lon = 122
levels = 1
dates = 1356

w_path = '/Users/helenfellow/Documents/cnn_paper/data/atlantic-data/s-omega/w/'

date_list = open('/Users/helenfellow/Documents/cnn_paper/other_peoples_code/run-atlantic-again/date_list-08-18.txt','r')

w_array = np.zeros((dates,num_lat,num_lon,levels))

for d in range(0,dates):
	filename = "s_"+(date_list.readline()).strip('\n')+"_ww.gr"
	print(filename)
	if os.path.isfile(w_path+filename):
		w_file = open(w_path+filename,"r")
		w_file.readline()
		w_file.readline()
		for i in range(0,levels):
			for j in range(0,num_lat):
				for k in range(0,num_lon):
					w = w_file.readline()
					w_array[d,j,k,i] = float(w)
					#print(w)
	

latitude_val = np.arange(12.625+.5,51.875-0.25,0.25)
longitude_val = np.arange(311.875+.5,342.125-0.25,0.25)
time_val = np.arange(377064,604704+168,168)
print(time_val.size)

grp = Dataset('/Users/helenfellow/Documents/cnn_paper/data/atlantic-data/s-atlantic-w-08-18.nc','w', format='NETCDF4')
grp.createDimension('lon', num_lon-4)
grp.createDimension('lat', num_lat-4)
grp.createDimension('depth', levels)
grp.createDimension('time', dates)

longitude = grp.createVariable('longitude', 'f4', 'lon')
latitude = grp.createVariable('latitude', 'f4', 'lat')  
depth = grp.createVariable('depth', 'f4', 'depth')
time = grp.createVariable('time','f4', 'time')
w = grp.createVariable('w', 'f4', ('time', 'lat', 'lon', 'depth'))

longitude[:] = longitude_val
latitude[:] = latitude_val
time[:] = time_val
depth[:]= [1]

w[:] = w_array[:,2:156,2:120,:]

time.units = 'hours since 1950-01-01'
latitude.units = 'degrees_north'
depth.units = 'm'
depth.positive ='down'
depth.axis = 'Z'

w.units = 'm/day'

grp.close()



