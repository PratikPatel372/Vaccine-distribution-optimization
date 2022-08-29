# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 14:10:31 2022

@author: Pratik
"""
import requests, json
import pandas as pd
import numpy as np
import geopy.distance

path=r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"

coord = pd.read_csv(path+'/India Coordinates.csv')
states = list(coord['States'])

Key = "AkKE31Tnn-RfIc3gAP3CGhfulk3QCYcovk3ayERz8pnmYtl-VlBZmCQNpE4I42Ve"
url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?"
start = ';'.join(list(coord["Coordinates"]))
dest  = ';'.join(list(coord["Coordinates"]))

r = requests.get(url + "origins=" + start + "&destinations=" + dest + 
                 "&travelMode=driving&o=json&key=" + Key +"&distanceUnit=km")
json_data=r.json()

dist = pd.DataFrame.from_dict(json_data.get('resourceSets')[0].get('resources')[0].get('results'))

DistanceMatrix = np.zeros((36,36))

k=0
print(len(dist["travelDistance"]))

for i in range(36):
    for j in range(36):
        DistanceMatrix[i][j] = round(dist["travelDistance"][k],0)
        k+=1
coords_1 = [coord["Coordinates"][0],coord["Coordinates"][18]]
coords_2 = coord["Coordinates"][0:]
      
for i in range(36):
    temp = geopy.distance.geodesic(coords_1[0], coords_2[i]).km
    DistanceMatrix[0][i] = round(temp,0)
    DistanceMatrix[i][0] = round(temp,0)
    temp2 = geopy.distance.geodesic(coords_1[1], coords_2[i]).km
    DistanceMatrix[18][i] = round(temp2,0)
    DistanceMatrix[i][18] = round(temp2,0)

Distance_Matrix = pd.DataFrame(DistanceMatrix,columns=states)
Distance_Matrix.insert(0, column="States", value=states)

Distance_Matrix.to_csv(path + "/India Distance matrix.csv",index=False)

#..........................................................................FOR USA.......................................................
import requests, json
import pandas as pd
import numpy as np
import geopy.distance

path=r"C:\Users\Pratik\Desktop\IIT KGP\Information System Project (IM69004)\Dataset"

coord = pd.read_csv(path+'/USA Coordinates.csv')
states = list(coord['States'])

Key = "AkKE31Tnn-RfIc3gAP3CGhfulk3QCYcovk3ayERz8pnmYtl-VlBZmCQNpE4I42Ve"
url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix?"
start = ';'.join(list(coord["Coordinates"]))
dest  = ';'.join(list(coord["Coordinates"]))

r = requests.get(url + "origins=" + start + "&destinations=" + dest + 
                 "&travelMode=driving&o=json&key=" + Key +"&distanceUnit=km")
json_data=r.json()

dist = pd.DataFrame.from_dict(json_data.get('resourceSets')[0].get('resources')[0].get('results'))

DistanceMatrix = np.zeros((50,50))

k=0
print(len(dist["travelDistance"]))

for i in range(50):
    for j in range(50):
        DistanceMatrix[i][j] = round(dist["travelDistance"][k],0)
        k+=1

coords_1 = [coord["Coordinates"][1],coord["Coordinates"][10]]
coords_2 = coord["Coordinates"][0:]
      
for i in range(50):
    temp = geopy.distance.geodesic(coords_1[0], coords_2[i]).km
    DistanceMatrix[1][i] = round(temp,0)
    DistanceMatrix[i][1] = round(temp,0)
    temp2 = geopy.distance.geodesic(coords_1[1], coords_2[i]).km
    DistanceMatrix[10][i] = round(temp2,0)
    DistanceMatrix[i][10] = round(temp2,0)
        
Distance_Matrix = pd.DataFrame(DistanceMatrix,columns=states)
Distance_Matrix.insert(0, column="States", value=states)

Distance_Matrix.to_csv(path + "/USA Distance matrix.csv",index=False)



