#!/bin/bash python3

#-------------------------------------------------------------------------
# ASSIGNMENT #1:
# Script to plot global temp
# by Daniel Horton, Feb 2017; mod to Python: Stacy, June 2019
# daniel.horton@northwestern.edu

# Objectives: Learn how to explore netCDF files using python, learn to use python map plotting libraries, 
#             Bonus challenge questions require manipulation of data, recommended to try and we can go over your attempts.
# 
#-------------------------------------------------------------------------

# ************ LIBRARIES ************

# Import libraries -> make sure these are available in a conda environment or in your computer
# You can import specific functions from a library by coding: from <LIB> import <FUNC> (as seen from netCDF4 import Dataset)

# There are two ways to explore netCDF files -- by netCDF or by xarray. 
# Learn both, choose your favorite. Understanding both is important so you can look up any answer.
# Advantage of netCDF4 library -- more straight forward, variables are easier to pull BUT difficult to setup correctly on your computer; advantage of xarray -- faster, more ubiquitous
import xarray as xr; from netCDF4 import Dataset 

# Global plotting can be done by cartopy or Basemap. Basemap is being depreciated, learn to love cartopy.
import cartopy.crs as ccrs

# Matplotlib is the classic plotting tool, honorable mention to Seaborn which can tweak matplotlib aesthetics.
import matplotlib.pyplot as plt

# numpy and pandas are a classic way to handle arrays. Pandas is slower but gives you a tabular format of data, easy to visualize. Numpy is faster, acts more like a list. Both reference each variable slightly differently -- understand the difference. Being able to switch between numpy and pandas will be helpful.
import numpy as np; import pandas as pd


# ************ USER INPUT ************

# Directory and filenames
file_in ="/projects/b1045/cmip/CMIP5/NCL_Practice/tas_Amon_CESM1-WACCM_rcp85_r2i1p1_200601-209912.nc"

# Load in file by using NetCDF4
NC=Dataset(file_in); DS=xr.open_dataset(file_in)

# Examine difference and similarities between netcdf formatted Dataset and xarray dataset
print(NC); print(DS)

# What is difference between NC.variables and DS.variables? Can you call a variable from each?
# Hint: look at what variables are available easily by printing NC.variables.keys()

# Pulling in top 10 timesteps from netCDF
# What are the units? What do these steps mean? Are the values different? 
NC['time'][0:10]; DS['time'][0:10]

#Note: NC -- days since 2005-01-01; DS -- cftimeDatetime objects

# Pull February 2066. How many values are in Feb. 2066? How would you do this with netCDF? Bonus points for writing out netCDF operations
feb66=DS.sel(time=slice('2066-02-01','2066-02-28'))
feb66_avg=feb66.mean(dim='time') 

# Our variables separated out. We don't really need to do this, could just keep feb66_avg and reference the lat/lon/temps. But this is just for clarity. 
lat= feb66_avg.lat
lon= feb66_avg.lon
tas= feb66_avg.tas

# Our variables separated out using netCDF. Again, just for clarity.
latNC= NC['lat'][:]
lonNC= NC['lon'][:]
tasNC= NC['tas'][:] # --> note this all the temps in all 1128 time steps. To get february, you need to find the index of february. then you can call tasNC[index_february2066] where index_february2066 is an integer. I asked you to do this earlier in a bonus question.

# !! Bonus challenge question -- change temperature from Kelvin to celsius!

# ************ PLOTTING ************

# Set map projection here. Check out what different map projections are. This matters because lat/lon variables are stored in different ways (-180 to 180 vs 0 360 for lon values), so you could get an error. This could also skew the information. Learn more about map projections through your own research!

#Projection for plot
projection= ccrs.PlateCarree(central_longitude=255);
# Data projection  -- these are different!
data_crs = ccrs.PlateCarree() 

# Open figure object
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=projection)
ax.set_global()
ax.coastlines()

#There are two ways to plot using contourf using lat lon. You can make a grid using lat lon to get the same size matrix as the data, then tell contourf the latlon=True
# For example: 
#xx,yy=np.meshgrid(lon,lat)
#cf=ax.contourf(xx,yy,tas,levels=60,latlon=True, transform=data_crs, cbar_kwargs={'label': DS.tas.units})

# Or you can just use the lat lon, no need to put latlon= True. Both look the same, so what is the real difference?
cf=ax.contourf(lon, lat, tas, levels=60, transform=data_crs, cbar_kwargs={'label': DS.tas.units})
plt.colorbar(cf)
ax.set_label(DS.tas.units)

# Add the gridlines, title, colorbar
ax.set_xticks([-180,-120,-60,0, 60, 120, 180], crs= projection)
ax.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs= projection)
ax.gridlines(crs=projection,linestyle="dotted")
plt.title("Temperature")

#Save our figure, show our figure! (Must save before showing)
plt.savefig('assignment1_feb66.png')
plt.show()

# !! Bonus challenge question: What does a different projection look like? Find the weirdest projection and plot the data. Find a subset of the current dataset. Change the color map for the contour plot.


