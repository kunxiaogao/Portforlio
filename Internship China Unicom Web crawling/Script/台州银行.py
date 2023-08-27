#!/usr/bin/env python
# coding: utf-8

# In[74]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for Id in areaid:
    url = "http://www.tzbank.com/" + Id #GET
    resp = requests.get(url)
    a = resp.text
    lst = re.findall('AddPin\(.*?\)',a)[:-2]
    for i in lst:
        b = re.findall('\d+',i)
        lng = b[0]+'.'+b[1]
        lat = b[2]+'.'+b[3]
        c = re.findall('\'.*?\'',i)
        if c == []:
            c = re.findall('\'.*',i)
        d = re.sub('\'','',c[0])
        name = d.split(';')[0]
        address = d.split(';')[1]
        if len(d.split(';')) == 2:
            tel = "None" 
        elif len(d.split(';')) > 2:
            tel = d.split(';')[2].strip('\)')
        data.loc[len(data), :] = [name,address,tel,lat,lng,len(data)+1]
        print(name)
data.drop_duplicates('name').to_excel('./台州银行网点数据.xlsx', index=False) 


# In[35]:


URL1 = "http://www.tzbank.com/network-query.jsp" #GET
resp1 = requests.get(URL1)
tree = etree.HTML(resp1.text)
areaid = tree.xpath('//div[@class="addmap_list "]//li//a/@href')


# In[73]:


areaid


# In[69]:


url = "http://www.tzbank.com/network-query.jsp?&areaid=64" #GET
resp = requests.get(url)
a = resp.text
lst = re.findall('AddPin\(.*?\)',a)[:-2]
for i in lst:
    b = re.findall('\d+',i)
    lng = b[0]+'.'+b[1]
    lat = b[2]+'.'+b[3]
    c = re.findall('\'.*',i)
    d = re.sub('\'','',c[0])
    name = d.split(';')[0]
    address = d.split(';')[1]
    if len(d.split(';')) == 2:
        tel = "None" 
    elif len(d.split(';')) > 2:
        tel = d.split(';')[2].strip('\)')
    print(tel)


# In[75]:


data


# In[76]:


data.drop_duplicates('name').to_excel('./台州银行网点数据.xlsx', index=False)


# In[ ]:




