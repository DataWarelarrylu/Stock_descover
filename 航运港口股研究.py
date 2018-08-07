#coding=utf-8

import tushare as ts

df = ts.bdi('D')
df[df['date']=='2017-09-28']
print (df[df['date']=='2017-09-28'])