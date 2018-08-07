import requests
import  demjson
from xml.etree import ElementTree
import json
import re
from 发送邮件 import *
response = requests.get('http://q.ssajax.cn/webhandler/rank_market.ashx?style=1&_=1506652755160')
d = response.text.replace('var varprice=','').replace(';','')
dr = re.compile(r'<[^>]+>',re.S)
dd1 = dr.sub('',demjson.decode(d)['html'])

#处理html
# dr = re.compile(r'<[^>]+>',re.S)
# dd = dr.sub('',demjson.decode(d)['msg'])
dd2 = dr.sub('',demjson.decode(d)['msg'])
vstr = dd1[dd1.find("最新价:"):dd1.find("涨跌额")].replace('最新价','大盘')+"--"+dd2[dd2.find("平均市净率"):dd2.find("总股本")]+"--"+dd2[dd2.find("平均市盈率"):dd2.find("总市值")]

mail(vstr)