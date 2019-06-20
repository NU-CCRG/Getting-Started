**Resources for Python usage in the Atmospheric, Climate, and Earth System Sciences**

**#1 – Python starter tips** 
 
[Python Tutorial](https://docs.python.org/3/tutorial/) <– to learn all the basics and some more complex stuff about object-oriented programming and whatnot.
 
One of the real powers in python is the massive library of pre-assembled scripts and packages. Anyone who is getting started in using python should first understand [Anaconda](https://conda.io/docs/user-guide/install/download.html). Anaconda is a package manager for python, much like macports or homebrew is for unix. Furthermore, anaconda comes pre-installed with all of the necessary packages to start tooling around with netCDF files, crunching numbers, and plotting cool stuff. If you want to just dive right in, a good synopsis of how to read in and plot netCDF data can be found [here](http://joehamman.com/2013/10/12/plotting-netCDF-data-with-Python/)
 
Here are some more basic tutorials on how to use 3 of the most important python packages:
 
To analyze netcdf data, you want to use the netCDF4 package for python (simply add the “import netCDF4” line at the top of the code). It is super straightforward, and all you need to know about it is found in a short few examples [here](http://aosc.umd.edu/~cmartin/python/examples/netcdf_example1.html) 
 
To plot things, you have options. See Data Viz below. 
 
Finally, to do matrix and array operations, use [Numpy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html). Numpy is VERY similar to Matlab. 
  
 
**#2 – Xarray**
 
Xarray helps you work with netcdf-type data: 

•	[Xarray for beginners](https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f)  

•	[Xray](https://nbviewer.jupyter.org/github/nicolasfauchereau/metocean/blob/master/notebooks/xray.ipynb)
 


**#3 – Climate Data Viz**
 
•	[CMIP Viz](https://carpentrieslab.github.io/python-aos-lesson/02-visualisation/index.html)       

•	[PCMDI Community Data Analysis Tool](https://uvcdat.llnl.gov/index.html)

•	[Map Projections](https://predictablynoisy.com/cartopy/tutorials/understanding_transform.html)  

•	[WRF-Python Plotting Examples](https://wrf-python.readthedocs.io/en/latest/plot.html) 

•	[Mapping w/ cartopy](https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html) 

•	[Weather/Climate Python Stack](rhttps://drclimate.wordpress.com/2016/10/04/the-weatherclimate-python-stack/)

 
**#4 – Other potentially helpful libraries**

•	Statistical Analyses: [statsmodels](http://www.statsmodels.org/stable/index.html) 
• Machine Learning / Clustering: [Scikit-learn](https://scikit-learn.org/stable/) 
 
