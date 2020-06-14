# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 07:39:42 2020

@author: Vipul
"""


from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen 
from urllib.request import Request

myurl='https://www.worldometers.info/coronavirus/'
headers = {'User-Agent': 'Chrome/41.0.2228.0'}
req=Request(url=myurl, headers=headers)

uClient=urlopen(req)
page_html=uClient.read()
uClient.close()

page_soup=BeautifulSoup(page_html,'html.parser')

container=page_soup.find_all("table",{"id":"main_table_countries_today"})

"""row_container=container[0].find_all("tr")
col_container=row_container[1].find_all("td")
print(col_container[0].text)
print(col_container[3].text)
print(col_container[5].text)
print(col_container[7].text)
print(col_container[10].text)"""



i=0
Country_Region=[]
Deaths=[]
Recovered=[]
Serious_critical=[]
Tests=[]

for row_container in container[0].find_all("tr"):
    i=i+1
    print(i)
    if i>1 :
        col_container=row_container.find_all("td")
        
        """Country_Region.append(col_container[0].text)
        Deaths.append(col_container[3].text)
        Recovered.append(col_container[5].text)
        Serious_critical.append(col_container[7].text)
        Tests.append(col_container[10].text)"""
        
        
        Country_Region.append(col_container[1].text)
        Deaths.append(col_container[4].text)
        Recovered.append(col_container[6].text)
        Serious_critical.append(col_container[9].text)
        Tests.append(col_container[12].text)
       
        
      
        
df_tests=pd.DataFrame({"Country_Region":Country_Region,"Deaths":Deaths 
                         ,"Recovered":Recovered,"Serious_critical":Serious_critical
                        ,"Tests":Tests})

df_tests.to_csv(r'C:\Users\Vipul\Downloads\Tableau_data\data\tests.csv')


#df_pop.to_csv(r'C:\Users\Vipul\Downloads\Tableau_data\world_population.csv')
