from 股票方法集 import *

vstcode = [] #证券代码
vstname = [] #证券简称
vprice = [] #最新价
vzhangdifu = [] #涨跌幅
vchenjiaoe = [] #成交额
vhuanshoulv = [] #换手率
vsyl = [] #市盈率
vzongshizhi = [] #总市值

vurl='http://data.eastmoney.com/hsgt/index.html'

for j in range(1,11):
  for i in [2,3,5,6,7,8,9,10]:
      if i==2 :
         re =GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/a')
         vstcode.append(re)
      elif i==3:
          re = GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/a')
          vstname.append(re)
      elif i==5:
          re = GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          print(re)
          vprice.append(re)
      elif i == 6:
          re =GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vzhangdifu.append(re)
      elif i==7:
          re = GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']')
          vchenjiaoe.append(re)
      elif i ==8:
          re =GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']')
          vhuanshoulv.append(re)
      elif i==9:
          re = GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']')
          vsyl.append(re)
      else :
          re =GetzhibiaoData(url=vurl,vPath='//*[@id="tb_hgtszdf"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']')
          vzongshizhi.append(re)


data = {'stcode':vstcode,
        'stname':vstname,
        'price' : vprice,
        'zhangdifu' : vzhangdifu,
        'chenjiaoe' : vchenjiaoe,
        'huanshoulv' : vhuanshoulv,
        'syl' : vsyl,
        'zongshizhi' : vzongshizhi,
}
# print(data)
fr = pd.DataFrame(data)

insertData(fr,'st_eastmoney_hgt')