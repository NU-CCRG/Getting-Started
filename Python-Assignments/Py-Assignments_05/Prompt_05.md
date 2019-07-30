**Assignment #5**

**Introduction:**

For this assignment, you will use the Weather Research Forecast Model output and compare it to real station data. This model run has a domain over the entire continental United States (CONUS) and outputs many meteorological variables. This assignment also asks you to analyze your results by including a caption for each figure that you make. We have provided a couple functions to help with the processing of the script, feel free to modify these functions or write your own. Included in this function script has some lines of main loop code that you may want to include into your own main loop so that your nomenclature is consistent with the functions. This is not necessary; it just will help with any confusion.

**Task**

*Part 1: Pull NOAA station data*
NOAA data is stored online, with each station saved as a CSV on a webpage. We have included a function that downloads the NOAA data from known, active climate stations over this time period and returns observations at hourly measurements on UTC time. Read through this function [def getRealData(LCD, dates, LCDvariables)] and understand how it operates. Guiding questions: what is the output of this function? What kind of format is the output? How would you use this output in order to compare it to the gridded WRF data? 

*Part 2: Overlay NOAA station data*

Given this station data, (a) plot the weeklong-average daytime temperature over CONUS with WRF and overlay average daytime temperature from the station, (b) average nighttime temperatures over CONUS and overlay average nighttime temperature from the station, (c) difference map between these two temperature maps and the stations, and (d) the variance between these two datasets over CONUS. 
Use circles to represent each station, filled with the color of the temperature, include a black border around the circle, and use 1 color bar for both the station and WRF (note: make sure your temperature and WRF data have the same units). Including subplot titles. Additionally, create a figure caption describing the main takeaway of the analysis. Make sure you reference subplots a-d when you create this caption (adding this figure caption doesn’t need to be in Python, you can import the figure to word to create your figure).

*Part 3: Pull Average Diurnal Temperature over Chicago*

To match the lat/lon of Chicago to the nearest grid cell in WRF, we have included the function find_index(stn_lon, stn_lat, wrf_lon, wrf_lat). When applied to this problem, the output of the function is a pair of indices corresponding to the point in the array which Chicago is located, such that the index pair returns the temperature at the given latitude and longitude you are interested in. We search for indices rather than the exact lat/lon pair because WRF has an array of center lat/lons that will very unlikely be an exact match to your very specific Chicago lat/lon pair. This function searches for the difference between the lat/lon pair and finds the index of the grid cell with the smallest difference between your lat/lon pair and the WRF grid cell center lat/lon pair. If you would like to solve this problem differently, you may. 
Create a 2-panel figure. (a) A map of CONUS with a star over Chicago, as to confirm that your index function gave you the right answer. Note: you cannot use the index to plot the star over Chicago, you must use the index to find the WRF lat-lon. (b) A line plot of the average hourly temperature over Chicago (you may choose a single gridcell to represent Chicago) with temperature on the Y-axis and time on the X-axis, include 95% confidence interval line for this line plot. Include titles for each subplot. Include a figure caption describing the main takeaway of this analysis (When is it hottest? Is that surprising?). 


*Extra credit or come up with your best hypothesis:* compare the hourly diurnal temperature cycle of Chicago to the average hourly diurnal temperature cycle of the whole United States. 

**Directory:**

The WRF file is located on QUEST. The path can be found here: `/projects/b1045/wrf-cmaq/output/Chicago_LADCO/Practice/`

**Recommended libraries: **

`xarray, netCDF4, cartopy,matplotlib.pyplot , numpy, pandas`

**NECESSARY libraries for functions:**

`pytz, time; dateutil, datetime, timezonefinder`


