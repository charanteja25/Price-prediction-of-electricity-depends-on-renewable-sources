# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 23:06:42 2023

@author: paulo
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import minmax_scale, normalize
import seaborn as sn
%matplotlib inline



SBP=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\SSPSBPdata\SBP.xlsx")

SSP=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\SSPSBPdata\SSP.xlsx")

SBP = SBP.drop('Run', axis=1)

SBP.info()
SBP2= SBP.loc[:, ['SF','BM']]


SBP.columns()

#Lineploting SBP vs Time
sn.lineplot(data = SBP, x='Date', y='SBP Daily Average(£/Mwh)')
plt.xlabel('Date')
plt.ylabel('SBP Daily Average(£/Mwh)')
plt.show()

#Lineploting SSP vs Time
sn.lineplot(data = SSP, x='Date', y='SSP Daily Average (£/Mwh)')
plt.xlabel('Date')
plt.ylabel('SSP Daily Average (£/Mwh)')
plt.show()

SSP.boxplot()
SBP.boxplot()
  
