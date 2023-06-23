# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:55:16 2023

@author: paulo
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import minmax_scale, normalize
import seaborn as sn
%matplotlib inline

Demanda_Data=pd.read_csv(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\Historic Demand Data\demanddata_2019.csv")

Demanda_Data.info()

Demanda_Data2= Demanda_Data.loc[:, ['SETTLEMENT_DATE','TSD','EMBEDDED_SOLAR_GENERATION']]

Demanda_Data2['SETTLEMENT_DATE'] = pd.to_datetime(Demanda_Data2['SETTLEMENT_DATE']).dt.date

#Lineploting TSd vs Solar
sn.lineplot(data = Demanda_Data2, x='EMBEDDED_SOLAR_GENERATION', y='TSD')
plt.xlabel('EMBEDDED_SOLAR_GENERATION')
plt.ylabel('TSD')
plt.show()

#Lineploting TSd vs time
sn.lineplot(data = Demanda_Data2, x='SETTLEMENT_DATE', y='TSD')
plt.xlabel('SETTLEMENT_DATE')
plt.ylabel('TSD')
plt.show()

sn.lineplot(data = Demanda_Data2, x='SETTLEMENT_DATE', y='EMBEDDED_SOLAR_GENERATION')
plt.xlabel('SETTLEMENT_DATE')
plt.ylabel('EMBEDDED_SOLAR_GENERATION')
plt.show()