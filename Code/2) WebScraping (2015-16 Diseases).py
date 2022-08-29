# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 20:22:43 2022

@author: Pratik
"""
#....................................................ALL Comorbidities.............................................................
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

out_path="C:/Users/Pratik/Desktop/IIT KGP/Information System Project (IM69004)/Dataset"
col=['Sl.No.','States','% Women_Diabetes','% Women_Asthma','% Women_Thyroid','% Women_Heart_Diseases','% Women_Cancer','% Men_Diabetes','% Men_Asthma','% Men_Thyroid','% Men_Heart_Diseases','% Men_Cancer']

xpath ="/html/body/div/div[1]/div/div[7]/div[2]/div/section/div/div/div/div/div/div/div[2]/div[3]/h3/a"

op = webdriver.ChromeOptions()
op.add_argument('--ignore-certificate-errors')

driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"),options=op)
driver.maximize_window()
time.sleep(2)

try:
    driver.get("https://data.gov.in/")
    time.sleep(2)

    #search for diabetes datasets
    search = driver.find_element(By.NAME,"text")
    search.send_keys("Diabetes Asthma NFHS 4")
    search.send_keys(Keys.RETURN)
    
    #select the Particular data
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,xpath)))
    element.click() 
        
    #select the xls format
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"xls")))
    element.click() 
        
    #select non-commarcial option
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/form/div/div[4]/div/div[2]/label/div")))
    element.click()
    
    #Select purpose
    purpose = driver.find_element(By.XPATH,"/html/body/div[2]/div/form/div/div[5]/div/div[1]/label")
    purpose.click()
        
    #Enter name
    name = driver.find_element(By.ID,"edit-name-d")
    name.send_keys("PRATIK")
        
    #Enter mailID
    mail = driver.find_element(By.ID,"edit-mail-d")
    mail.send_keys("pratikakbari372@gmail.com")
    
    #Enter submit
    submit = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit-submit")))
    submit.click()
    time.sleep(10)
    
    #Get downloaded data
    df = pd.read_excel("C:/Users/Pratik/Downloads/datafile.xls",skiprows=[1],names=col).drop(['Sl.No.'], axis=1)
    
    #Add Hypertension data
    hyper = pd.read_csv(out_path + '/Hypertension.csv')
    df.insert(6,"% Women_Hypertension",hyper["% Women_Hypertension"])
    df.insert(12,"% Men_Hypertension",hyper["% Men_Hypertension"])
    
    #Sorting by "States" Alphabatically
    df = df.sort_values(by=['States'], ascending=True)
    #df.reset_index(inplace = True,drop =True)

    #Final Save as "All Diseases(2015-16).csv"
    df.to_csv(out_path + '/All Diseases(2015-16).csv', index=False)
    os.remove("C:/Users/Pratik/Downloads/datafile.xls")
    print('All Diseases(2015-16).csv saved')
    

except:
    driver.quit()
        
    
    
