# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 02:02:34 2023

@author: paulo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import minmax_scale, normalize
import seaborn as sn
%matplotlib inline

MID_2021=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2021.xlsx")

MID_2021_2 = MID_2021.drop(MID_2021[MID_2021['Market Index Data Provider Id'] == 'N2EXMIDP'].index)

MID_2021_2['Settlement Date']

""" Transforming the time stamp """

# Create a DataFrame with a column of 30-minute intervals

MID_2021_2['Settlement Date'] = pd.to_datetime(MID_2021['Settlement Date']).dt.date

date_range = pd.date_range('2021-01-01','2022-01-01', freq='30min')

Date=pd.DataFrame(date_range)

# Creating a dataframe with the date column
MID_2021_2['Date'] = pd.DataFrame({'Timestamp': date_range})

MID_2021_2.info()


sn.lineplot(data =MID_2021_2, x='Date', y='Market Index Price (£/MWh)')
plt.xlabel('Date')
plt.ylabel('Market Index Price (£/MWh)')
plt.show()