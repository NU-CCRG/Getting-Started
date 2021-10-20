## In this overview, we have pulled useful commandline programs and NCO operators that can manipulate netCDF files super quickly. This can provide you a lot of simple tools to manipulate netCDF files. 

### Get header information -- gives you variable list, dimensions, previous nco operators, etc.
ncdump -h lat_lon_CONUS4K_d02.nc

### Make an average across time steps, ie: monthly average
ncra COMBINE_ACONC_201808*.nc avg.nc

### Concatenate files and retain timesteps
cd /projects/b1045/wrf-cmaq/output/Chicago_LADCO/output_Amy_noBUSplusLDV_wint_1.33km_sf_rrtmg_5_8_1_v3852/postprocess/
ncrcat COMBINE_ACONC_201901*.nc out_201901.nc

### Make a difference with 2 files with the same variables
ncdiff maxime_eldv_avg201808.nc baseline_avg201808.nc > diff.nc

### Pull out lat/lon
ncks -v LAT,LON GRIDCRO2D_CONUS4K_d02_2016-01-01.nc lat_lon_CONUS4K_d02.nc

### Drop variables from a file
ncks -x -v O1D,N2O5,PNA,C2O3,MEO2,RO2,PACD,AACD,CXO3,ALD2,XO2H,PANX,MEPX,MEOH,XO2,XO2N,XPAR,XPRP,NTR1,NTR2,FACD,HCO3,ALDX,GLYD,GLY,MGLY,ETHA,ETOH,KET,PAR,ACET,PRPA,ROR,OLE,IOLE,ISO2,ISPD,INTR,ISPX,HPLD,OPO3,EPOX,EPX2,CRES,BZO2,OPEN,XOPN,XYLMN,XLO2,XYLRO2,NAPH,PAHRO2,CRO,CAT1,CRON,OPAN,ECH4,CLNO2,SESQ,SOAALK,H2NO3PIJ,H2NO3PK,VLVPO1,VSVPO1,VSVPO2,VSVPO3,VIVPO1,VLVOO1,VLVOO2,VSVOO1,VSVOO2,VSVOO3,PCVOC,ALD2_PRIMARY,BUTADIENE13,ACROLEIN,ACRO_PRIMARY,TOLU,HG,HGIIGAS,ASO4J,ASO4I,ANH4J,ANH4I,ANO3J,ANO3I,AALK1J,AALK2J,AXYL1J,AXYL2J,AXYL3J,ATOL1J,ATOL2J,ATOL3J,ABNZ1J,ABNZ2J,ABNZ3J,APAH1J,APAH2J,APAH3J,ATRP1J,ATRP2J,AISO1J,AISO2J,ASQTJ,AORGCJ,AECJ,AECI,AOTHRJ,AOTHRI,AFEJ,AALJ,ASIJ,ATIJ,ACAJ,AMGJ,AKJ,AMNJ,ACORS,NUMATKN,NUMACC,NUMCOR,SRFATKN,SRFACC,SRFCOR,AH2OJ,AH2OI,AH3OPJ,AH3OPI,ANAJ,ANAI,ACLJ,ACLI,ASEACAT,ACLK,ASO4K,ANH4K,ANO3K,AH2OK,AH3OPK,AISO3J,AOLGAJ,AOLGBJ,AGLYJ,APCSOJ,ALVPO1I,ASVPO1I,ASVPO2I,ALVPO1J,ASVPO1J,ASVPO2J,ASVPO3J,AIVPO1J,ALVOO1I,ALVOO2I,ASVOO1I,ASVOO2I,ALVOO1J,ALVOO2J,ASVOO1J,ASVOO2J,ASVOO3J,NH3,SV_ALK1,SV_ALK2,SV_XYL1,SV_XYL2,SV_TOL1,SV_TOL2,SV_BNZ1,SV_BNZ2,SV_PAH1,SV_PAH2,SV_TRP1,SV_TRP2,SV_ISO1,SV_ISO2,SV_SQT,LV_PCSOG CCTM_CONC_v3852_20160101.nc CCTM_CONC_v3852_20160101.drop.nc

### Get a preliminary visualization of netCDF file
ncview baseline_avg201808.nc

### Create mda8 o3 -- need to make hourly megafile using nrcat, then can use this script
/projects/b1045/cmaq/cmaq_v5.2/POST/hr2day/scripts/run_hr2day.csh

Further reading on NCO OPERATORS
http://nco.sourceforge.net/

