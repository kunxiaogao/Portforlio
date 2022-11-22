#!/usr/bin/env python
# coding: utf-8

# In[29]:


import requests
from lxml import etree
import json
import re
import pandas as pd
import openpyxl
URL = "https://www.cqrcb.com/cqrcb/aboutus/networkinformation/index.html" #GET
resp1 = requests.get(URL, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"})
resp1.encoding = resp1.apparent_encoding
print(resp1.text)
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","City","Zone"])
text_lst = re.findall(r'{"BankName":.*\s+.*?}',resp1.text)
for i in text_lst:
    a = json.loads(i)
    data.loc[len(data), :] = [a['Name'],a['Address'],a['Tel'],a['Y'],a['X'],len(data)+1,a['City'],a['BankName']]
    print(a['Name'])
data.to_excel('./重庆农村商业银行网点数据.xlsx', index=False)    


# In[27]:


json.loads('{"BankName":"璧山县","Address":"重庆市璧山县璧城街道办事处璧铜路4号","Service":"","City":"重庆市","Pro":"重庆市","Env":"",\r\n\t"Name":"重庆农村商业银行股份有限公司璧山支行","WorkTime":"","Type":"0","MapSeq":1,"X":"106.236756","Y":"29.600111","Tel":""}')


# In[ ]:




