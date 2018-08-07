import tushare as ts
import pandas as pd
import json
from sqlalchemy import create_engine
import numpy as np
from config import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from fake_useragent import UserAgent
#伪装浏览器头部
ua = UserAgent()
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (ua.random)
SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']
#创建一个dataframe
data = {'crdt':['2017-09-05'],
        'stcode':['600019'],
        'bdate':['2017-09-07'],
        'price':['12']}
frame=pd.DataFrame(data)
browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
# browser = webdriver.PhantomJS(service_args=SERVICE_ARGS,desired_capabilities=dcap)
wait = WebDriverWait(browser, 10)

#读取数据
def getData(tablename):
    res = pd.read_sql(tablename, engine)
    return res
#插入数据库
def insertData(frame,tablename):
    frame.to_sql(tablename,engine,if_exists='append',index=None)

def GetzhibiaoData(url,vPath):
    browser.get(url)
    #vList =[]
    #vList.append(browser.find_element_by_xpath('//*[@id="pricetr"]/tbody/tr/td[1]/a').text)
    res = browser.find_element_by_xpath(vPath).text
    return res

def import_db(sql):
    connection = cx_Oracle.Connection(DBLINE)
    cursor = connection.cursor()
    cursor.execute(sql)
    connection.commit()

###测试股票价格
def getShHistData(stcode,bdate,edate):
    re = ts.get_hist_data(stcode, start=bdate, end=edate)
    return re

# 测试第一期代码 stock_test=>stock_test_res
def TESTHistdata(tablename,stcode,bdate,edate):
    res = getData(tablename)
    df = pd.DataFrame(res)
    for i in range(df.__len__()):
        re =getShHistData(df.loc[df.index[i], stcode],df.loc[df.index[i], bdate],df.loc[df.index[i], edate])
        v_hig = re.loc[re['high'].idxmax(), 'high']
        sql="insert into stock_test_res(stcode,bdate,high_price) values('"+df.loc[df.index[i], stcode]+"','"+df.loc[df.index[i], bdate]+"',"+str(v_hig)+")"
        import_db(sql)
#得到json
def getJson(url):
            f = open('D:/WORK/spiderData/sh.txt', 'a', encoding='utf-8')
            html = browser.get(url)
            f.write(browser.page_source.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','').replace('</pre></body></html>', '').replace('var hqdata=',''))
            f.write("\n")
            f.close()

def ReadDetail(FileUrl):
    f = open(FileUrl, encoding='utf-8')
    s = f.readlines()
    d = list(s)
    h = d[3].split(',')
    for i in h:
        print(i[i.find(':')+1:].replace('}',''))


#TESTHistdata('stock_test','stcode','bdate','edate')

# getJson('http://hqquery.jrj.com.cn/duokong.do?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk')


ReadDetail('D:/WORK/spiderData/sh.txt')