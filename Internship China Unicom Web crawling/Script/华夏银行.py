#!/usr/bin/env python
# coding: utf-8

# In[58]:


from lxml import etree
import json
import re
import pandas as pd
import openpyxl
import requests
URL = "https://www.hxb.com.cn/hxmap/get_bank.jsp?params.areaCode=p001&params.branchCode=c0001&params.bankType=2&page=1"
resp = requests.get(URL).text.strip("\r\n\r\n\r\n\r\n\r\n\r\nnull()").rstrip('\r\n')
text = re.sub('[\r\n\t]','',resp)
text2 = re.sub(',    ','',text)
dic = json.loads(text2)
pageCount = dic['pageCount']
bank = dic['list']
print(pageCount)
bank


# In[45]:


URL1 = "https://www.hxb.com.cn/hxmap/get_area.jsp?" #Area code GET
URL2 = "https://www.hxb.com.cn/hxmap/get_branch.jsp?params.status=pc&params.areaCode={}" # Branch Code GET
URL3 = "https://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak=3WV8pQQ2oFdhpnMl9dSZSW3lh7sdmw6i" # 经纬度城市 address城市名字 get
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36 Edg/91.0.864.48"}
resp1 = requests.get(URL1, headers = headers).text.lstrip('\r\n\r\n\r\n\r\n\r\n\r\nnull(').rstrip(')\r\n\r\n')
text = re.sub('[\r\n\t]','',resp1)
text1 = re.sub('\s+','',resp1)
text2 = text1[:-3] + text1[-2:]
result_area = json.loads(text2)['list']


# In[109]:


URL = "https://www.hxb.com.cn/hxmap/get_bank.jsp?params.areaCode={}&params.branchCode={}&params.bankType=2&page={}"
data = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","type","code","city"])
for i in result_area:
    areaCode = i['areaCode']
    areaName = i['areaName']
    resp2 = requests.get(URL2.format(areaCode), headers = headers).text.lstrip('\r\n\r\n\r\n\r\n\r\nnull(').rstrip(')\r\n\r\n')
    a = re.sub('[\r\n\s+]','',resp2)
    b = a[:-3]+a[-2:]
    result_branch = json.loads(b)['list']
    for j in result_branch:
        branchCode = j['branchCode']
        branchName = j['branchName']
        if branchName != "常州":
            resp = requests.get(URL.format(areaCode,branchCode,1)).text.strip("\r\n\r\n\r\n\r\n\r\n\r\nnull()").rstrip('\r\n')
            t = re.sub('[\r\n\t]','',resp)
            t2 = re.sub(',    ','',t)
            dic = json.loads(t2)
            pageCount = int(dic['pageCount'])
            print(branchName)
            for num in range(1,pageCount + 1):
                resp_all = requests.get(URL.format(areaCode,branchCode,num)).text.strip("\r\n\r\n\r\n\r\n\r\n\r\nnull()").rstrip('\r\n')
                t_all = re.sub('[\r\n\t]','',resp_all)
                t2_all = re.sub(',    ','',t_all).replace('\\','|')
                dic_all = json.loads(t2_all)
                bank_all = dic_all['list']
                for k in bank_all:
                    data.loc[len(data), :] = [k['branchName'],k['branchAddress'],k['branchPhone'],k['branchDimension'],k['branchLongitude'],k['bankType'],len(data)+1,branchName]
data.drop_duplicates('name').to_excel('./华夏银行网点数据.xlsx', index=False)


# In[54]:


resp2 = requests.get(URL2.format('p002'), headers = headers).text.lstrip('\r\n\r\n\r\n\r\n\r\nnull(').rstrip(')\r\n\r\n')
a = re.sub('[\r\n\s+]','',resp2)
b = a[:-3]+a[-2:]
json.loads(b)['list']


# In[114]:


len(data)


# In[148]:


resp_all = requests.get(URL.format("p018","c0030",6)).text.strip("\r\n\r\n\r\n\r\n\r\n\r\nnull()").rstrip('\r\n')
t_all = re.sub('[\r\n\t]','',resp_all)
t2_all = re.sub(',    ','',t_all)
t2_all


# In[142]:





# In[120]:


sad = '\r\n\r\n\r\n\r\n\r\n\r\nnull({"rows":10,"page":1,"pageCount":6,"rowCount":56,"list":[\r\n\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "分行营业部",\r\n\t\t\t\t\t"branchAddress": "常州市新北区龙锦路1598号府西花园9幢",\r\n\t\t\t\t\t"branchLongitude": "119.978393",\r\n\t\t\t\t\t"branchDimension":"31.81923",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "1",\r\n\t\t\t\t\t"branchWeekendopen": "2",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "0519-88179863",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": ""个人储蓄业务：周一至周日 8：30-17：00<br>对公、贷款业务：周一至周五 8：30-11：30 13：30-17：00"<br>",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "0"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "新北万达",\r\n\t\t\t\t\t"branchAddress": "新北区万达广场内",\r\n\t\t\t\t\t"branchLongitude": "119.977183",\r\n\t\t\t\t\t"branchDimension":"31.824504",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "晋陵北苑",\r\n\t\t\t\t\t"branchAddress": "新北区晋陵北苑18号（锦绣东院对面）",\r\n\t\t\t\t\t"branchLongitude": "119.978058",\r\n\t\t\t\t\t"branchDimension":"31.802817",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "金百国际",\r\n\t\t\t\t\t"branchAddress": "新北区金百商业广场2-108号（交银大厦对面）",\r\n\t\t\t\t\t"branchLongitude": "119.966735",\r\n\t\t\t\t\t"branchDimension":"31.807282",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "火车站北广场",\r\n\t\t\t\t\t"branchAddress": "火车站北广场",\r\n\t\t\t\t\t"branchLongitude": "119.980162",\r\n\t\t\t\t\t"branchDimension":"31.791455",\r\n\t\t\t\t\t"branchCity": "钟楼支行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "关河西路",\r\n\t\t\t\t\t"branchAddress": "常州市关河西路23-2号（农工商超市对面）",\r\n\t\t\t\t\t"branchLongitude": "119.964521",\r\n\t\t\t\t\t"branchDimension":"31.795046",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "天宁支行",\r\n\t\t\t\t\t"branchAddress": "常州市竹林北路惠峰花园2-12至2-22号",\r\n\t\t\t\t\t"branchLongitude": "119.99991",\r\n\t\t\t\t\t"branchDimension":"31.795207",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "1",\r\n\t\t\t\t\t"branchWeekendopen": "0",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "0519-86929967",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": ""个人储蓄业务：周一至周六 8：30-11：30 13：30-17：00 周日不营业  <br>对公、贷款业务：周一至周五 8：30-11：30 13：30-17：00<br>"<br>",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "0"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "天宁支行",\r\n\t\t\t\t\t"branchAddress": "常州市竹林北路惠峰花园2-12至2-22号",\r\n\t\t\t\t\t"branchLongitude": "119.99991",\r\n\t\t\t\t\t"branchDimension":"31.795207",\r\n\t\t\t\t\t"branchCity": "常州分行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "红梅假日",\r\n\t\t\t\t\t"branchAddress": "红梅假日广场16号",\r\n\t\t\t\t\t"branchLongitude": "119.990132",\r\n\t\t\t\t\t"branchDimension":"31.790585",\r\n\t\t\t\t\t"branchCity": "钟楼支行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n\t\t\t\t{\r\n\t\t\t\t\t"branchName": "北直街",\r\n\t\t\t\t\t"branchAddress": "北直街38号",\r\n\t\t\t\t\t"branchLongitude": "119.96491",\r\n\t\t\t\t\t"branchDimension":"31.793337",\r\n\t\t\t\t\t"branchCity": "钟楼支行",\r\n\t\t\t\t\t"branchWorktime": "null",\r\n\t\t\t\t\t"branchQueueflag": "null",\r\n\t\t\t\t\t"branchWeekendopen": "null",\r\n\t\t\t\t\t"branchNews": "暂无公告信息",\r\n\t\t\t\t\t"branchPhone": "null",\r\n\t\t\t\t\t"branchPhone2": "null",\r\n\t\t\t\t\t"branchBusinessTime": "null",\r\n\t\t\t\t\t"branchShowNewsBeginTime": "null",\r\n\t\t\t\t\t"branchShowNewsEndTime": "null",\r\n\t\t\t\t\t"bankType": "1"\r\n\t\t\t\t},\r\n\t\t\r\n    ]\r\n})\r\n\r\n'
try:
    res = json.loads(sad)
except Exception as err:
    print(err)
    tmp = re.sub('""(?=\w)', '"', sad)
    tmp = tmp.replace('<br>"<br>', '')
    print(json.loads(tmp))


# In[113]:


data.drop_duplicates('name').to_excel('./华夏银行网点数据.xlsx', index=False)


# In[123]:


resp_all = requests.get(URL.format("p018","c0030",1)).text.strip("\r\n\r\n\r\n\r\n\r\n\r\nnull()").rstrip('\r\n')
t_all = re.sub('[\r\n\t]','',resp_all)
t2_all = re.sub(',    ','',t_all)
t2_all


# In[ ]:




