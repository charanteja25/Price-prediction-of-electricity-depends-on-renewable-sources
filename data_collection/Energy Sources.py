# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 22:48:55 2023

@author: paulo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot.gca() 
import matplotlib.axes.Axes.plot()
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import minmax_scale, normalize
import seaborn as sn
%matplotlib inline

S_Data=pd.read_csv(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\Generation_sources.csv")

S_Data.info()

S_Data2= S_Data.loc[:, ['DATETIME','WIND','SOLAR','HYDRO','RENEWABLE_perc']]

S_Data3= S_Data.loc[:, ['RENEWABLE','FOSSIL']]

S_Data4= S_Data.loc[:, ['DATETIME','WIND','SOLAR','HYDRO']]

S_Data2.boxplot()

S_Data3.boxplot(patch_artist= True, boxprops= dict(facecolor='white', color='black'),whiskerprops=dict(color='black'),capprops=dict(color='black'), medianprops=dict(color='black'))
plt.title('Renewable Energy vs Non-Renewable')
plt.ylabel('Power Generation(MWh)')
plt.grid(visible=False)
plt.show()

S_Data4.boxplot(patch_artist= True, boxprops= dict(facecolor='white', color='black'),whiskerprops=dict(color='black'),capprops=dict(color='black'), medianprops=dict(color='black'))
plt.title('Renewable Energy vs Non-Renewable')
plt.ylabel('Power Generation(MWh)')
plt.grid(visible=False)
plt.show()


S_Data2.boxplot(patch_artist= True, boxprops= dict(facecolor='white', color='black'),whiskerprops=dict(color='black'),capprops=dict(color='black'), medianprops=dict(color='black'))
plt.title('Renewable Energy')
plt.ylabel('Power Generation(MWh)')
plt.grid(visible=False)
plt.show()

S_Data2['DATETIME'] = pd.to_datetime(S_Data2['DATETIME']).dt.date

S_Data2.info()

sn.lineplot(data =S_Data2, x='DATETIME', y='RENEWABLE_perc')
plt.xlabel('DATETIME')
plt.ylabel('Renewable Energy %')
plt.show()

plt.plot(S_Data2['DATETIME'], S_Data2['SOLAR'], label='SOLAR')
plt.plot(S_Data2['DATETIME'], S_Data2['WIND'],  label='WIND')
plt.plot(S_Data2['DATETIME'], S_Data2['HYDRO'], label='HYDRO')
plt.xlabel('Date')
plt.ylabel('Generation in MWh')
plt.title('Generation by sources')
plt.legend()
plt.show()

# _________________________Select rows within a date range by year 2014________________________________________
start_date = pd.to_datetime('2014-01-01 00:00:00+00')
end_date = pd.to_datetime('2014-12-31 23:30:00+00')
Sources_2014 = S_Data2[(S_Data2['DATETIME'] >= start_date) & (S_Data2['DATETIME'] <= end_date)]


Sources_2014.head()
Sources_2014.tail()

#Year 2014 graph of solar generation
sn.lineplot(data =Sources_2014, x='DATETIME', y='SOLAR')
plt.xlabel('Dates')
plt.ylabel('Generation in MWh')
plt.title('2014 Solar Generation')
plt.show()

# Plotting the line plots
plt.plot(Sources_2014['DATETIME'], Sources_2014['SOLAR'], label='SOLAR')
plt.plot(Sources_2014['DATETIME'], Sources_2014['WIND'],  label='WIND')
plt.plot(Sources_2014['DATETIME'], Sources_2014['HYDRO'], label='HYDRO')
plt.xlabel('Date')
plt.ylabel('Generation in MWh')
plt.title('2014 Generation by sources')
plt.legend()
plt.show()


# Select rows within a date range by MONTH
start_date1 = pd.to_datetime('2014-01-01 00:00:00+00')
end_date1 = pd.to_datetime('2014-01-31 23:30:00+00')
Sources_month1 = S_Data2[(S_Data2['DATETIME'] >= start_date1) & (S_Data2['DATETIME'] <= end_date1)]

#Plotting the three different sources at same time
plt.plot(Sources_month1['DATETIME'], Sources_month1['SOLAR'], label='SOLAR')
plt.plot(Sources_month1['DATETIME'], Sources_month1['WIND'],  label='WIND')
plt.plot(Sources_month1['DATETIME'], Sources_month1['HYDRO'], label='HYDRO')
plt.xlabel('Date')
plt.ylabel('Sources')
plt.title('2014 Month1 Generation by sources')
plt.legend()
plt.show()


#Month January 2014 graph of solar
sn.lineplot(data =Sources_month1, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('January 2014')
plt.show()

# Select rows January within a date range by week1
start_date2 = pd.to_datetime('2014-01-01 00:00:00+00')
end_date2 = pd.to_datetime('2014-01-07 23:30:00+00')
Sources_week1 = S_Data2[(S_Data2['DATETIME'] >= start_date2) & (S_Data2['DATETIME'] <= end_date2)]


#week1 January 2014 graph of solar1
sn.lineplot(data =Sources_week1, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('January week1')
plt.show()

# Select rows within a date range by week2
start_date3 = pd.to_datetime('2014-01-07 00:00:00+00')
end_date3 = pd.to_datetime('2014-01-14 23:30:00+00')
Sources_week2 = S_Data2[(S_Data2['DATETIME'] >= start_date3) & (S_Data2['DATETIME'] <= end_date3)]


#week2 1 2014 graph of solar2
sn.lineplot(data =Sources_week2, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('January week2')
plt.show()


# Select rows within a date range by week3
start_date4 = pd.to_datetime('2014-01-14 00:00:00+00')
end_date4 = pd.to_datetime('2014-01-21 23:30:00+00')
Sources_week3 = S_Data2[(S_Data2['DATETIME'] >= start_date4) & (S_Data2['DATETIME'] <= end_date4)]


#week3 1 2014 graph of solar
sn.lineplot(data =Sources_week3, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('January week3')
plt.show()

# Select rows within a date range by week3
start_date5 = pd.to_datetime('2014-01-21 00:00:00+00')
end_date5 = pd.to_datetime('2014-01-31 23:30:00+00')
Sources_week4 = S_Data2[(S_Data2['DATETIME'] >= start_date5) & (S_Data2['DATETIME'] <= end_date5)]

#week4 1 2014 graph of solar
sn.lineplot(data =Sources_week4, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('January week4')
plt.show()

"""Inspecting month 11 of the data November"""

# Select rows within a date range by MONTH
july_start = pd.to_datetime('2014-07-01 00:00:00+00')
july_end = pd.to_datetime('2014-07-31 23:30:00+00')
july_2014 = S_Data2[(S_Data2['DATETIME'] >= july_start) & (S_Data2['DATETIME'] <=july_end)]

#Month July 2014 graph of solar
sn.lineplot(data =july_2014, x='DATETIME', y='SOLAR')
plt.xlabel('DATETIME')
plt.ylabel('SOLAR')
plt.title('July 2014')
plt.show()

# Select rows July within a date range by week1
july_start1 = pd.to_datetime('2014-07-01 00:00:00+00')
july_end1 = pd.to_datetime('2014-07-07 23:30:00+00')
july_week1 = S_Data2[(S_Data2['DATETIME'] >= july_start1) & (S_Data2['DATETIME'] <=july_end1)]


#week1 January 2014 graph of solar1
sn.lineplot(data =july_week1, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('July week1')
plt.show()

# Select rows within a date range by week2
july_start2 = pd.to_datetime('2014-07-07 00:00:00+00')
july_end2 = pd.to_datetime('2014-07-14 23:30:00+00')
july_week2 = S_Data2[(S_Data2['DATETIME'] >= july_start2) & (S_Data2['DATETIME'] <=july_end2)]


#week2 July 2014 graph of solar1
sn.lineplot(data =july_week2, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('July week2')
plt.show()

# Select rows within a date range by week3
july_start3 = pd.to_datetime('2014-07-14 00:00:00+00')
july_end3 = pd.to_datetime('2014-07-21 23:30:00+00')
july_week3 = S_Data2[(S_Data2['DATETIME'] >= july_start3) & (S_Data2['DATETIME'] <=july_end3)]


#week3 July 2014 graph of solar1
sn.lineplot(data =july_week3, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('July week3')
plt.show()

# Select rows within a date range by week4
july_start4 = pd.to_datetime('2014-07-21 00:00:00+00')
july_end4 = pd.to_datetime('2014-07-31 23:30:00+00')
july_week4 = S_Data2[(S_Data2['DATETIME'] >= july_start4) & (S_Data2['DATETIME'] <=july_end4)]


#week3 July 2014 graph of solar1
sn.lineplot(data =july_week4, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('July week4')
plt.show()


#plt.plot(Sources_week1['DATETIME'], Sources_week1['SOLAR'], label='SOLAR')
#plt.plot(Sources_week1['DATETIME'], Sources_week1['WIND'],  label='WIND')
#plt.plot(Sources_week1['DATETIME'], Sources_week1['HYDRO'], label='HYDRO')
#plt.xlabel('Date')
#plt.ylabel('Sources')
#plt.title('2014 Month1 Generation by sources')
#plt.legend()
#plt.show()

"""Inspecting month 11 of the data November"""

# Select rows within a date range by MONTH
Nov_start = pd.to_datetime('2014-11-01 00:00:00+00')
Nov_end = pd.to_datetime('2014-11-30 23:30:00+00')
Nov_2014 = S_Data2[(S_Data2['DATETIME'] >= Nov_start) & (S_Data2['DATETIME'] <=Nov_end)]

#Month November 2014 graph of solar
sn.lineplot(data =Nov_2014, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('November 2014')
plt.show()

# Select rows November within a date range by week1
Nov_start1 = pd.to_datetime('2014-11-01 00:00:00+00')
Nov_end1 = pd.to_datetime('2014-11-07 23:30:00+00')
Nov_week1 = S_Data2[(S_Data2['DATETIME'] >= Nov_start1) & (S_Data2['DATETIME'] <=Nov_end1)]

#week1 November 2014 graph of solar1
sn.lineplot(data =Nov_week1, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('November week1')
plt.show()

# Select rows November within a date range by week2
Nov_start2 = pd.to_datetime('2014-11-07 00:00:00+00')
Nov_end2 = pd.to_datetime('2014-11-14 23:30:00+00')
Nov_week2 = S_Data2[(S_Data2['DATETIME'] >= Nov_start2) & (S_Data2['DATETIME'] <=Nov_end2)]


#week2 November 2014 graph of solar1
sn.lineplot(data =Nov_week2, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('November week2')
plt.show()

# Select rows November within a date range by week3
Nov_start3 = pd.to_datetime('2014-11-14 00:00:00+00')
Nov_end3 = pd.to_datetime('2014-11-21 23:30:00+00')
Nov_week3 = S_Data2[(S_Data2['DATETIME'] >= Nov_start3) & (S_Data2['DATETIME'] <=Nov_end3)]

#week3 November 2014 graph of solar1
sn.lineplot(data =Nov_week3, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('November week3')
plt.show()

# Select rows November within a date range by week4
Nov_start4 = pd.to_datetime('2014-11-21 00:00:00+00')
Nov_end4 = pd.to_datetime('2014-11-30 23:30:00+00')
Nov_week4 = S_Data2[(S_Data2['DATETIME'] >= Nov_start4) & (S_Data2['DATETIME'] <=Nov_end4)]


#week3 July 2014 graph of solar1
sn.lineplot(data =Nov_week4, x='DATETIME', y='SOLAR')
plt.xlabel('Date')
plt.ylabel('Solar Generation')
plt.title('November week4')
plt.show()




"""_________________________Applying Moving average to the data sets__________________________"""

def moving_average(data, window_size):
    df = pd.DataFrame(data)
    rolling_mean = df.rolling(window=window_size).mean()
    filtered_data = rolling_mean.values.flatten()
    return filtered_data

data = S_Data2.loc[:, ['WIND']]
window_size = 200

filtered_data = moving_average(data, window_size)
print(filtered_data)

Wind = pd.DataFrame(filtered_data)

wind_start =pd.to_datetime('2009-01-01 00:00:00')
wind_end = pd.to_datetime('2022-12-31 00:00:00')
interval = pd.Timedelta(minutes=30)

Wind["Date"] = pd.DataFrame({'Date': pd.date_range(start=wind_start, end=wind_end, freq=interval)})

Wind2= Wind.rename(columns={0:'Wind Gen'})

Wind2[0]

Wind2.info()



sn.lineplot(data =Wind2, x='Date', y='Wind Gen')
plt.xlabel('Date')
plt.ylabel('Generation in Mwh')
plt.title('Filtered wind gen')
plt.show()


#Filtering for solar Year 2014
data1 = Sources_2014.loc[:, ['SOLAR']]
window_size = 200

filtered_solar2014 = moving_average(data1, window_size)
print(filtered_data)

Solar= pd.DataFrame(filtered_solar2014)

Solar= Solar.rename(columns={0:'Solar Gen'})

solar_start =pd.to_datetime('2014-01-01 00:00:00')
solar_end = pd.to_datetime('2014-12-31 00:00:00')
interval = pd.Timedelta(minutes=30)

Solar["Date"] = pd.DataFrame({'Date': pd.date_range(start=solar_start, end=solar_end, freq=interval)})

sn.lineplot(data = Solar, x='Date', y='Solar Gen')
plt.xlabel('Date')
plt.ylabel('Generation in Mwh')
plt.title('Filtered solar gen 2014')
plt.show()



#Filtering for sources
data2 = S_Data2.loc[:, ['SOLAR']]
window_size = 200

Source_solar = moving_average(data2, window_size)

 
Sources_solar1= pd.DataFrame(Source_solar)

Sources_solar1 = Sources_solar1.rename(columns={0:'Solar Gen'})

ssolar_start =pd.to_datetime('2009-01-01 00:00:00')
ssolar_end = pd.to_datetime('2022-12-31 00:00:00')
interval = pd.Timedelta(minutes=30)

Sources_solar1["Date"] = pd.DataFrame({'Date': pd.date_range(start=ssolar_start, end=ssolar_end, freq=interval)})

sn.lineplot(data = Sources_solar1, x='Date', y='Solar Gen')
plt.xlabel('Date')
plt.ylabel('Generation in Mwh')
plt.title('Filtered solar gen')
plt.show()


data3 = S_Data2.loc[:, ['HYDRO']]
window_size = 200

Source_hydro = moving_average(data3, window_size)

 
Sources_hydro = pd.DataFrame(Source_hydro)

Sources_hydro = Sources_hydro.rename(columns={0:'Hydro Gen'})

hydro_start =pd.to_datetime('2009-01-01 00:00:00')
hydro_end = pd.to_datetime('2022-12-31 00:00:00')
interval = pd.Timedelta(minutes=30)

Sources_hydro["Date"] = pd.DataFrame({'Date': pd.date_range(start=hydro_start, end=hydro_end, freq=interval)})

sn.lineplot(data = Sources_hydro, x='Date', y='Hydro Gen')
plt.xlabel('Date')
plt.ylabel('Generation in Mwh')
plt.title('Filtered Hydro gen')
plt.show()


Filtered_sources= pd.merge(Sources_hydro, Sources_solar1, on='Date')

Filtered_sources2= pd.merge(Wind2, Sources_solar1, on='Date')

plt.plot(Filtered_sources['Date'], Filtered_sources['Solar Gen'], label='Solar generation')
plt.plot(Filtered_sources['Date'], Filtered_sources['Hydro Gen'],  label='Hydro gneration')
plt.plot(Filtered_sources2['Date'], Filtered_sources2['Wind Gen'], label='Wind generation')
plt.xlabel('Date')
plt.ylabel('Generation in MWh')
plt.title('Generation by sources')
plt.legend()
plt.show()


data4 = S_Data2.loc[:, ['RENEWABLE_perc']]
window_size1 = 25

Renew_perc = moving_average(data4, window_size1)

 
Renew_perc1 = pd.DataFrame(Renew_perc)

Renew_perc1= Renew_perc1.rename(columns={0:'Renew %'})

renew_start =pd.to_datetime('2009-01-01 00:00:00')
renew_end = pd.to_datetime('2022-12-31 00:00:00')
interval = pd.Timedelta(minutes=30)

Renew_perc1["Date"] = pd.DataFrame({'Date': pd.date_range(start=hydro_start, end=hydro_end, freq=interval)})

sn.lineplot(data = Renew_perc1, x='Date', y='Renew %')
plt.xlabel('Date')
plt.ylabel('Generation % in Mwh')
plt.title('Filtered Renewable %')
plt.show()


conda update anaconda
conda install spyder=5.4.3

