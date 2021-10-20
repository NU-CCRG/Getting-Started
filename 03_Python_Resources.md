**Resources for Python usage in the Atmospheric, Climate, and Earth System Sciences**

**#1 – Python starter tips** 
 
[Python Tutorial](https://cscircles.cemc.uwaterloo.ca/) <– If you have no familiarity with Python, complete this tutorial in order to understand the syntax and vocabularly related to Python programming. This provides a basis to everything you will learn moving forward. This tutorial does not include tutorials that use libraries -- libraries are a set of programs that someone else has developed to help you do work in Python. Below you will find links to important libraries that we use in our labwork.
 
In order to work with libraries in Python, you need to understand how to download the packages (the bundle of scripts in a library) so you can use it on your machine. In CCRG, we use Anaconda to access the pre-assembled libraries that others have posted: [Anaconda](https://conda.io/docs/user-guide/install/download.html). Anaconda is a package manager for python, much like macports or homebrew is for unix. 

The reason we use Anaconda is because we work with various file types. You're probably familiar with .csv files, but a lot of climate data are stored in .nc or .hdf files. These files are binary formatted, meaning that you can't just open them in Excel. These files have three basic parts: metadata, dimensions and variables. The metadata will include information on the grid that the data is placed on, the dimensions will outline how many grid cells there may be in the dataset, and the variables include in the information on the relevant environmental output which are placed on our grid with the given projection.  Our tutorials will go over netCDF file handling, but Anaconda comes pre-installed with all of the necessary packages to start tooling around with netCDF files, crunching numbers, and plotting cool stuff. If you want to just dive right in, a good synopsis of how to read in and plot netCDF data can be found [here](http://joehamman.com/2013/10/12/plotting-netCDF-data-with-Python/)
 
Here are some more basic tutorials on how to use 3 of the most important python packages:
 
To analyze netcdf data, you want to use the netCDF4 package for python (simply add the “import netCDF4” line at the top of the code). It is super straightforward, and all you need to know about it is found in a short few examples [here](http://aosc.umd.edu/~cmartin/python/examples/netcdf_example1.html).
 
To plot things, you have options. See Data Viz below. 
 
Finally, to do matrix and array operations, use [Numpy](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html). Numpy is VERY similar to Matlab. 
  
 
**#2 – Xarray**
 
Xarray helps you work with netcdf-type data: 

* [Xarray for beginners](https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f)  

* [Xray](https://nbviewer.jupyter.org/github/nicolasfauchereau/metocean/blob/master/notebooks/xray.ipynb)
 


**#3 – Climate Data Viz**
 
* [CMIP Viz](https://carpentrieslab.github.io/python-aos-lesson/02-visualisation/index.html)       

* [PCMDI Community Data Analysis Tool](https://uvcdat.llnl.gov/index.html)

* [Map Projections](https://predictablynoisy.com/cartopy/tutorials/understanding_transform.html)  

* [WRF-Python Plotting Examples](https://wrf-python.readthedocs.io/en/latest/plot.html) 

* [Mapping w/ cartopy](https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html) 

* [Weather/Climate Python Stack](https://drclimate.wordpress.com/2016/10/04/the-weatherclimate-python-stack/)

 
**#4 – Other potentially helpful libraries**

* Statistical Analyses: [statsmodels](http://www.statsmodels.org/stable/index.html)

* Machine Learning / Clustering: [Scikit-learn](https://scikit-learn.org/stable/) 
 
**#5 - Some other tutorials/examples for Python**

* [Python for Geosciences](https://github.com/koldunovn/python_for_geosciences)
* [Earthpy](http://earthpy.org/)
* [A gallery of interesting Jupyter Notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks)
