import tushare as ts
import pandas as pd
def calStock(sname,btime):
    resList =[]
    tmphn = ts.get_k_data(sname.strip(),start=btime.strip())
    # print(tmphn)
    resList.append(tmphn.iloc[1].values[2])
    resList.append(tmphn.iloc[2].values[3])
    return resList

def calFromfile(url):
    data =open(url)
    vbtime=[]
    vsname=[]
    vnextprice=[]
    vnextMaxprice=[]

    for eachline in data:
        (btime,sname)=eachline.split('|')
        res =calStock(sname,btime)
        vbtime.append(btime)
        vsname.append(sname)
        vnextprice.append(res[0])
        vnextMaxprice.append(res[1])
    df =pd.DataFrame({
            'btime':vbtime,
            'sname':vsname,
            'vnextprice':vnextprice,
            'vnextMaxprice':vnextMaxprice
         })
    df.to_excel('result.xls')

if __name__=='__main__':
    # #12号产生金叉，13号收盘买入，14号最高价卖出
    # re =calStock('000001','2018-06-12')
    # print(re[0])#取得后一天的收盘价
    # print(re[1])#取得后2天的最高价
    calFromfile('test.txt')