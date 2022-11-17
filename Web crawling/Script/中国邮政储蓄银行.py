#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import pandas as pd
import json
from lxml import etree
import re
import openpyxl
# https://www.psbc.com/cn/common/fwwd/
URL1 = "https://s.psbc.com/portal/PsbcService/dotMap/provinceNames?" #GET
resp1 = json.loads(requests.get(URL1).text.strip('empty()'))['resultList']
P_NAME = []
RGLM_NAME = []
data = pd.DataFrame(columns=["name", "address", "tel", "lat_gcj02", "lng_gcj02","id"])
for i in resp1:
    if i not in P_NAME:
        P_NAME.append(i['RGLM_NAME'])
URL2 = "https://s.psbc.com/portal/PsbcService/dotMap/regionalism?provRglmName={}"
for j in P_NAME:
    resp2 = json.loads(requests.get(URL2.format(j)).text.strip('empty()'))['resultList']
    for k in resp2:
        city = k["CITY_RGLM_NAME"]
        rglmlist = k['rglmList']
        for n in rglmlist:
            zone = n['RGLM_NAME']
            if zone not in RGLM_NAME:
                RGLM_NAME.append(zone)
URL3 = "https://s.psbc.com/portal/PsbcService/dotMap/businessOutlets?rglmName={}"
for m in RGLM_NAME:
    if json.loads(requests.get(URL3.format(m)).text.strip('empty()'))['retCode'] == '000':
        resp3 = json.loads(requests.get(URL3.format(m)).text.strip('empty()'))['resultList']
        print(m)
        for c in resp3:
            data.loc[len(data), :] = [c["BRH_NAME"],c["BRH_ADDR"],c["MNG_DUTY_TEL"],c["LAT_ITUDE"],c["LONG_ITUDE"],c["BRH_CODE"]] 
data.drop_duplicates('name').to_excel('./中国邮政储蓄银行网点数据.xlsx', index=False)


# In[2]:


import requests
import pandas as pd
import json
from lxml import etree
import re
import openpyxl
# https://www.psbc.com/cn/common/fwwd/
URL1 = "https://s.psbc.com/portal/PsbcService/dotMap/provinceNames?" #GET
headers = {"Connection":"close","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
resp1 = json.loads(requests.get(URL1).text.strip('empty()'))['resultList']
P_NAME = []
RGLM_NAME = []
data = pd.DataFrame(columns=["name", "address", "tel", "lat_gcj02", "lng_gcj02","id","city","zone"])
for i in resp1:
    if i not in P_NAME:
        P_NAME.append(i['RGLM_NAME'])
URL2 = "https://s.psbc.com/portal/PsbcService/dotMap/regionalism?provRglmName={}"
URL3 = "https://s.psbc.com/portal/PsbcService/dotMap/businessOutlets?rglmName={}"
for j in P_NAME:
    resp2 = json.loads(requests.get(URL2.format(j),headers = headers, verify = False).text.strip('empty()'))['resultList']
    for k in resp2:
        city = k["CITY_RGLM_NAME"]
        rglmlist = k['rglmList']
        for n in rglmlist:
            zone = n['RGLM_NAME']
            if json.loads(requests.get(URL3.format(zone),headers = headers, verify = False).text.strip('empty()'))['retCode'] == '000':
                 resp3 = json.loads(requests.get(URL3.format(zone)).text.strip('empty()'))['resultList']
                 print(zone)
            for c in resp3:
                data.loc[len(data), :] = [c["BRH_NAME"],c["BRH_ADDR"],c["MNG_DUTY_TEL"],c["LAT_ITUDE"],c["LONG_ITUDE"],c["BRH_CODE"],city,zone] 
data.drop_duplicates('name').to_excel('./中国邮政储蓄银行网点数据.xlsx', index=False)


# In[3]:


data


# In[ ]:




