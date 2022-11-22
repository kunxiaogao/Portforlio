#!/usr/bin/env python
# coding: utf-8

# In[137]:


from urllib.parse import unquote
from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.hsbank.com.cn/Channel/11902" #GET
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.get(URL,headers = headers)
tree = etree.HTML(resp.text)
tel = tree.xpath('//table//table//table//tr/td[last()-1]/text()')
address = tree.xpath('//table//table//table//tr/td[last()-2]//text()')
name = tree.xpath('//table//table//table//tr/td[last()-3]//text()')
[k for k in name if k.strip('\n\r\xa0')]
address 


# In[93]:


name[1] == '\r\n'


# In[110]:


URL1 = "http://www.hsbank.com.cn/Channel/665836" #GET
URL2 = "http://www.hsbank.com.cn"
resp1 = requests.get(URL1,headers = headers)
tree1 = etree.HTML(resp1.text)
href = tree1.xpath('//map/area/@href')[:-1]
for i in href:
    url = i
    r = requests.get(url)
    t = etree.HTML(r.text)
    h = t.xpath('//table//td[@align="center"]//a/@href')[-8]
    URL2 = "http://www.hsbank.com.cn" + h
    


# In[109]:


url = "http://www.hsbank.com.cn/Channel/12118"
r = requests.get(url)
t = etree.HTML(r.text)
h = t.xpath('//table//td[@align="center"]//a/@href')[-8:-6]


# In[87]:


a


# In[90]:


name


# In[ ]:




