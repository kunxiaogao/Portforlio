#!/usr/bin/env python
# coding: utf-8

# In[6]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
url = 'https://www.bosc.cn/apiQry/apiPCQry/qryMcdept?size=4&current={}'
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","city","zone"])
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
for i in range(1,88):
    URL = url.format(i)
    rsp = requests.get(URL,headers = headers)
    banks = rsp.json()['data']['records']
    for bank in banks:
        data.loc[len(data), :] = [bank['deptName'],bank['deptAddr'],bank['tel'],bank['latitude'],bank['longitude'],bank['cityName'],bank['regionName']]
    print(i)
data


# In[2]:


rsp = requests.get('https://www.bosc.cn/apiQry/apiPCQry/qryMcdept?size=4&current=1',headers = headers)
print(rsp.json())


# In[7]:


data.drop_duplicates('name').to_excel('./上海银行网点数据.xlsx', index=False)


# In[ ]:




