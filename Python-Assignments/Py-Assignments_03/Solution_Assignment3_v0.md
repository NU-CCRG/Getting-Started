# ASSIGNMENT 3: Investigating by seasons

Notes by Irene

**Objectives:**

Use the WACCM netCDF file to

(1) create a 2006-2099 annual average global Mollweide map plot, 

(2) create a time series line plot of annual average global temperature weighted by latitude, 

(3) create a time series line plot of global average temperature anomalies weighted by latitude with a baseline of 2006-2035, and 

(4) repeat steps 2 and 3 for each season (Spring: March-April-May, Summer: June-July-August, Autumn: Sept-Oct-Nov, Winter: Dec-Jab-Feb) with each season in a subplot.

The first three tasks are similar to Assignments 1 and 2.
The fourth task is the main challenge in this assignment.

Before the solution key is provided, I'd like you to try to figure it out yourselves. To start you out, to get the seasonal mean, one approach is to **resample** your dataset into 3-monthly intervals according to the months within a season.

Here are two links that would help you with that:

1. http://xarray.pydata.org/en/stable/generated/xarray.Dataset.resample.html

2. https://pandas.pydata.org/pandas-docs/stable/user\_guide/timeseries.html#offset-aliases