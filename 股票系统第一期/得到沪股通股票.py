import requests
import  demjson
import  pandas as pd
SNAME=[]
SALESNAME=[]
PRICE=[]
RCHANGE=[]
SALESCODE=[]
BUYERNAME=[]
CPRICE=[]
SECUCODE=[]
TDATE=[]
def getDataDetail():
    res1 = requests.get('http://dcfm.eastmoney.com//EM_MutiSvcExpandInterface/api/js/get?type=HSGTCJB&token=70f12f2f4f091e459a279469fe49eca5&sty=HGT&js=var%20ukLsryGW={%22data%22:(x),%22pages%22:(tp)}&ps=100&p=1&sr=-1&filter=&st=DetailDate&cmd=601989&rt=50459446').text.replace('var ukLsryGW=','')
    res2 = demjson.decode(res1)
    # print(res2)
    for i in range(len(res2['data'])-2):
        SNAME.append(res2['data'][i]['HGTMRJE'])
        SALESNAME.append(res2['data'][i]['HGTCJJE'])
        PRICE.append(res2['data'][i]['ChangePercent'])
        RCHANGE.append(res2['data'][i]['HGTJME'])
    data={
        "SNAME":SNAME,
        "SALESNAME":SALESNAME,
        "PRICE":PRICE,
        "RCHANGE":RCHANGE
    }
    print(pd.DataFrame(data))

if __name__ == '__main__':
    getDataDetail()

