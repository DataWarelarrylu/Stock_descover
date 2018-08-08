import tushare as ts
import pandas as pd

def getToday():
    df = ts.get_today_all()
    df.to_csv('today.csv')

def getDay(vday):
    df = ts.get_day_all(vday)
    df.to_csv('day.csv')


if __name__ =='__main__':
    # getDay('2018-07-06')
    df =pd.read_csv('today.csv')
    df2 =pd.read_csv('day.csv')
    selhsl=df.turnoverratio<1
    selpb1=df.pb<1
    selpb2 = df.pb >0
    selpe1=df2.pe<30
    selpe2= df2.pe>0
    # print(df[selhsl].count()[0])#换手率小于1的股票个数
    # print(df[selpb1 & selpb2].count()[0])#跌破净资产的股票个数
    # print(df2[selpe1 & selpe2].count()[0])#低于市盈率30的股票个数
    # df[selpb1 & selpb2].to_csv('tmp.csv')
    # print(df.count()[0])
    # print(df2.count()[0])
    print('低换手率个数:'+str(round(int(df[selhsl].count()[0])/int(df.count()[0]),2)*100)+'%')
    print('跌破净资产个数:' + str(round(int(df[selpb1 & selpb2].count()[0]) / int(df.count()[0]),2)*100)+'%')
    print('低于市盈率30个数:' + str(round(int(df2[selpe1 & selpe2].count()[0]) / int(df2.count()[0]),2)*100)+'%')
