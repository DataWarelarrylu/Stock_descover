import requests
import pandas as pd
time = []
num = []
price = []
vtype = []
from sqlalchemy import create_engine
engine = create_engine('oracle://gmonkey:gmonkey@127.0.0.1:1521/xe')

reponse = requests.get('http://vip.stock.finance.sina.com.cn/quotes_service/view/CN_TransListV2.php?num=2000&symbol=sh600373').text.replace('var trade_item_list = new Array();','').strip().replace('trade_INVOL_OUTVOL',"=")
vList = reponse.replace("\n", "").split(';')
del vList[len(vList)-2];
for i in vList:
    #  print(i)
    # print('############################')
    if len(i.split('='))>=2:
      time.append(i.split('=')[1].replace('new Array(','').replace(')','').split(',')[0])
      num.append(i.split('=')[1].replace('new Array(', '').replace(')', '').split(',')[1])
      price.append(i.split('=')[1].replace('new Array(', '').replace(')', '').split(',')[2])
      vtype.append(i.split('=')[1].replace('new Array(', '').replace(')', '').split(',')[3])

data ={
    "time":time,
    "num":num,
    "price":price,
    "vtype":vtype
}

df = pd.DataFrame(data)
# print(df)
df.to_sql('sina_cjmx', engine, if_exists='append', index=None)
