#!/usr/bin/env python
# coding: utf-8

# In[11]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.zybank.com.cn/eportal/ui?moduleId=3&pageId=364659&portal.url=/portlet/mapFront!getMapDotDataSelectList.portlet"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for i in range(1,143):
    data = {"currentPageNo": i,
        "queryInfo": "",
        "regionRadio": "-1",
        "containsRegionRadio": "yes",
        "categoryRadio": "",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}  
    resp = requests.post(URL,data = data,headers = headers)
    bank = resp.json()['result']
    print(i)
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['dotName'],j['dotAddress'],j['dotPhone'],j['dotDimension'],j['dotLongitude'],j['id']]
dataframe.drop_duplicates('name').to_excel('./中原银行网点数据.xlsx', index=False)  


# In[14]:


dataframe.drop_duplicates('name').to_excel('./中原银行网点数据.xlsx', index=False)


# In[12]:


dataframe


# In[13]:


dataframe.to_excel('./中原银行网点数据不去重.xlsx', index=False)  


# In[17]:


data = {"currentPageNo": 150,
        "queryInfo": "",
        "regionRadio": "-1",
        "containsRegionRadio": "yes",
        "categoryRadio": "",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}  
resp = requests.post(URL,data = data,headers = headers)
bank = resp.json()['result']


# In[16]:


bank


# In[ ]:




