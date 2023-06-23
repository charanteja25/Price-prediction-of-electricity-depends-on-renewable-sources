# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 19:00:35 2023

@author: paulo
"""

import pandas as pd

# Read datasets into DataFrames
MID_2014=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2014.xlsx")

MID_2015=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2015.xlsx")

MID_2016=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2016.xlsx")

MID_2017=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2017.xlsx")

MID_2018=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2018.xlsx")

MID_2019=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2019.xlsx")

MID_2020=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2020.xlsx")

MID_2021=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2021.xlsx")

MID_2022=pd.read_excel(r"C:\Users\paulo\Downloads\Final_Project\Final_Project\.spyproject\Codes\MID\MID_2022.xlsx")

MID_2014.info()

merged_MID.head()

# Merge DataFrames based on a common column
merged_MID = pd.merge(MID_2014, MID_2015, on=('Settlement Date','Market Index Data Provider Id','Market Index Volume (MWh)','Market Index Price (£/MWh)'))
