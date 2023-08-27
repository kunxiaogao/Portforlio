#!/usr/bin/env python
# coding: utf-8

# In[13]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
ULR = "http://www.jsbchina.cn/cms/ShowCityMap.do?MmEwMD=5m71P2AE_1o2WJoFSs7eZqwJPQ3qCkA95AO6gc7gkCHXKad7s8zOqh1tW2bpdPWw7.Wj0qo52nSOaJiFlxuE0w219epVLPka0.TEBdK_2eKDhWhU0ZLVKct8VOG0rMIEQk6Ztqf7aESkgc6s6rtlUC_exHM1gmXt3sibVmc_VsuC5S4V2_5pPiLqzP.AczUxDh1PkwCX9S35Hb5jPKyHctqe.v6czExbfiluo9WgLD0JDYiBM0zyZAzdx..DQFmbzWCSTDUG._X457Wk7pgTxPSDZJmxgaBDyFHnm3yWIxPjUho_buJI8i9eIeJjmdnQrtA3fnDw7Rkvw5vn6DnVbEq"#POST
data = {"Type": 0,
        "City": "南京"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(ULR,data = data,headers = headers)


# In[ ]:




