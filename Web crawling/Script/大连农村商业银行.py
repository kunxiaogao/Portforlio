#!/usr/bin/env python
# coding: utf-8

# In[1]:


from lxml import etree
import pandas as pd
import requests
import execjs
import re

url = 'http://www.dlrcb.cn/view/todayDlrcb/map.shtml'
res = requests.get(url).text
html = etree.HTML(res)
js = html.xpath('//script/text()')[1].replace('\r', '')
markers = re.findall('var markers[\w\W]+(?=function initMap)', js)
markers_func = 'function a(){' + markers[0] + '\nreturn markers;}'
banks_func = execjs.compile(markers_func)
banks = banks_func.eval('a()')
banks


# In[14]:


dataframe = pd.DataFrame(columns=["name", "address", "tel", "lat", "lng","id"])
for i in banks:
    Con = i['content']
    if '电话' in Con:
        A = Con.split('<br/>')[0]
        T = Con.split('<br/>')[1]
    else:
        A = Con
        T = 'None'
    N = i['title']
    Lat = i['position']['lat']
    Lng = i['position']['lng']
    Id = i['id']
    dataframe.loc[len(dataframe), :] = [N,A,T,Lat,Lng,Id]
    print(N)


# In[13]:


banks[1]['content'].split('<br/>')[1]


# In[16]:


dataframe.drop_duplicates('name').to_excel('./大连农村商业银行网点数据.xlsx', index=False)


# In[17]:


dataframe


# In[ ]:




