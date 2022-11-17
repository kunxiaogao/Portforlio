#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
import json
from lxml import etree
import re
import openpyxl
URL_bank_per_page = "http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&TXCODE=NZX010&ADiv_Cd={}&Enqr_MtdCd=4&PAGE={}" #PAGE 页码 ADiv_Cd Code
URL_zone_code = "http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&TXCODE=NAREA1&type=3&areacode={}" #areacode 市码
URL_city_code = "http://www.ccb.com/cn/v3/js/city_bank_data.js" #GET
cityCode = []
areacode = []
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id","type"])
resp1 = requests.get(URL_city_code)
resp1.encoding = "utf-8"
lst = json.loads(resp1.text.strip('jsonpCallback()'))['cityList']
for i in lst:
    children = i['children']
    if children != []:
        for city in children:
            cityCode.append(city['cityCode'])
    elif children == []:
        cityCode.append(i['cityCode'])        


# In[23]:





# In[3]:


for code in cityCode:
    resp2 = requests.get(URL_zone_code.format(code),headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()['arealist']
    for area in resp2:
        if area != {}:
            areacode.append(area["areacode"])


# In[33]:


for j in areacode:
    page = int(requests.get(URL_bank_per_page.format(j,1),headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()["TOTAL_PAGE"])
    print(j)
    for pape_num in range(1,page + 1):
        resp3_type1 = requests.get(URL_bank_per_page.format(j,pape_num),headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()["OUTLET_DTL_LIST"]
        resp3_type2 = requests.get(URL_bank_per_page.format(j,pape_num),headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()["SLFBANK_DTL_LIST"]
        resp3_type3 = requests.get(URL_bank_per_page.format(j,pape_num),headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}).json()["SLFEQMT_DTL_LIST"]
        for bank1 in resp3_type1:
            if bank1 != {}:
                data.loc[len(data), :] = [bank1["CCBIns_Nm"],bank1["Dtl_Adr"],bank1["Fix_TelNo"],bank1["Ltt"],bank1["Lgt"],bank1["CCBIns_ID"],'OUTLET_DTL']
        for bank2 in resp3_type2:
            if bank2 != {}:
                data.loc[len(data), :] = [bank2["Bnk_Nm"],bank2["Dtl_Adr"],bank2["Fix_TelNo"],bank2["Ltt"],bank2["Lgt"],bank2["CCB_SlfSvc_Bnk_ID"],'SLFBANK_DTL_LIST']
        for bank3 in resp3_type3:
            if bank3 != {}:
                data.loc[len(data), :] = [bank3["MtIt_Nm"],bank3["Dtl_Adr"],bank3["Fix_TelNo"],bank3["Ltt"],bank3["Lgt"],bank3["SSEq_ID"],'SLFEQMT_DTL_LIST']
data.to_excel('./中国建设银行网点数据.xlsx', index=False)


# In[9]:


sess = requests.Session()
sess.get("http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NZX010&ADiv_Cd=110101&Kywd_List_Cntnt=&Enqr_MtdCd=4&PAGE=1&Cur_StCd=4",
         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"})
page = sess.get("http://www.ccb.com/tran/WCCMainPlatV5?CCB_IBSVersion=V5&SERVLET_NAME=WCCMainPlatV5&isAjaxRequest=true&TXCODE=NZX010&ADiv_Cd=110101&Kywd_List_Cntnt=&Enqr_MtdCd=4&PAGE=1&Cur_StCd=4"
                   ,headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"})
page.text


# In[ ]:




