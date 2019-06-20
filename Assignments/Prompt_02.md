**Assignment #2**

**Introduction:**
For this assignment, you are tasked with creating two linear Python plots of 4D WACCM data. The Whole Atmosphere Community Climate Model (WACCM) is a comprehensive numerical model, spanning the range of altitude from the Earth's surface to the thermosphere. The development of WACCM is an inter-divisional collaboration that unifies certain aspects of the upper atmospheric modeling of HAO, the middle atmosphere modeling of ACOM, and the tropospheric modeling of CGD, using the NCAR Community Earth System Model (CESM) as a common numerical framework (from NCAR). 

**Task:**
Your assignment is to use the WACCM netCDF file (1) create a time series plot of global average monthly temperatures from 2006-2099 and (2) create a time series plot of global average annual temperature anomalies from 2006-2099. Use 2006-2035 as your baseline.

Bonus challenge #1: Use subplot functionality to put both of these plots in the same figure. 

It is recommended that you try to create this plot before checking the answer script.

**Directory:**
The WACCM file is located on QUEST. The path can be found here: /projects/b1045/cmip/CMIP5/NCL_Practice/tas_Amon_CESM1-WACCM_rcp85_r2i1p1_200601-209912.nc

To get a preview of the contents use the command line and type: 
`ncdump -h <file name>`


