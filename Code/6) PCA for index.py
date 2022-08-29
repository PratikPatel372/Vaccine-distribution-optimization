# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:25:54 2022

@author: Pratik
"""

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler,MinMaxScaler,minmax_scale
import matplotlib.pyplot as plt
from numpy import asarray

path = r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"
Diseases_2022 = pd.read_csv(path+"/All Diseases Final(2022)(No of people).csv")

#Scaling the data before using PCA
scalar = StandardScaler()   
scaled = pd.DataFrame(scalar.fit_transform(Diseases_2022[["Diabetes","Asthma","Thyroid"]]),columns=["Diabetes","Asthma","Thyroid"])

#Principle Component Analysis
pca =PCA(n_components=3)
df_pca = pd.DataFrame(pca.fit_transform(scaled),columns=["1st","2nd","3rd"])
df_pca.insert(0, "States", Diseases_2022["States"])

explained_variance = pca.explained_variance_ratio_

pd.DataFrame(pca.explained_variance_ratio_).plot.bar()
plt.xlabel('Principal Components')
plt.ylabel('Explained Varience')

c_index = df_pca[["States","1st"]]
c_index["1st"] = minmax_scale(c_index["1st"], feature_range=(1, 10), axis=0, copy=True)
#c_index["1st"] = MinMaxScaler().fit_transform(pd.DataFrame(c_index["1st"]))
c_index.to_csv(path+"/Comorbidity Index.csv",index = False)
df_pca.to_csv(path+"/Com Index.csv",index = False)


