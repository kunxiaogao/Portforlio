#!/usr/bin/env python
# coding: utf-8

# In[31]:


from urllib.parse import unquote,quote
from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "http://www.cgbchina.com.cn/Channel/185652?currPage=1&pageSize=20" # POST
data = {"operation": "net",
        "searchNetBranch": "上海",
        "currPage": "2",
        "pageSize": "20",
        "equType2": "-1"}
resp = requests.post(URL,data = data,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"})
resp.text


# In[17]:


a = "%C9%CF%BA%A3%B7%D6%D0%D0"
unquote(a)


# In[38]:


unquote("%A3%B7")


# In[ ]:




