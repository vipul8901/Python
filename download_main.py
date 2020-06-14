# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 05:54:04 2020

@author: Vipul
"""

import pandas as pd

df = pd.read_csv('https://query.data.world/s/hvfxiyuxjhhh2rsulv2c7d4wibtqjq')
df["Latest_Date"]=pd.to_datetime(df.Date).max()
df.to_csv(r'C:\Users\Vipul\Downloads\Tableau_data\data\COVID-19 Cases deaths.csv')