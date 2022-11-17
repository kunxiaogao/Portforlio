#!/usr/bin/env python
# coding: utf-8

# In[36]:


from urllib.parse import unquote
from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.bankcomm.com/BankCommSite/zonghang/cn/node/queryBranchResult.do"
data = {"urlType": "",
"city": "深圳",
"countyName": ""}
resp = requests.post(URL,data = data)
json.loads(resp.text.strip('\r\n\r\n'))['data'].values()


# In[27]:


URL1 = "http://www.bankcomm.com/BankCommSite/zonghang/cn/node/queryCityResult.do" #POST
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp1 = requests.post(URL1,headers = headers).json()[ 'citys']
a = []
resp1


# In[59]:


a = []
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","city"])
for i in resp1.values():
    a.append(i)
for j in a:
    for k in j.values():
        resp = requests.post(URL,data = {"urlType": "",
               "city": k['d'],
               "countyName": ""})
        result = json.loads(resp.text.strip('\r\n\r\n'))['data']
        print(k['d'])
        for bank in result.values():
            data.loc[len(data), :] = [bank["n"],unquote(bank["a"]),unquote(bank["p"]),bank["y"],bank["x"],bank["i"],k['d']]
data.loc[1509]["address"] = "常熟市世茂世纪中心-创富世纪5幢107室"
data.drop_duplicates('name').to_excel('./交通银行网点数据.xlsx', index=False)           


# In[48]:





# In[43]:





# In[58]:





# In[56]:





# In[57]:


unquote("0558-2708898%EF%BC%88%E5%8F%AF%E5%90%91%E5%AE%A2%E6%88%B7%E6%8F%90%E4%BE%9B%EF%BC%89")


# In[ ]:




