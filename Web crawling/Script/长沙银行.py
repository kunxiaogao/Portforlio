#!/usr/bin/env python
# coding: utf-8

# In[27]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
url = "http://www.cscb.cn/portal-frontend/branch/map/getAllBranches?_1624516725323" #POST
data = {"cpoint": "116.40387397,39.91488908",
        "kind": "",
        "keyword": "",
        "pageIndex": 3,
        "pageSize": "5"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(url,data = data, headers = headers)


# In[28]:


resp.json()['data']


# In[23]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","type"])
for i in range(1,64):
    data = {"cpoint": "116.40387397,39.91488908",
        "kind": "",
        "keyword": "",
        "pageIndex": i,
        "pageSize": "5"}
    resp = requests.post(url,data = data, headers = headers)
    bank = resp.json()['data']
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['name'],j['address'],j['telephone'],j['pointY'],j['pointX'],j['id'],j['kind']]
    print(i) 


# In[24]:


dataframe.drop_duplicates('name').to_excel('./长沙银行网点数据.xlsx', index=False)


# In[15]:





# In[ ]:




