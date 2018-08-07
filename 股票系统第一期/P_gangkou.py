import tushare as ts
from sqlalchemy import create_engine
import  sys
import time
# strtime=time.strftime('%Y-%m-%d')
strtime='2017-09-28'
engine = create_engine('oracle://lb:lb@192.168.10.3:1521/test')

def getBDIData():
    df = ts.bdi('D')
    df.to_sql('p_bdi_ft', engine, if_exists='append', index=None)

def getBDIData_DAY(vdate):
    df = ts.bdi('D')
    df2 = df[df['date'] == '2017-09-28']
    df2.to_sql('p_bdi_ft', engine, if_exists='append', index=None)
if __name__=='__main__':
    if sys.argv[1]=='day':
        getBDIData_DAY(strtime)
    else:
      getBDIData()