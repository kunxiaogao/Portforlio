# 浦发银行 - 无法直接请求的得到数据，只能使用webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

from time import sleep
from lxml import etree
import pandas as pd

driver_path = '../../房价爬虫数据抓取测试-含滑块验证/webdriver/chromedriver.exe'
options = ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_experimental_option('w3c', False)
options.add_argument('--headless') # 无头浏览器
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
driver = Chrome(executable_path=driver_path, options=options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
    })
    """
})
driver.delete_all_cookies()
# 打开指定链接
url = 'https://www.spdb.com.cn/web_query/'
driver.get(url)
WebDriverWait(driver, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//a[@id="querybutton1"]')
))
driver.find_element_by_xpath('//a[@id="querybutton1"]').click()
data = pd.DataFrame(columns=['id', 'name', 'addr', 'tel', 'postcode', 'lng_gcj02', 'lat_gcj02'])
while True:
    sleep(3)
    html = etree.HTML(driver.page_source)
    print(html.xpath('//a[@class="active"]/text()')[0])
    banks = html.xpath('//table[@class="table02"]//tr[not(@id)]')
    for bank in banks:
        data.loc[len(data), :] = [
            bank.xpath('./td[1]/input/@value')[0].strip(),
            bank.xpath('./td[2]/text()')[0].strip(),
            bank.xpath('./td[3]/text()')[0].strip(),
            bank.xpath('./td[5]/text()')[0].strip(),
            bank.xpath('./td[4]/text()')[0].strip(),
            float(bank.xpath('./td[1]/input/@long')[0].strip()),
            float(bank.xpath('./td[1]/input/@dimen')[0].strip())
        ]
    next_page = html.xpath('//a[@class="classPage"][contains(text(), "下一页")]')
    if next_page:
        driver.find_element_by_xpath('//a[@class="classPage"][contains(text(), "下一页")]').click()
    else:
        break