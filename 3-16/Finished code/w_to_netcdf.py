# script to turn w outputs into netcdf
import os
import numpy as np
import datetime
from netCDF4 import Dataset

num_lat = 158
num_lon = 122
levels = 1
dates = 1356

#path to w files (created by fortran code)
w_path = '/Users/brownscholar/Documents/Intern/data/omega/w/'

#creates file name from date_list
date_list = open('/Users/brownscholar/Documents/Intern/ocean-motion-2021/3-23/date_list.txt','r')

#creates blank array to fill
w_array = np.zeros((dates,num_lat,num_lon,levels))

#loops through number of dates
for d in range(0,dates):
	#opens w file
	filename = (date_list.readline()).strip('\n')+"_ww.gr" 
	print(filename)

	if os.path.isfile(w_path+filename): #checking to see if the path created is a real file name
		w_file = open(w_path+filename,"r") #opens w file
		w_file.readline() #skips the header in w file
		w_file.readline()
		#loops through depth
		for i in range(0,levels):
			for j in range(0,num_lat): #loops through latitude
				for k in range(0,num_lon): #loops through longitude
					w = w_file.readline() # takes value from w file and puts it into numpy array
					w_array[d,j,k,i] = float(w)
					#print(w)
	

latitude_val = np.arange(12.625+.5,51.875-0.25,0.25) #creates numpy array with all of the latitude values
longitude_val = np.arange(311.875+.5,342.125-0.25,0.25) #creates numpy array with all of the longitude values
time_val = np.arange(377064,604704+168,168) #creates numpy array with all of the time values
print(time_val.size)

grp = Dataset('/Users/brownscholar/Documents/Intern/Data/atlantic-w','w', format='NETCDF4') # opens netcdf file
grp.createDimension('lon', num_lon-4) #creates dimensions in netcdf file
grp.createDimension('lat', num_lat-4) #creates dimensions in netcdf file
grp.createDimension('depth', levels) #creates dimensions in netcdf file
grp.createDimension('time', dates) #creates dimensions in netcdf file

#creates variables in numpy array 
longitude = grp.createVariable('longitude', 'f4', 'lon') #f4 means that the values will be floats
latitude = grp.createVariable('latitude', 'f4', 'lat')  #f4 means that the values will be floats
depth = grp.createVariable('depth', 'f4', 'depth') #f4 means that the values will be floats
time = grp.createVariable('time','f4', 'time') #f4 means that the values will be floats
w = grp.createVariable('w', 'f4', ('time', 'lat', 'lon', 'depth')) #f4 means that the values will be floats

#fills the variables in the netcdf file with the values from the numpy arrays
longitude[:] = longitude_val 
latitude[:] = latitude_val
time[:] = time_val
depth[:]= [1]

w[:] = w_array[:,2:156,2:120,:] #crops out uneeded rows and columbs 

#adds units to netcdf variables
time.units = 'hours since 1950-01-01'
latitude.units = 'degrees_north'
depth.units = 'm'
depth.positive ='down'
depth.axis = 'Z'

w.units = 'm/day'

grp.close() #closes netcdf file




