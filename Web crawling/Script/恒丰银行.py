#!/usr/bin/env python
# coding: utf-8

# In[2]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
url = "https://www.hfbank.com.cn/ucms/OutletsServlet" #POST
data = {"methodType": "getPageData",
        "city": "10759",
        "outletsType": "outlets",
        "pageSize": "200",
        "pageIndex": "0"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(url,data = data,headers = headers)


# In[12]:


resp.json()['rows']


# In[14]:


URL1 = "https://www.hfbank.com.cn/gyhf/fwwd/index.shtml" #GET
resp1 = requests.get(URL1,headers=headers)
resp1.encoding = resp1.apparent_encoding
tree = etree.HTML(resp1.text)
text = tree.xpath('//div[@class="bankBranchBox"]//a/@id')


# In[11]:


re.findall('\d+','cityA_10750')


# In[15]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for i in text:
    code = re.findall('\d+',i)
    data = {"methodType": "getPageData",
        "city": code,
        "outletsType": "outlets",
        "pageSize": "200",
        "pageIndex": "0"}
    resp = requests.post(url,data = data,headers = headers)
    bank = resp.json()['rows']
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['title'],j['address'],j['tel'],j['latitude'],j['longitude'],j['id']]
    print(i) 
dataframe.drop_duplicates('name').to_excel('./恒丰银行网点数据.xlsx', index=False)        


# In[16]:


dataframe


# In[ ]:




