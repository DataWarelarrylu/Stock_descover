import talib as ta
import  tushare as ts
import pandas as pd
from 股票系统第一期.config import *



def getRSI(vstcode):
    df = ts.get_k_data(vstcode,ktype='W', start='2015-01-03', end='2017-10-20')
    high=   df['high'].values
    low = df['low'].values
    closed = df['close'].values
    date = df['date'].values
    rs=ta.RSI(closed,timeperiod=6)

    sar = ta.SAR(high,low)
    data = {
        "date": date,
        "close": closed,
        "rsi": rs,
        "sar":sar
    }
    df2 = pd.DataFrame(data)
    return df2
if __name__ == '__main__':
        # for i in vcodeList:
         df = getRSI('600000')
         df['stcode']='600000'
         print(df)
         # df.to_csv("D:/Data/stockData/"+i+".csv")
