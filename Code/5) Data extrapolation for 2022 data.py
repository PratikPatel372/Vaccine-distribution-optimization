# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 17:01:40 2022

@author: Pratik
"""

import pandas as pd
import matplotlib.pyplot as plt

path = r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"
data_2005 = pd.read_csv(path + "/All Diseases Final(2005-06)(No of people)(WM).csv")
data_2015 = pd.read_csv(path + "/All Diseases Final(2015-16)(No of people).csv")
data_2022 = pd.DataFrame()
data_2022[["States","Diabetes","Asthma","Thyroid"]] = data_2015["States"],0,0,0

#Linear extrapolation technique
#y = y1 + (x-x1)*((y2-y1)/(x2-x1))

x1 = 2005
x2 = 2015
x = 2022
for i in range(1,4): #Column
    for j in range(36):  #Row 
        y1 = data_2005.iloc[j,i]
        y2 = data_2015.iloc[j,i]
        data_2022.iloc[j,i] = (y1 + (x - x1)*((y2 - y1) / (x2 - x1))).astype(int)

data_2022["pop"] = data_2005["pop"]
data_2022.to_csv(path + "/All Diseases Final(2022)(No of people).csv",index =False)   
'''
plt.plot([x1,x2],[y1,y2],marker = 'o')
plt.plot([x2,x],[y2,data_2020["Diabetes"][0]],marker = 'o')
plt.show()
'''