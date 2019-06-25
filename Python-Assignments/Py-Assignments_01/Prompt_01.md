**Assignment #1**

**Introduction:**
For this assignment, you are tasked with creating a Python plot of Climate Model Intercomparison Project [CMIP](https://www.wcrp-climate.org/wgcm-cmip) data. CMIP is a standard experimental framework for studying the output of coupled atmosphere-ocean general circulation models. This facilitates assessment of the strengths and weaknesses of climate models which can enhance and focus the development of future models. For example, if the models indicate a wide range of values either regionally or globally, then scientists may be able to determine the cause(s) of this uncertainty.

**Task:**
Your assignment is to plot February 2066 global temperature using the Plate Carree projection. 
Bonus challenge #1: Convert the temperature from Kelvin to Celsius.
Bonus challenge #2: Change the projection and change the colormap of the plot.

It is recommended that you try to create this plot before consulting the answer script. The answer script does not include answers to the challenge questions, though you may ask anyone for help.

**Directory:**
The CMIP file is located on QUEST. The path can be found here: /projects/b1045/cmip/CMIP5/NCL_Practice/tas_Amon_CESM1-WACCM_rcp85_r2i1p1_200601-209912.nc

To get a preview of the contents of this file you can use an NCO command. NCO is a command software that allows you to perform operations on netcdf files. To use NCO on QUEST you can invoke `module load nco` or set up your .bashrc environmnet by following the directions [here](02_SetUp_bashrc.md). 

After NCO is loaded, you can preview the file contents by typing: 
`ncdump -h <file name>`


**Recommended libraries:** 
[xarray](https://towardsdatascience.com/handling-netcdf-files-using-xarray-for-absolute-beginners-111a8ab4463f), [netCDF4](https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html), [cartopy](http://earthpy.org/tag/cartopy.html), [matplotlib.pyplot](https://matplotlib.org/3.1.0/tutorials/introductory/pyplot.html), [numpy](https://docs.scipy.org/doc/numpy/user/quickstart.html), [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html#min)
If you are unfamiliar with these libraries, explore the hyperlinked web pages to get an understanding. You may not necessarily use every single one of these libraries.
