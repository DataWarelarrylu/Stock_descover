import requests
import  demjson
import  pandas as pd
from sqlalchemy import create_engine
engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')
import  time
vtime =time.strftime('%Y-%m-%d')
SNAME=[]
SALESNAME=[]
PRICE=[]
RCHANGE=[]
SALESCODE=[]
BUYERNAME=[]
CPRICE=[]
SECUCODE=[]
TDATE=[]





def getDataDetail(vpag,vdate):
    res1 = requests.get('http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?type=DZJYXQ&token=70f12f2f4f091e459a279469fe49eca5&cmd=&st=SECUCODE&sr=1&p='+str(vpag)+'&ps=50&js=var%20aHsNAnSW={pages:(tp),data:(x)}&filter=(Stype=%27EQA%27)(TDATE=^'+vdate+'^)&rt=50285747').text.replace('var aHsNAnSW=','')
    res2 = demjson.decode(res1)
    for i in range(len(res2['data'])-2):
        SNAME.append(res2['data'][i]['SNAME'])
        SALESNAME.append(res2['data'][i]['SALESNAME'])
        PRICE.append(res2['data'][i]['PRICE'])
        RCHANGE.append(res2['data'][i]['RCHANGE'])
        SALESCODE.append(res2['data'][i]['SALESCODE'])
        BUYERNAME.append(res2['data'][i]['BUYERNAME'])
        CPRICE.append(res2['data'][i]['CPRICE'])
        SECUCODE.append(res2['data'][i]['SECUCODE'])
        TDATE.append(res2['data'][i]['TDATE'])


if __name__ =='__main__':
    vList=[
'2017-09-19',
'2017-09-20',
'2017-09-21',
'2017-09-22',
'2017-09-25',
'2017-09-26',
'2017-09-27',
'2017-09-28',
'2017-09-29',
'2017-10-09',
'2017-10-10',
'2017-10-11',
'2017-10-12',
'2017-10-13',
'2017-10-16',
'2017-10-17',
'2017-10-18',
'2017-10-19',
'2017-10-20',
]
    for j in vList:
        for i in range(1,3):
            SNAME = []
            SALESNAME = []
            PRICE = []
            RCHANGE = []
            SALESCODE = []
            BUYERNAME = []
            CPRICE = []
            SECUCODE = []
            TDATE = []

            print(j)
            getDataDetail(i,j)

            data ={
               'SNAME':SNAME,
                'SALESNAME':SALESNAME,
                'PRICE':PRICE,
                'BUYERNAME':BUYERNAME,
                'CPRICE':CPRICE,
                'SECUCODE':SECUCODE,
                'TDATE':TDATE,

            }
            df =pd.DataFrame(data)
            print(df)
            df.to_sql('dfcf_dzjy', engine, if_exists='append', index=None)
        # time.sleep(60)
