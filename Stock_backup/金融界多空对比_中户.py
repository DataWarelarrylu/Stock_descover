from Stock_backup.股票方法集 import *

vstcode = [] #证券代码
vstname = [] #证券简称
vduokong = [] #多空比值
vduobuy = [] #多方买入
vkongsale = [] #空方卖出
vprice = [] #最新价
vzhangdiee = [] #涨跌额
vzhangdifu = [] #涨跌幅
vzongchenjiao = [] #总成交额
vdate = [] #更新时间

for j in range(1,21):
  for i in range(1,11):
      if i==1 :
         re =GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/a')
         vstcode.append(re)
      elif i==2:
          re = GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/a')
          vstname.append(re)
      elif i ==3:
          re =GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vduokong.append(re)
      elif i==4:
          re = GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vduobuy.append(re)
      elif i == 5:
          re =GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vkongsale.append(re)
      elif i==6:
          re = GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vprice.append(re)
      elif i ==7:
          re =GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vzhangdiee.append(re)
      elif i==8:
          re = GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vzhangdifu.append(re)
      elif i ==9:
          re =GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
          vzongchenjiao.append(re)
      else :
         re = GetzhibiaoData(url='http://summary.jrj.com.cn/zljk/zhdkdb.shtml?vname=hqdata&level=2&sort=ratio&page=1&order=desc&size=20&dk=dk',vPath='//*[@id="grid-1"]/tbody/tr[' + str(j) + ']/td[' + str(i) + ']/span')
         vdate.append(re)

data = {'stcode':vstcode,
        'stname':vstname,
        'duokong' : vduokong,
        'duobuy' : vduobuy,
        'kongsale' : vkongsale,
        'price' : vprice,
        'zhangdiee' : vzhangdiee,
        'zhangdifu' : vzhangdifu,
        'zongchenjiao' : vzongchenjiao,
        'cdate' : vdate,
}
# print(data)
fr = pd.DataFrame(data)

insertData(fr,'st_jrj_zh')