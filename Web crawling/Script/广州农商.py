#!/usr/bin/env python
# coding: utf-8

# In[17]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
                                                            
URL = "https://www.grcbank.com/eportal/ui?moduleId=3&pageId=747031f10b4c4a8ca844ab8e782096b0&portal.url=/portlet/map-portlet!getMapDotDataSelectList.portlet"
data = {"currentPageNo": 1,
"queryInfo": "",
"regionRadio": "ec29aa50c39346b29c22c495e6bca1a2",
"containsRegionRadio": "yes",
"categoryRadio": "" ,
"containsCategoryRadio": "yes",
"oneHidden": "all",
"twoHidden": "all",
"threeHidden": "all"}
headers = {"Connection":"close",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(URL,data = data,headers = headers,stream=True,verify=False)
json.loads(resp.text)


# In[19]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","Province"])
for i in range(1,104):
    data = {"currentPageNo": i,
            "queryInfo": "",
            "regionRadio": "ec29aa50c39346b29c22c495e6bca1a2",
            "containsRegionRadio": "yes",
            "categoryRadio": "" ,
            "containsCategoryRadio": "yes",
            "oneHidden": "all",
            "twoHidden": "all",
            "threeHidden": "all"}
    resp = requests.post(URL,data = data,headers = headers)
    bank = json.loads(resp.text)['result']
    print(i)
    for j in bank:
        dataframe.loc[len(dataframe), :] = [j['dotName'],j['dotAddress'],j['dotPhone'],j['dotDimension'],j['dotLongitude'],j['id'],"广州省"]
            


# In[20]:


dataframe


# In[ ]:


dataframe.drop_duplicates('name').to_excel('./银行网点数据.xlsx', index=False) 

