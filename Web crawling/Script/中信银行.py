#!/usr/bin/env python
# coding: utf-8

# In[35]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "https://etrade.citicbank.com/portalweb/pq/branchSearch.htm" # POST
data = {"cpLng": "116.413384",
"cpLat": "39.910925",
"cityName": "北京市",
"pageFlag": "1",
"pageSize": "10",
"currentPage": "7",
"tcstNo": "",
"userId": "",
"pwdControlFlag": "0",
"responseFormat": "JSON"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp = requests.post(URL,data = data, headers = headers).json()
pageCount = resp['pageCount']
resultList = resp['content']['resultList']
pageCount
resultList


# In[34]:


URL3 = "https://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=3WV8pQQ2oFdhpnMl9dSZSW3lh7sdmw6i" # 经纬度城市 address城市名字 get
a = requests.get(URL3.format("北京市")).json()['result']['location']
test=('%.6f'% float(a['lng']))
a


# In[19]:


URL2 = "https://etrade.citicbank.com/portalweb/ot/city.htm"
data2 = {"province": "河北省",
"tcstNo": "",
"userId": "",
"pwdControlFlag": "0",
"responseFormat": "JSON"}
b = requests.post(URL2,data = data2, headers = headers).json()


# In[39]:


URL1 = "https://etrade.citicbank.com/portalweb/am/provinceCity.htm" #POST
URL2 = "https://etrade.citicbank.com/portalweb/ot/city.htm"#POST
URL3 = "https://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=3WV8pQQ2oFdhpnMl9dSZSW3lh7sdmw6i" # 经纬度城市 address城市名字 get
URL = "https://etrade.citicbank.com/portalweb/pq/branchSearch.htm" # POST
data1 = {"tcstNo": "",
"userId": "",
"pwdControlFlag": "0",
"responseFormat": "JSON"}
dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","city"])
Province = requests.post(URL1,data=data1,headers=headers).json()['content']['resultList']
for i in Province:
    Pname = i['province']
    data2 = {"province": Pname,
    "tcstNo": "",
    "userId": "",
    "pwdControlFlag": "0",
    "responseFormat": "JSON"}
    City = requests.post(URL2,data = data2, headers = headers).json()['content']['resultList']
    for j in City:
        Cname = j['cityname']
        Center = requests.get(URL3.format(Cname),headers = headers).json()['result']['location']
        lat = ('%.6f'% float(Center['lat']))
        lng = ('%.6f'% float(Center['lng']))
        data_first = {"cpLng": lng,
                "cpLat": lat,
                "cityName": Cname,
                "pageFlag": "1",
                "pageSize": "10",
                "currentPage": "1",
                "tcstNo": "",
                "userId": "",
                "pwdControlFlag": "0",
                "responseFormat": "JSON"}
        resp_first = requests.post(URL,data = data_first, headers = headers).json()
        pageCount = int(resp_first['pageCount'])
        print(Cname)
        for num in range(1,pageCount+1):
            data = {"cpLng": lng,
                "cpLat": lat,
                "cityName": Cname,
                "pageFlag": "1",
                "pageSize": "10",
                "currentPage": num,
                "tcstNo": "",
                "userId": "",
                "pwdControlFlag": "0",
                "responseFormat": "JSON"}
            resp = requests.post(URL,data = data, headers = headers).json()
            resultList = resp['content']['resultList']
            print(num)
            for bank in resultList:
                dataframe.loc[len(dataframe), :] = [bank['branchName'],bank['branchAdd'],bank['branchTel'],bank['branchLat'],bank['branchLng'],bank['branchNo'],Cname]
dataframe.drop_duplicates('name').to_excel('./中信银行网点数据.xlsx', index=False)       
    


# In[ ]:





# In[ ]:




