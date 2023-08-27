#!/usr/bin/env python
# coding: utf-8

# In[7]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "https://www.cdrcb.com/map/cdnsmapdata.php" #POST
data = {"query_prov": "四川",
"query_city": "",
"query_area": "",
"query_type": "",
"query_key": "",
"query_page": "1"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(URL,data = data,headers = headers)


# In[29]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","city","zone"])
a = resp.text.strip('43|+|1|+|11')
b = re.sub('\'','\"',a)
c= re.sub('<br/>','","',b)
d = re.sub('地址： ','',c)
e = re.sub('电话： ','',d)
g = json.loads(e)
for i in g:
    dataframe.loc[len(dataframe), :] = [i[2],i[3],i[4],i[1],i[0],i[-1],i[7],i[8]]
    


# In[25]:


b = re.sub('\'','\"',"[104.0835,30.62023,'成都农商银行','地址： 成都市武侯区科华中路88号<br/>电话： 028-85357369','物理网点','四川','成都','武侯区',0]")
c= re.sub('<br/>','","',b)
json.loads(c)
c


# In[27]:


json.loads(e)


# In[30]:


data


# In[32]:


dataframe.drop_duplicates('name').to_excel('./成都农业银行网点数据.xlsx', index=False) 


# In[ ]:




