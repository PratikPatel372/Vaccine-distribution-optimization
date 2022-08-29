# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:34:57 2022

@author: Pratik
"""

import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer # import the KNNimputer class
from scipy import interpolate

path = r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"

#..............1) KNN Imputer..........
Before_imputation = pd.read_csv(path + "/All Diseases Final(2005-06)(No of people).csv")

imputer = KNNImputer(n_neighbors=2)
After_imputation = imputer.fit_transform(Before_imputation.iloc[:,1:4])
pd.DataFrame(After_imputation).to_csv(path+'/wrong_KNN(2005-06)(No of people)(WM).csv',index=False)


#..............2) Linear Interpolation.........
Before_imputation = pd.read_csv(path + "/All Diseases Final(2005-06)(No of people).csv")

def missing_value(input_file):
    train_data = input_file[~input_file['Diabetes'].isnull()]
    missing_data = input_file[input_file['Diabetes'].isna()]

    train_x = train_data["pop"]
    missing_x = missing_data["pop"]
    for i in range(1,4):
        train_y = train_data.iloc[:,i]
        f = interpolate.interp1d(train_x, train_y, fill_value='extrapolate')
        
        missing_data.iloc[:,i] = f(missing_x).astype(int)
        print(f(missing_x).astype(int))
        
    df = train_data.append(missing_data)
    
    df = df.sort_values(by=['States'], ascending=True)

    return df

after_imputation = missing_value(Before_imputation)
after_imputation.to_csv(path+'/All Diseases Final(2005-06)(No of people)(WM).csv',index=False)

for i in range(1,4):
    after_imputation[after_imputation.columns[i]] = after_imputation[after_imputation.columns[i]] / after_imputation["pop"]

after_imputation.to_csv(path+'/All Diseases Final(2005-06)(% of people)(WM).csv',index=False)






