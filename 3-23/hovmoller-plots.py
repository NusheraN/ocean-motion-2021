import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from netCDF4 import Dataset
import numpy as np

#get the data from the netcdf 
hovfile = "/Users/brownscholar/documents/intern/data/atlantic-w.nc/"

#create a numpy array create an empty numpy array for the hovmoller diagram with the dimension of width and years

