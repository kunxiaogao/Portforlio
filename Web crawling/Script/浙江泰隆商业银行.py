#!/usr/bin/env python
# coding: utf-8

# In[5]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
url = "http://www.zjtlcb.com/eportal/ui?moduleId=3&pageId=364324&struts.portlet.action=/portlet/mapFront!getMapDotDataSelectList.action" #POST
data = {"currentPageNo": 67,
        "queryInfo": "",
        "regionRadio": "cf1a31fefc4a4377bcca08948ae7d176",
        "containsRegionRadio": "yes",
        "categoryRadio": "d461be9c619349faa0c5d8778ed32284",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(url,data =data, headers = headers)


# In[7]:


resp.json()['result']


# In[8]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for i in range(1,68):
    data = {"currentPageNo": i,
        "queryInfo": "",
        "regionRadio": "cf1a31fefc4a4377bcca08948ae7d176",
        "containsRegionRadio": "yes",
        "categoryRadio": "d461be9c619349faa0c5d8778ed32284",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}
    resp = requests.post(url,data =data, headers = headers)
    bank = resp.json()['result']
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['dotName'],j['dotAddress'],j['dotPhone'],j['dotDimension'],j['dotLongitude'],j['id']]
    print(i)    


# In[9]:


dataframe


# In[10]:


dataframe.drop_duplicates('name').to_excel('./浙江泰隆商业银行网点数据.xlsx', index=False)


# In[ ]:




