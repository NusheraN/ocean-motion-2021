#import libaries to create the plot 
import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

#opening our ss1a2ww file which came from the fortran code. 
w_file = '/Users/brownscholar/Downloads/ss1a2ww.gr' 
w = open(w_file, "r") #opening the file 

#open netcdf file
original_data = Dataset("/Users/brownscholar/Documents/Intern/Archive/intern-data-t0.nc")

#geting latitude and longitude data from netcdf file:
lat = original_data.variables['latitude'] 
lon = original_data.variables['longitude']

#defining the depths, latitude and longtiture to make the empty number array (line 26)
num_lat = 158 
num_lon = 122 
levels = 1 

# make empty numpy array of shape lat, lon depth shape for storing w:
w_values = np.zeros((levels,num_lat,num_lon)) # fills the array with zeros, import data in to a structured arrary (multidemisional  geography )

# use a loop to read w_file into the variable
#(skip first two lines of the file)
w.readline() #reads the line of code and by putting two you skip the first two it lets you only read the numbers in  the loop because the first two lines are just the depths, latitude and longitude and we don't really need that information. 
w.readline() 
for i in range(0,levels): # range 0 to 1
    for j in range(0, num_lat): # ranges 0 to 158
        for k in range(0, num_lon): # range 0 to 122
            w_values[i,j,k] = w.readline() #reads in the numbers in the empty array


#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128) 
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue') 


#now use the following function to plot your data:
#function to make colorplot is:
# p = plt.pcolormesh(V,cmap = newcmp), where V is the numpy array with the data
p = plt.pcolormesh(w_values[0,2:-2,2:-2],cmap = newcmp)

plt.xlabel("Longitude")# labels x axis
plt.ylabel("Latitude")# labels the y axis
plt.title("ColorMap")# labels the entire map
plt.scatter([],[], color = "blue", label = "going down")#lables legend
plt.scatter([],[], color = "red", label = "going up")#lables legend
plt.legend(bbox_to_anchor=[1.0,1.0])# create legend
plt.xticks(np.arange(0,num_lon,10),lon[::10])
plt.yticks(np.arange(0,num_lat,10),lat[::10])
plt.show()

# you can use these to add the x and y ticks to your plot:
# I am happy to talk to you about why this works
