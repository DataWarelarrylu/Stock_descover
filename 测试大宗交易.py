import tushare as ts
from sqlalchemy import  create_engine
import  pandas as pd
import datetime
engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')

CRDT=[]
ST_CODE=[]
ST_NAME=[]
CPRICE=[]
SALESNAME=[]
BUYERNAME=[]
st_max =[]
st_min =[]



def getData():
    res = pd.read_sql('select * from S2_DFCF_DZJY_hist', engine)
    return res

def getAftDate(vdate,n):
    myday = datetime.datetime(int(vdate[0:4]), int(vdate[5:7]), int(vdate[8:10])) + datetime.timedelta(days=+n)
    # print(str(myday).replace(' 00:00:00',''))
    return str(myday).replace(' 00:00:00','')
if __name__ == '__main__':
    df = getData()
    # for i in range(len(df)):
    for i in range(len(df)):
        print(df.iat[i,1],getAftDate(df.iat[i,0],1),getAftDate(df.iat[i,0],10))
        ds =ts.bar(df.iat[i,1],start_date=getAftDate(df.iat[i,0],1),end_date=getAftDate(df.iat[i,0],10))
        CRDT.append(df.iat[i,0])
        ST_CODE.append(df.iat[i,1])
        ST_NAME.append(df.iat[i,2])
        CPRICE.append(df.iat[i,3])
        SALESNAME.append(df.iat[i,4])
        BUYERNAME.append(df.iat[i,5])
        st_max.append(ds['close'].max())
        st_min.append(ds['close'].min())
    data ={
        'CRDT' :CRDT,
        'ST_CODE':ST_CODE,
        'ST_NAME' : ST_NAME,
        'CPRICE' : CPRICE,
        'SALESNAME':SALESNAME,
        'BUYERNAME':BUYERNAME,
        'st_max' : st_max,
        'st_min':st_min
    }
    df2 = pd.DataFrame(data)
    df2.to_sql('dfcf_dzjy_res', engine, if_exists='append', index=None)
