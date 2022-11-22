#!/usr/bin/env python
# coding: utf-8

# In[2]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.bankofbeijing.com.cn/contents/340/28317.html" #GET
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.get(URL,headers = headers)
resp.encoding = resp.apparent_encoding
tree = etree.HTML(resp.text)
name = tree.xpath('//tr[2]/td[1]/text()')
address = tree.xpath('//tr/td[2]/text()')
tel = tree.xpath('//tr/td[3]/text()')
name[0]


# In[17]:


re.sub('[\r\n\t]','','\r\n\r\n\t\t\t\t89756452、89756407')


# In[48]:


URL1 = "http://www.bankofbeijing.com.cn/branch/index.html"
resp1 = requests.get(URL1,headers = headers)
resp1.encoding = resp1.apparent_encoding
tree1 = etree.HTML(resp1.text)
city = tree1.xpath('//div[@class="title_in f_000_12"]//a/@href')
dataframe = pd.DataFrame(columns=["name", "address", "tel"])
for i in city:
    URL = "http://www.bankofbeijing.com.cn" + i
    resp = requests.get(URL,headers = headers)
    resp.encoding = resp.apparent_encoding
    tree = etree.HTML(resp.text)
    name = tree.xpath('//tr/td[1]/text()')[1:]
    address = tree.xpath('//tr/td[2]/text()')
    tel = tree.xpath('//tr/td[3]/text()')
    start = len(dataframe)
    count = start
    for n in name:
        N = re.sub('[\r\n\t]','',n)
        dataframe.loc[count,"name"] = N
        count += 1
    count = start
    for a in address:
        A = re.sub('[\r\n\t]','',a)
        dataframe.loc[count,"address"] = A
        count += 1
    count = start
    for t in tel:
        T = re.sub('[\r\n\t]','',t)
        dataframe.loc[count,"tel"] = T
        count += 1
    print(i)


# In[30]:





# In[32]:


dataframe = pd.DataFrame(columns=["name", "address", "tel"])


# In[50]:


dataframe.drop_duplicates('name').to_excel('./北京银行网点数据.xlsx', index=False) 


# In[ ]:




