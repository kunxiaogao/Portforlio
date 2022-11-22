#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
from lxml import etree
import json
import re
import pandas as pd
import openpyxl
URL = "http://www.cebbank.com/eportal/ui?struts.portlet.action=/portlet/emapFront!queryEmapDotList.action&moduleId=12853&pageId=484657" #POST
data = {"keyword": "",
"cityId": "896443488a5f444a998a653f51625690"}
resp = requests.post(URL,data = data, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"})
resp.json()['dotList']


# In[14]:


data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","code","city"])
URL2 = "http://www.cebbank.com/eportal/ui?struts.portlet.action=/portlet/emapFront!getCityList.action&moduleId=12853"
resp2 = requests.get(URL2).json()['cityList']
for i in resp2.values():
    for k in i:
        ID = k["id"]
        CITY = k['name']
        bank = requests.post(URL, data = {"keyword": "","cityId": ID}, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()['dotList']
        print(CITY)
        for j in bank:
            data.loc[len(data), :] = [j['name'],j['address'],j['phone'],j['pointY'],j['pointX'],j['id'],CITY]
data.drop_duplicates('name').to_excel('./中国光大银行网点数据.xlsx', index=False)        


# In[13]:


URL2 = "http://www.cebbank.com/eportal/ui?struts.portlet.action=/portlet/emapFront!getCityList.action&moduleId=12853"
resp2 = requests.get(URL2).json()['cityList']
resp2


# In[ ]:




