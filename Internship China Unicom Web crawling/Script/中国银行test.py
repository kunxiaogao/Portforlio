#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
from lxml import etree
import requests

base_url = 'https://www.bankofchina.com/sourcedb/operations2021/406/446/447/index_124.htm'
resp = requests.get(base_url)
resp.encoding = resp.apparent_encoding
html = etree.HTML(resp.text)
page_num = int(html.xpath('//div[@class="turn_page"]//span/text()')[0])
if page_num > 1:
    url = base_url + link.strip('./')


# In[6]:


base_url = 'https://www.bankofchina.com/sourcedb/operations2021/'
html = etree.HTML(requests.get(base_url).text)
links = html.xpath('//ul[@class="list clearfix"]/li/a/@href')
for link in links:
    link2 = link.strip('.htm')+'_{}'+'.htm'
    url = base_url + link.strip('./')
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    banks = html.xpath('//table[@id="documentContainer"]//tr')[1:]
    for bank in banks:
        data.loc[len(data), :] = [bank.xpath(xpath_str.format(i))[0].strip() for i in save_index]
    page_num = int(html.xpath('//div[@class="turn_page"]//span/text()')[0])
    if page_num > 1:
        for i in range(1,page_num):
            url = (base_url + link2.strip('./')).format(i)
            resp = requests.get(url)
            resp.encoding = resp.apparent_encoding
            html = etree.HTML(resp.text)
            banks = html.xpath('//table[@id="documentContainer"]//tr')[1:]
            for bank in banks:
                data.loc[len(data), :] = [bank.xpath(xpath_str.format(i))[0].strip() for i in save_index]


# In[7]:


import pandas as pd
from lxml import etree
import requests

base_url = 'https://www.bankofchina.com/sourcedb/operations2021/'
html = etree.HTML(requests.get(base_url).text)
links = html.xpath('//ul[@class="list clearfix"]/li/a/@href')
data = pd.DataFrame(columns=['name', 'zone', 'addr', 'tel'])
save_index = [1, 2, 4, 5]
xpath_str = './td[{}]/text()'
for link in links:
    link2 = link.strip('.htm') + '_{}' + '.htm'
    url = base_url + link.strip('./')
    resp = requests.get(url)
    resp.encoding = resp.apparent_encoding
    html = etree.HTML(resp.text)
    banks = html.xpath('//table[@id="documentContainer"]//tr')[1:]
    for bank in banks:
        data.loc[len(data), :] = [bank.xpath(xpath_str.format(i))[0].strip() for i in save_index]
    page_num = int(html.xpath('//div[@class="turn_page"]//span/text()')[0])
    if page_num > 1:
        for i in range(1, page_num):
            url = (base_url + link2.strip('./')).format(i)
            resp = requests.get(url)
            resp.encoding = resp.apparent_encoding
            html = etree.HTML(resp.text)
            banks = html.xpath('//table[@id="documentContainer"]//tr')[1:]
            print(i)
            for bank in banks:
                data.loc[len(data), :] = [bank.xpath(xpath_str.format(i))[0].strip() for i in save_index]
data


# In[8]:


data.drop_duplicates('name').to_excel('./中国银行网点数据.xlsx', index=False)


# In[ ]:




