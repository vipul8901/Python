# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 07:27:16 2020

@author: Vipul
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from urllib.request import urlopen as uReq

myurl='https://www.timeanddate.com/worldclock/distances.html?n=665'

uClient=uReq(myurl)
page_html=uClient.read()
uClient.close()

page_soup=BeautifulSoup(page_html,'html.parser')

container=page_soup.find_all("table",{"class":"zebra fw tb-wc"})

row_container=container[0].find_all("tr")

#col_container=row_container[2].find_all("td")
col_container=row_container[6].find_all("td")

name_container=col_container[0].find_all("a")

print(name_container[0].text)
print(col_container[1].text)
print(col_container[2].text)
print(col_container[3].text)
print(col_container[4].text)
print(col_container[5].text)




"""driver = webdriver.Chrome("C:\Users\Vipul\Downloads\chromedriver")"""