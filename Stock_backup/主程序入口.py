from Stock_backup.股票方法集 import *

vstcode = []
vstname = []
vprice = []
vzhibiao = []
for j in range(1,41):
  for i in [1,2,3,8]:
      if i==1 :
         re =GetzhibiaoData(url='http://vip.stock.finance.sina.com.cn/q/go.php/vDYData/kind/dxcj/index.phtml',vPath='//*[@id="dataTable"]/tbody/tr['+str(j)+']/td['+str(i)+']/a')
         vstcode.append(re)
      elif i==2:
          re = GetzhibiaoData(url='http://vip.stock.finance.sina.com.cn/q/go.php/vDYData/kind/dxcj/index.phtml',vPath='//*[@id="dataTable"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/a')
          vstname.append(re)
      elif i == 3:
          re =GetzhibiaoData(url='http://vip.stock.finance.sina.com.cn/q/go.php/vDYData/kind/dxcj/index.phtml',vPath='//*[@id="dataTable"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']')
          vprice.append(re)
      else :
         re = GetzhibiaoData(url='http://vip.stock.finance.sina.com.cn/q/go.php/vDYData/kind/dxcj/index.phtml',vPath='//*[@id="dataTable"]/tbody/tr['+str(j)+']/td[' + str(i) + ']')
         vzhibiao.append(re)

data = {'stcode':vstcode,
         'stname':vstname,
        'price':vprice,
        'zhibiao':vzhibiao}
fr = pd.DataFrame(data)

insertData(fr,'sttest')