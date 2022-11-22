#!/usr/bin/env python
# coding: utf-8

# In[9]:





# In[1]:


import requests
import pandas as pd
import json
from lxml import etree
import re
import openpyxl
URL1 = "http://app.abchina.com/branch/common/BranchService.svc/District" # 所有城市码 GET
resp1 = requests.get(URL1).json()
city_code = []
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","city"])
a = 1
for i in resp1:
    city_code.append(i['Id'])
URL2 = "http://app.abchina.com/branch/common/BranchService.svc/Branch?p={}&c=-1&b=-1&t=1&z=0&i={}"
for code in city_code:
    page = 0
    resp2 = requests.get(URL2.format(code,page)).json()["BranchSearchRests"]
    while resp2 != []:
        for j in resp2:
            data.loc[len(data), :] = [j["BranchBank"]["Name"], j["BranchBank"]["Address"], j["BranchBank"]["PhoneNumber"],
                                      j["BranchBank"]["Latitude"], j["BranchBank"]["Longitude"],j["BranchBank"]["BoroughId"],j["BranchBank"]["City"]]
            print(a)
            a += 1
        page += 1
        resp2 = requests.get(URL2.format(code, page)).json()["BranchSearchRests"]
    


# In[2]:


data


# In[3]:


data.drop_duplicates('name').to_excel('./中国农业银行网点数据.xlsx', index=False)   


# In[ ]:




