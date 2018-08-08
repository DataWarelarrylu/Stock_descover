import  tushare as ts
import requests
cols =['open','high','low','close','vol']
# 'dateL', 'openL', 'highL', 'lowL', 'closeL', 'volL'
# df = ts.bar('600021','2017-01-01','2017-10-01')
# df.to_csv('D:/Data/600021.csv',columns=cols)
vdata ={
    'token':'24ade310-4817-48f4-a192-e886524fcc3a',
    'date':'2017-11-08',
    'stockCodes':'600021',
    'metrics':["market_value", "pe_ttm", "pb", "dividend_r"]
}
html = requests.post('https://www.lixinger.com/api/open/a/fs-info',data=vdata)
print(html.text)