import  sys
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# browser.get('http://data.eastmoney.com/invest/invest/list.html')
# res01 =browser.page_source
# print(res01)
#
# import re
# links = re.findall('href="(\d+)\.html', res01)
# for i in links:
#     print(i)

import tushare as ts

#
# if sys.argv[1]==1:
#     print('first function')
# if sys.argv[1]==1:
#     print('Second function')
# print(sys.argv[1])


# import time
# strtime=time.strftime('%Y-%m-%d')
# print(strtime)

#
# from sqlalchemy import create_engine
# import  pandas as pd
# engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')
# data ={'1':[1,2,3,4,5]}
# df = pd.DataFrame(data)
# df.to_sql('t001', engine, if_exists='append', index=None)

# import  tushare as ts
# df =ts.bar('600021','2017-10-09','2017-10-10')
# print(df['close'].max())
from lxml.html import parse
from urllib.request import urlopen

url = 'http://example.com/'
headers = { 'Host':'example.com',
                    'Connection':'keep-alive',
                    'Cache-Control':'max-age=0',
                    'Accept': 'text/html, */*; q=0.01',
                    'X-Requested-With': 'XMLHttpRequest',
                    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36',
                    'DNT':'1',
                    'Referer': 'http://example.com/',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
}
data = None
doc = parse(urlopen('http://stockdata.stock.hexun.com/zlkp/',headers=headers))
print(doc)