#!/usr/bin/env python
# coding: utf-8

# In[2]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
url = "https://www.qrcb.com.cn/eportal/ui?moduleId=3&pageId=1f3e292754f54fc6b18c421f87013954&portal.url=/portlet/map-portlet!getMapDotDataSelectList.portlet"
data = {"currentPageNo": 1,
        "queryInfo": "",
        "regionRadio": "3209ea37f0054366b44a899ef85375c6",
        "containsRegionRadio": "yes",
        "categoryRadio": "",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(url,data = data, headers = headers)


# In[5]:


resp.json()['result']


# In[6]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for i in range(1,61):
    data = {"currentPageNo": i,
        "queryInfo": "",
        "regionRadio": "3209ea37f0054366b44a899ef85375c6",
        "containsRegionRadio": "yes",
        "categoryRadio": "",
        "containsCategoryRadio": "yes",
        "oneHidden": "all",
        "categoryHidden": "all"}
    resp = requests.post(url,data = data, headers = headers)
    bank = resp.json()['result']
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['dotName'],j['dotAddress'],j['dotPhone'],j['dotDimension'],j['dotLongitude'],j['id']]
    print(i)  


# In[7]:


dataframe


# In[8]:


dataframe.drop_duplicates('name').to_excel('./青岛农村商业银行网点数据.xlsx', index=False)


# In[ ]:




