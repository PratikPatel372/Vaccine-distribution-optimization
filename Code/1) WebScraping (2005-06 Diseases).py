# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 14:38:17 2022

@author: Pratik
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

#............................................................INPUT GIVEN...............................................
Diseases=['Thyroid','Diabetes','Asthma']
xpath=['/html/body/div/div[1]/div/div[7]/div[2]/div/section/div/div/div/div/div/div/div[2]/div[4]/h3/a',
       '/html/body/div[1]/div[1]/div/div[7]/div[2]/div/section/div/div/div/div/div/div/div[2]/div[7]/h3/a',
       '/html/body/div/div[1]/div/div[7]/div[2]/div/section/div/div/div/div/div/div/div[2]/div[5]/h3/a']
out_path="C:/Users/Pratik/Desktop/IIT KGP/Information System Project (IM69004)/Dataset"
col=['Sl.No.','States','Women_Total/100000','Women_Rural/100000','Women_Urban/100000','Men_Total/100000','Men_Rural/100000','Men_Urban/100000']

op = webdriver.ChromeOptions()
#op.add_argument("--incognito")
op.add_argument('--ignore-certificate-errors')
#prefs = {"download.default_directory" : out_path};
#op.add_experimental_option("prefs",prefs);

driver = webdriver.Chrome(service=Service("C:/Program Files (x86)/chromedriver.exe"),options=op)
driver.maximize_window()
time.sleep(2)

def Data_collection(Die,link):
    try:
        driver.get("https://data.gov.in/")
        time.sleep(2)

        #search for diabetes datasets
        search = driver.find_element(By.NAME,"text")
        search.send_keys(Die[i])
        search.send_keys(Keys.RETURN)
        
        #select the Particular data
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,link[i])))
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
        time.sleep(5)
        
        df = pd.read_excel("C:/Users/Pratik/Downloads/datafile.xls",skiprows=[1],names=col)
        df.to_csv(out_path + '/' + Die[i] +'.csv', index=False)
        os.remove("C:/Users/Pratik/Downloads/datafile.xls")
        print(Die[i] +'.csv' + ' saved')
        
    except:
        driver.quit()
        
    return;
    
for i in range(len(Diseases)):
    Data_collection(Diseases, xpath);

print("all done")
driver.quit()

#os.rename("C:/Users/Pratik/Downloads/datafile.xls","C:/Users/Pratik/Downloads" + '/'+ Die[i]+'.xls')
       
    
    
    