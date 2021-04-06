from netCDF4 import Dataset
import numpy as np
import datetime as dt
import seawater as sw

# data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t0.nc')
# data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t1.nc')
# data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t2.nc')
# data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t3.nc')
# data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t4.nc')
data = Dataset('/Users/brownscholar/Documents/Intern/Archive/intern-data-t5.nc')

time = data.variables["time"]

startDate = dt.datetime(1950, 1, 1, 0, 0, 0)

for dayIndex in range(time.shape[0]):
	currentDate = startDate +dt.timedelta(hours=int(time[dayIndex]))
	day = currentDate.strftime("%y") + currentDate.strftime("%m") + currentDate.strftime("%d")

	soData = data.variables["so"][dayIndex, :, :, :]
	toData = data.variables["to"][dayIndex, :, :, :]
	depthData = data.variables["depth"][:]

	file = open("/Users/brownscholar/Documents/Intern/Data/density/density_"+str(day)+".gr","w")
	file.write("")
	file.close()

	file = open("/Users/brownscholar/Documents/Intern/Data/density/density_"+str(day)+".gr","w")
	file.write("1\n")
	file.write("158\t122\n")

	for x in range(0,1): #x, y, z are the indices.  #depth #
		for y in range(0,158):
			for z in range(0, 122):
				density = sw.dens(soData[x,y,z,], toData[x,y,z], depthData[0]) #created density function. #calculate the density at each end point using the sw.dens() function
				file.write("\t")
				file.write("%7f"%(1000-density)) #1000-density= adds units, "\t"= adds the tab
				file.write("\n")

	file.close()

	##Dynamic Height## 
for dayIndex in range(time.shape[0]):
	currentDate = startDate +dt.timedelta(hours=int(time[dayIndex]))
	day = currentDate.strftime("%y") + currentDate.strftime("%m") + currentDate.strftime("%d")

	g = data.variables["zo"][:]

	dynamic_file = open("/Users/brownscholar/Documents/Intern/Data/dynamic-height/dynamic-height_"+str(day)+".gr","w")
	dynamic_file.write("")
	dynamic_file.close()

	dynamic_file = open("/Users/brownscholar/Documents/Intern/Data/dynamic-height/dynamic-height_"+str(day)+".gr","w")
	dynamic_file.write("1\n")
	dynamic_file.write("158\t122\n")

	for x in range(0,1): 
		for y in range(0,158):
			for z in range(0, 122):
				dynamic_file.write("\t")
				dynamic_file.write("%7f"%(zoData[x, y, z]*100))
				dynamic_file.write("\n")

	dynamic_file.close()




