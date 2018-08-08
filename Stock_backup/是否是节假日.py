import tushare as ts

df =ts.trade_cal()
df.to_csv('test.csv')