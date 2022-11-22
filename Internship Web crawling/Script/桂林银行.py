#!/usr/bin/env python
# coding: utf-8

# In[2]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "https://www.guilinbank.com.cn/portal-home/net/position/queryList?OmcXG6H0=5YHP15m2DNONFur_XDBQLWPBiGHuDJ4k6oyNq_7uZ_6Mj3salOg7icDUOlLJPJ10bUEAOTAxENbpoKw55zQ502aDFmlQKupkMSqBL7kQBD26b3X0PHwh_QFqlTLX7_wkU0umYtjGzhkcCSqxDGPnMr_Gn5yYFIhVj8zmIqoygHm9uln.5UoGMzJ7pzboXXkIU7yNqgnkCmt.IIFJIxdXpV4AmgJAiwxcnx8voH09SLHapBPH_7wTZGeHCzfW_QSPOJZS_BHs0lk0rRD9ZpWRUmWffTcIWtFt_KSiQBi7CjU0FpR1hIsZhhtpLnKFcM873"
data = {"netAddress": "",
        "netAreaName": "桂林市",
        "netTypeName": "",
        "pageNum": 1,
        "pageSize": 5}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
a = requests.post(URL,data = data,headers = headers)


# In[4]:


a.text


# In[ ]:




