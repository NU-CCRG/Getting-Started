**Assignment #3**

**Introduction:**
For this assignment, you will continue to use WACCM data, but you will begin to learn how to parse data by seasons. 

**Task:**
Your assignment is to (1) create a 2006-2099 annual average global Mollweide map plot, (2) create a line plot of annual average global time series weighted by latitude, (3) create a line plot of global average temperature anomalies weighted by latitude with a baseline of 2006-2035, and (4) repeat steps 2 and 3 for each season (Spring: March-April-May, Summer: June-July-August, Autumn: Sept-Oct-Nov, Winter: Dec-Jab-Feb) with each season in a subplot.

It is recommended that you try to create this plot before checking the answer script.

**Directory:**
The CMIP file is located on QUEST. The path can be found here: /projects/b1045/cmip/CMIP5/NCL_Practice/tas_Amon_CESM1-WACCM_rcp85_r2i1p1_200601-209912.nc

To get a preview of the contents use the command line and type: 
`ncdump -h <file name>`

**Recommended libraries:** 
[xarray](https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f), [netCDF4](https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html), [cartopy](http://earthpy.org/tag/cartopy.html), [matplotlib.pyplot](https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html), [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html), [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min)
If you are unfamiliar with these libraries, explore the hyperlinked web pages to get an understanding. You may not necessarily use every single one of these libraries.
