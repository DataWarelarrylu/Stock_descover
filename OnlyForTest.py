import tushare as ts
import re
###################用例一
# hq = ts.get_day_all() #当前行情信息
# share = ts.get_stock_basics() #股票基本信息
# hq = hq.set_index('code')
# #选取每股公积金，eps，上市日期字段
# basics = share[['reservedPerShare','esp','timeToMarket']]
# df = hq.merge(basics,left_index=True,right_index=True)
# #排除新股后(选定在2017年2月1日前上市的公司)，查看当日涨跌幅排名前后的个股情况
# nonews = df[(df.timeToMarket < 20170201) & (df.timeToMarket > 0)]

###################用例二
# hq = ts.get_day_all() #当前行情信息
# share = ts.get_stock_basics() #股票基本信息
# hq = hq.set_index('code')
# #basics = share[['reservedPerShare','esp','timeToMarket']]
# df = hq.merge(share,left_index=True,right_index=True)
# #res = share[(share.pe < 30) & (share.esp > 0.2) & (share.interval3 < -15) & (share.timeToMarket < 20170301)]
#
# hq.to_csv('D:/hq.csv')
# share.to_csv('D:/share.csv')
# df.to_csv('D:/df.csv')

###############################################################################################################

import requests
import pandas as pd
# response = requests.get('http://stock.stockstar.com/list/4007.shtml')
# html = response.text
# pattern = re.compile('<li.*?span.*?href="(.*?)"今日"(.*?)".*?</li>', re.S)
# results = re.findall(pattern, html)
# for result in results:
#     print(result)

# df =ts.moneyflow_hsgt()


df = pd.DataFrame(pd.read_excel('test.xlsx',header=0))
print(df.iloc[0:1,])