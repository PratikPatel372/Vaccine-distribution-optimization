    # -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:02:22 2022

@author: Pratik
"""

#.......................................Collect all Diseases(2015-16)...............................
import pandas as pd

path=r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"

All_Diseases = pd.read_csv(path+'/All Diseases(2015-16).csv')
Pop = pd.read_csv(path + '/Population_2021.csv')
col = ['States','Diabetes', 'Asthma', 'Thyroid','Heart_Diseases', 'Cancer', 'Hypertension']

Pop['Total(000)'] = Pop['Total(000)'].str.replace(',','').astype(float).astype(int)
Pop['Men(000)']   = Pop['Men(000)'].str.replace(',','').astype(float).astype(int)
Pop['Women(000)'] = Pop['Women(000)'].str.replace(',','').astype(float).astype(int)

for i in range(1,7):
    a = (All_Diseases[All_Diseases.columns[i]] * Pop['Women(000)']*10) + (All_Diseases[All_Diseases.columns[i+6]] * Pop['Men(000)']*10)
    All_Diseases[col[i]]= a.astype(int)
            
All_Diseases = All_Diseases.drop(['% Women_Diabetes', '% Women_Asthma', '% Women_Thyroid','% Women_Heart_Diseases', '% Women_Cancer', '% Women_Hypertension','% Men_Diabetes', '% Men_Asthma', '% Men_Thyroid','% Men_Heart_Diseases', '% Men_Cancer', '% Men_Hypertension'],axis=1)
All_Diseases['Cancer'][7]= 206
All_Diseases['Cancer'][9]= 25178
All_Diseases['Cancer'][29]= 445

All_Diseases.to_csv(path+'/All Diseases Final(2015-16)(No of people).csv',index=False)


#.......................................Collect all Diseases(2005-06)...............................
import numpy as np

All_Diseases1 = pd.read_csv(path+'/All Diseases(2005-06).csv')
Pop = pd.read_csv(path + '/Population_2021.csv')
col = ['States','Diabetes', 'Asthma', 'Thyroid']

Pop['Total(000)'] = Pop['Total(000)'].str.replace(',','').astype(float).astype(int)
Pop['Men(000)']   = Pop['Men(000)'].str.replace(',','').astype(float).astype(int)
Pop['Women(000)'] = Pop['Women(000)'].str.replace(',','').astype(float).astype(int)

for i in range(1,4):
    a = (All_Diseases1[All_Diseases1.columns[i]] * Pop['Women(000)']/100) + (All_Diseases1[All_Diseases1.columns[i+3]] * Pop['Men(000)']/100)
    All_Diseases1[col[i]]= a
            
All_Diseases1 = All_Diseases1.drop(['Diabetes_Women/100000', 'Asthma_Women/100000', 'Thyroid_Women/100000','Diabetes_Men/100000', 'Asthma_Men/100000', 'Thyroid_Men/100000'],axis=1)

for i in range(1,4):
    for j in range(36):
        if All_Diseases1[col[i]][j]!='nan':
            All_Diseases1[col[i]][j]=round(All_Diseases1[col[i]][j],0)
            
All_Diseases1.to_csv(path+'/All Diseases Final(2005-06)(No of people).csv',index=False)
