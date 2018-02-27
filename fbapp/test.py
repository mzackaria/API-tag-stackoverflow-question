# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:56:42 2018

@author: zakis
"""
import pandas as pd
import numpy as np

result = pd.read_csv('tuto_/result_films.csv', encoding = "ISO-8859-1")


for i in range(0,len(result.values)):
    ident = result.iloc[i,0].astype(int)
    cluster = result.iloc[i,1].astype(int)
    title = result.iloc[i,2]
