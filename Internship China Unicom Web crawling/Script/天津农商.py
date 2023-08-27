#!/usr/bin/env python
# coding: utf-8

# In[3]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL1 = "http://www.trcbank.com.cn/2010/6-26/15415570994.html" #GET
resp = requests.get(URL1)
resp.encoding = resp.apparent_encoding


# In[29]:


tree1 = etree.HTML(resp.text)
href = tree1.xpath('//div[@class= "area"]//a/@href')


# In[52]:


dataframe = pd.DataFrame(columns=["name", "address", "tel"])
for i in href:
    url = "http://www.trcbank.com.cn" + i
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    a = etree.HTML(r.text).xpath('//table//tr/td/text()')
    name = etree.HTML(r.text).xpath('//table//tr/td[1]/text()')
    n = [j for j in name if j.strip('\r\n').strip('\r\n        ')]
    address = etree.HTML(r.text).xpath('//table//tr/td[2]/text()')
    ad = [k for k in address if k.strip('\r\n').strip('\r\n        ')]
    tel = etree.HTML(r.text).xpath('//table//tr/td[3]/text()')
    t = [n for n in tel if n.strip('\r\n').strip('\r\n        ')]
    start = len(dataframe)
    count = start
    for N in n:
        dataframe.loc[count,"name"] = N
        count += 1
    count = start
    for A in ad:
        dataframe.loc[count,"address"] = A
        count += 1
    count = start
    for T in t:
        dataframe.loc[count,"tel"] = T
        count += 1
    print(i)


# In[47]:


r = requests.get("http://www.trcbank.com.cn/2010/6-26/15420551207.html")
r.encoding = r.apparent_encoding
a = etree.HTML(r.text).xpath('//table//tr/td[3]/text()')


# In[48]:


[j for j in a if j.strip('\r\n').strip('\r\n        ')]


# In[40]:


r.text


# In[53]:


dataframe


# In[55]:


dataframe.drop_duplicates('name').to_excel('./天津农商银行网点数据.xlsx', index=False)


# In[ ]:




