#!/usr/bin/env python
# coding: utf-8

# In[25]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URLji = "http://www.jlbank.com.cn/eportal/ui?moduleId=3&pageId=362341&struts.portlet.action=/portlet/mapFront!getMapDotDataSelectList.action"
data = {"currentPageNo": 1,
        "queryInfo": "",
        "regionRadio": "7752661a3da146e2a42ae1840667520f",
        "containsRegionRadio": "yes",
        "categoryRadio": "31b56c21f67647c48a1437bd4f6ac245",
        "containsCategoryRadio": "yes",
        "oneHidden": "1d8690409c704a68936c13a10d225091",
        "twoHidden": "all",
        "categoryHidden": "0a3dbee2688f4b85aab658392bdec8a3"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(URLji, data = data, headers = headers)
resp.json()


# In[26]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","province"])
bankji = resp.json()['result']
for i in range(1,62):
    dataji = {"currentPageNo": i,
        "queryInfo": "",
        "regionRadio": "7752661a3da146e2a42ae1840667520f",
        "containsRegionRadio": "yes",
        "categoryRadio": "31b56c21f67647c48a1437bd4f6ac245",
        "containsCategoryRadio": "yes",
        "oneHidden": "1d8690409c704a68936c13a10d225091",
        "twoHidden": "all",
        "categoryHidden": "0a3dbee2688f4b85aab658392bdec8a3"}
    respji = requests.post(URLji, data = dataji, headers = headers)
    bankji = respji.json()['result']
    for ji in bankji:
        dataframe.loc[len(dataframe), :] = [ji['dotName'],ji['dotAddress'],ji['dotPhone'],ji['dotDimension'],ji['dotLongitude'],ji['id'],"吉林省"]
    print(i)
        


# In[29]:


URLliao = "http://www.jlbank.com.cn/eportal/ui?moduleId=3&pageId=362341&struts.portlet.action=/portlet/mapFront!getMapDotDataSelectList.action"
for j in range(1,4):
    dataliao = {"currentPageNo": j,
        "queryInfo": "",
        "regionRadio": "7752661a3da146e2a42ae1840667520f",
        "containsRegionRadio": "yes",
        "categoryRadio": "31b56c21f67647c48a1437bd4f6ac245",
        "containsCategoryRadio": "yes",
        "oneHidden": "011654ae7398420bb644db9513b9fcdb",
        "twoHidden": "all",
        "categoryHidden": "0a3dbee2688f4b85aab658392bdec8a3"}
    respliao = requests.post(URLliao, data = dataliao, headers = headers)
    bankliao = respliao.json()['result']
    for liao in bankliao:
        dataframe.loc[len(dataframe), :] = [liao['dotName'],liao['dotAddress'],liao['dotPhone'],liao['dotDimension'],liao['dotLongitude'],liao['id'],"辽宁省"]
    print(j)
        


# In[30]:


dataframe


# In[31]:


dataframe.drop_duplicates('name').to_excel('./吉林银行网点数据.xlsx', index=False)


# In[ ]:




