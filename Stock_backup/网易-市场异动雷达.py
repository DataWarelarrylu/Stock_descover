import requests
import  pandas as pd
from sqlalchemy import create_engine
engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')
response = requests.get('http://quotes.money.163.com/hs/realtimedata/service/radar.php?host=/hs/realtimedata/service/radar.php&page=0&fields=CODE,NAME,PRICE,PERCENT,DATE,TYPES,SYMBOL,NUMBER,HSL&sort=DATE&order=desc&count=5954&type=query&callback=callback_2084078549&req=42116').text
d1 = response.replace('callback_2084078549(','').replace(')','')
d2=eval(d1)

SYMBOL = []
TYPE = []
TITLE = []
NAME = []
DATE = []
NUMBER = []
PERCENT = []
INFO = []
HSL = []
PRICE = []
TYPES = []

for i in d2['list']:
     a1 = eval(str(i))
     SYMBOL.append(a1['SYMBOL'])
     TYPE.append(a1['TYPE'])
     TITLE.append(a1['TITLE'])
     NAME.append(a1['NAME'])
     DATE.append(a1['DATE'])
     NUMBER.append(str(a1['NUMBER']).replace(']','').replace('[',''))
     PERCENT.append(a1['PERCENT'])
     INFO.append(a1['INFO'])
     HSL.append(a1['HSL'])
     PRICE.append(a1['PRICE'])
     TYPES.append(str(a1['TYPES']).replace(']','').replace('[',''))

data = {
'SYMBOL':SYMBOL,
'TYPE':TYPE ,
'TITLE':TITLE ,
'NAME':NAME ,
'CDATE':DATE ,
'NUMBER':NUMBER ,
'PERCENT':PERCENT ,
'INFO':INFO ,
'HSL':HSL ,
'PRICE':PRICE ,
'TYPES':TYPES ,
}

df = pd.DataFrame(data)
df.to_sql('wy_scyd', engine, if_exists='append', index=None)

