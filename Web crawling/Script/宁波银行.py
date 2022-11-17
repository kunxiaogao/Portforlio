#!/usr/bin/env python
# coding: utf-8

# In[14]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.nbcb.com.cn/query_business_site/business_site.json?_=" #GET
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.get(URL,headers = headers)


# In[15]:


resp.encoding = resp.apparent_encoding


# In[24]:


lst = resp.json()['businessSiteItem']
lst = lst[:-1]


# In[26]:


data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","city","type"])
for i in lst:
    data.loc[len(data), :] = [i['businessSiteName'],i['address'],i['phone'],i['latitude'],i['longitude'],i['viewDataId'],i['city'],i['businessSiteType']]
    print(i['businessSiteName'],i['businessSiteType'],i['viewDataId'])
data.drop_duplicates(['name','type']).to_excel('./宁波银行网点数据.xlsx', index=False)


# In[27]:


data.drop_duplicates(['name','type']).to_excel('./宁波银行网点数据.xlsx', index=False) 


# In[ ]:




