
#  ----------------------------------------------------
#  ------------------ Functions -----------------------
#  ----------------------------------------------------

#  ----------------------------------------------------
#  Function: find_index
#  Description: Given a lat lon station pair, this returns the index of that lat lon in the model array.
#  adapted from : http://kbkb-wx-python.blogspot.com/2016/08/find-nearest-latitude-and-longitude.html
#
#  - INPUTS: a list of stations' lats, lons and wrf's lats and lons
#  ----------------------------------------------------
def find_index(stn_lon, stn_lat, wrf_lon, wrf_lat):
# stn -- points 
# wrf -- list
   xx=[];yy=[]
   for i in range(len(stn_lat)):
      abslat = np.abs(wrf_lat-stn_lat[i])
      abslon= np.abs(wrf_lon-stn_lon[i])
      c = np.maximum(abslon,abslat)
      latlon_idx = np.argmin(c)
      x, y = np.where(c == np.min(c))
      #add indices of nearest wrf point station
      xx.append(x)
      yy.append(y)
   #return indices list
   return xx, yy

#  ----------------------------------------------------
#  Function: find
#  Description: Returns the list of indices where the list has values that match the target. Used in getRealData func.
#  modified from https://stackoverflow.com/questions/16685384/finding-the-indices-of-matching-elements-in-list-in-python
#
#  - INPUTS: list (lst) and target (a)
#  ----------------------------------------------------
def find(lst, a):
    return [i for i, x in enumerate(lst) if x==a]


#  ----------------------------------------------------
#  Function: offset
#  Description: Use a library to find UTC hour offset given a lat/lon pair. Used in getRealData func.
#
#  - INPUTS: lat lon of target location
#  ----------------------------------------------------
def offset(lat,lon):
    # libraries
    import pytz
    import time; import pandas as pd; import numpy as np; import dateutil.parser as dparser
    from timezonefinder import TimezoneFinder; from pytz import timezone; from datetime import datetime,date, timedelta
    tf = TimezoneFinder(in_memory=True)
    utc = pytz.utc
    #returns a location's time zone offset from UTC in minutes.
    today = datetime.now()
    tz_target = timezone(tf.certain_timezone_at(lat=lat, lng=lon))
    # ATTENTION: tz_target could be None! handle error case
    today_target = tz_target.localize(today)
    today_utc = utc.localize(today)
    return (today_utc - today_target).total_seconds() / 3600


#  ----------------------------------------------------
#  Function: getRealData
#  Description: Pull in real data, apply UTC, and average duplicate hourly values.
#               Return an array fill with the variables you are interested in.
#
#  INPUTS: 
#  LCD = pd.read_csv(NOAAdataLink + stationList[i]), with i corresponding to one station from the list of station names given in the station_out file
#  dates = dates over the modeling period you want to compare to. Assumes isoformat naming scheme, which is default WRF output filename.
#  LCDvariables = the header names of the variables from the NOAA LCD file
#  ----------------------------------------------------

def getRealData(LCD, dates, LCDvariables):
   # import necessary libraries into temp memory...
   import time; import pandas as pd; import numpy as np; import dateutil.parser as dparser
   from datetime import datetime,date, timedelta
   from timezonefinder import TimezoneFinder; from pytz import timezone
#
   # Start loop timer for total count of how long it takes to pull the data
   big_start=time.time()
#
   # Create empty variables for dates and times
   date_noTime= [LCD['DATE'][z].split('T')[0] for z in range(len(LCD['DATE']))]
   time_noDate=[LCD['DATE'][z].split('T')[1] for z in range(len(LCD['DATE']))]
#
   # Find UTC offset
   UTC_offset=-offset(lon=LCD['LONGITUDE'][0], lat=LCD['LATITUDE'][0])
#
   # Pull day before and after for UTC offset sake
   date_onedaybefore=(dparser.parse(dates[0])-timedelta(days=1)).isoformat().split('T')[0]
   date_onedayafter=(dparser.parse(dates[-1])+timedelta(days=1)).isoformat().split('T')[0]
#
   # Get index of the first day of the model run from the LCD dataset 
   start_ind_dataset = find(date_noTime, date_onedaybefore)[0]
   end_ind_dataset= find(date_noTime, date_onedayafter)[-1]
#
   # Start actual UTC offset calculator
   if Chatty: print('-> Adding UTC offset to timestamp and averaging repeated values (%.2f)'%(time.time()-big_start,))
#
   # Get the time and round up or round down, also add the UTC offset such that correct time is in UTC
   # Set the corrected variable list
   #correctedTime=[];correctedSLP=[]; correctedWindDir=[]; correctedRH=[]; correctedWind =[]; correctedRain=[]; correctedTemp =[];correctedDate=[]
   correctedTime=[]; correctedDate=[]; correctedLCDVar=[[] for i in range(len(LCDvariables))]
   # Start loop through the LCD real data given model run dates
   for i in range(len(LCD[start_ind_dataset: end_ind_dataset])): # I recognize there are more intuitive loopings oops..
      datetimeLCD=dparser.parse(LCD['DATE'][start_ind_dataset+i])
      datetimeLCD_UTC = datetimeLCD + timedelta(hours=UTC_offset)
      for zz in range(len(correctedLCDVar)):
         try:
            correctedLCDVar[zz].append(float(LCD[LCDvariables[zz]][start_ind_dataset+i]))
         except ValueError:
            correctedLCDVar[zz].append(float('nan'))
#
      # Round the times
      if datetimeLCD_UTC.minute >= 30:
            correctedTime.append((datetimeLCD_UTC+timedelta(minutes=60-datetimeLCD_UTC.minute)).isoformat().split('T')[1])
            correctedDate.append((datetimeLCD_UTC+timedelta(minutes=60-datetimeLCD_UTC.minute)).isoformat().split('T')[0])
      elif datetimeLCD_UTC.minute < 30:
            correctedTime.append((datetimeLCD_UTC+timedelta(minutes=-datetimeLCD_UTC.minute)).isoformat().split('T')[1])
            correctedDate.append((datetimeLCD_UTC+timedelta(minutes=-datetimeLCD_UTC.minute)).isoformat().split('T')[0])
      else:
            correctedTime.append((datetimeLCD_UTC).isoformat().split('T')[1])
            correctedDate.append((datetimeLCD_UTC).isoformat().split('T')[0])
#
   # Now filter LCD so that it only uses UTC date times
   # crop datasets to start at correct first starting date
   start_ind_dataset2 = find(correctedDate, dates[0])[0]
   end_ind_dataset2 = find(correctedDate, dates[-1])[-1]
   #
   correctedDate= correctedDate[start_ind_dataset2: end_ind_dataset2]; correctedTime = correctedTime[start_ind_dataset2: end_ind_dataset2]
   correctedLCDVar= [correctedLCDVar[qq][start_ind_dataset2: end_ind_dataset2] for qq in range(len(correctedLCDVar))]
#
   #Now nan-average repeating values
   correctedLCDVar_noRepeats = [[] for qq in range(len(LCDvariables))]
   timeCorrected_noRepeats=[]; dateCorrected_noRepeats=[]
   i=0 #reset
   while i < len(correctedTime): 
         j=1
         tmpVar = [[] for qq in range(len(LCDvariables))]
         while i+j < len(correctedTime)-1 and correctedTime[i] == correctedTime[i+j]:
            for qq in range(len(LCDvariables)):
                tmpVar[qq].append(correctedLCDVar[qq][i+j])
            # move forward in search
            j=j+1
         # If none of the variables are repeated, just put in the variables without averaging
         if [len(tmpVar[qq]) == 0 for qq in range(len(LCDvariables))] == [True for qq in range(len(LCDvariables))]:
            for qq in range(len(LCDvariables)):
                correctedLCDVar_noRepeats[qq].append(correctedLCDVar[qq][i])
            for qq in range(len(LCDvariables)):
                correctedLCDVar_noRepeats[qq].append(correctedLCDVar[qq][i])
         # If the variables are duplicated, nanmean this
         else:
            for qq in range(len(LCDvariables)):
               correctedLCDVar_noRepeats.append(np.nanmean(tmpVar[qq]))
#
         timeCorrected_noRepeats.append(correctedTime[i])
         dateCorrected_noRepeats.append(correctedDate[i])
         # Move forward the counters
         if j == 1 and i<len(correctedTime):
            i=i+1
         if j>1 and i<len(correctedTime):
            i=i+j
   # Finished while loop
   if Chatty: print('-> Finished averaging duplicate values in station %s dataset'% str(station))
   #VERY quick check to see if all data is available, if not, flag it for later
   missing_dates=[];missing_hours=[]
   if len(dates) == len(list(set(dateCorrected_noRepeats))):
      if Chatty: print('-> No missing dates at station %s' %(stationList[station],))
   else:
      if Chatty: print('-> Missing dates at %s' %(stationList[station],))
      missing_dates.append(stationList[station])
   #next
   if len(list(set(timeCorrected_noRepeats))) == 24:
      if Chatty: print('-> No missing hours at station %s' %(stationList[station],))
   else:
      if Chatty: print('-> Missing hours at %s' %(stationList[station],))
      missing_hours.append(stationList[station])
   #return
   if Chatty: print('-> Done (%.2f sec)'%(time.time()-big_start,))
   return dateCorrected_noRepeats, timeCorrected_noRepeats, correctedLCDVar_noRepeats, UTC_offset


#----------- MAIN LOOP
# --- * Include this in your own main loop *
# --- * This is given so nomenclature is consistent in the functions above *

import pandas as pd

# ------- User input 
# dir to data
dir='/projects/b1045/wrf-cmaq/output/Chicago_LADCO/Practice/'

# data with lat lon and names of NOAA stations ... this was preprocessed
station_out_name= 'station_out_removedmissing.csv'

# link to data
NOAAdataLink="https://www.ncei.noaa.gov/data/local-climatological-data/access/2018/"

# Climate variables you are interested in
LCDvariables=['HourlyDryBulbTemperature']
Chatty = True # turn on print statements

# Pull in station data 
station_out=pd.read_csv(dir+station_out_name)
# Pull station lats and lons
stn_lat= station_out['lat']; stn_lon= station_out['lon'] 
# Pull list of station names for input to getRealData
stationList =station_out['stn']
dates=[filenames_d01[z].split("wrfout_d01_")[1].split("_00:00:00")[0] for z in range(len(filenames_d01))]





