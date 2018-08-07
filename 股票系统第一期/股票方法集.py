# coding=utf-8
import requests
import  pandas as pd
import  json
from 股票系统第一期.config import  *
import  time
import demjson
from lxml.html import parse
from pandas.io.parsers import TextParser
from urllib.request import urlopen
ISOTIMEFORMAT='%Y%m%d'
strtime=time.strftime(ISOTIMEFORMAT)
from lxml.html import clean
cleaner = clean.Cleaner(style=True,scripts=True,page_structure=False,safe_attrs_only=False)
#历史信息
def get_sh_sz_Data(url,repStr):
    res = requests.get(url).text.replace(repStr,'')
    res01 = json.loads(str(res))
    for i in res01['data']:
        vdic = eval(str(i))
        DetailDate.append(vdic['DetailDate'])
        LCGCode.append(vdic['LCGCode'])
        LCG.append(vdic['LCG'])  # 涨幅
        DRCJJME.append(vdic['DRCJJME'])  # 当日成交净买额
        LCGZDF.append(vdic['LCGZDF'])  # 领涨股涨幅
        MRCJE.append(vdic['MRCJE'])  # 买入成交额
        MCCJE.append(vdic['MCCJE'])  # 卖出成交额
        LSZJLR.append(vdic['LSZJLR'])  # 历史资金累计流入额
        DRZJLR.append(vdic['DRZJLR'])  # 当日资金流入额
#十大成交股
def get10_Data(url,repStr,va):
    res = requests.get(url).text.replace(repStr, '')
    res01 = json.loads(str(res))
    for i in res01['data']:
        vdic = eval(str(i))
        Name.append(vdic['Name'])
        Code.append(vdic['Code'])
        Close.append(vdic['Close'])
        ChangePercent.append(vdic['ChangePercent'])
        HGTJME.append(vdic[va+'GTJME'])
        HGTMRJE.append(vdic[va+'GTMRJE'])
        HGTMCJE.append(vdic[va+'GTMCJE'])
        HGTCJJE.append(vdic[va+'GTCJJE'])
        CRDT.append(strtime)
#涨幅榜
def getHGTZFBData(url,repStr):
    res = requests.get(url).text.replace(repStr, '')
    res01 = demjson.decode(res)
    for i in res01['data']:
         aa =i.split(',')
         STCODE.append(aa[1])
         STNAME.append(aa[2])
         STPRICE.append(aa[3])
         ZFB.append(aa[4])
         HSCRDT.append(strtime)
#融资融券
def getRZRQData(url,repStr):
    res = requests.get(url).text.replace(repStr, '')
    res01 = demjson.decode(res)
    for i in res01['data']:
        vdic = eval(str(i).replace('Decimal(','').replace(')',''))
        scode.append(vdic['scode'])
        sname.append(vdic['sname'])
        hfqjg.append(vdic['hfqjg'])
        tdate.append(vdic['tdate'])
        close.append(vdic['close'])
        zdf.append(vdic['zdf'])
        rzyezb.append(str(vdic['rzyezb']))
        rzye.append(vdic['rzye'])
        rzmre.append(vdic['rzmre'])
        rzmre3.append(vdic['rzmre3'])
        rzmre5.append(vdic['rzmre5'])
        rzmre10.append(vdic['rzmre10'])
        rzche.append(vdic['rzche'])
        rzche3.append(vdic['rzche3'])
        rzche5.append(vdic['rzche5'])
        rzche10.append(vdic['rzche10'])
        rzjmre.append(vdic['rzjmre'])
        rzjmre3.append(vdic['rzjmre3'])
        rzjmre5.append(vdic['rzjmre5'])
        rzjmre10.append(vdic['rzjmre10'])
        rqye.append(vdic['rqye'])
        rqyl.append(vdic['rqyl'])
        rqmcl.append(vdic['rqmcl'])
        rqmcl3.append(vdic['rqmcl3'])
        rqmcl5.append(vdic['rqmcl5'])
        rqmcl10.append(vdic['rqmcl10'])
        rqchl.append(vdic['rqchl'])
        rqchl3.append(vdic['rqchl3'])
        rqchl5.append(vdic['rqchl5'])
        rqchl10.append(vdic['rqchl10'])
        rqjmcl.append(vdic['rqjmcl'])
        rqjmcl3.append(vdic['rqjmcl3'])
        rqjmcl5.append(vdic['rqjmcl5'])
        rqjmcl10.append(vdic['rqjmcl10'])
        rzrqye.append(vdic['rzrqye'])
        rzrqyecz.append(vdic['rzrqyecz'])
        dta_date.append(strtime)

def _unpack(row, kind='td'):
    elts = row.xpath('.//%s' %kind)
    # 根据标签的类型获取数据
    return [val.text_content() for val in elts]
    # 使用列表推导式返回一个列表
def parse_options_data(table):
    rows = table.xpath('.//tr')
    # 以table为当前路径，查找tr标签
    header = _unpack(rows[0], kind='td')
    # 查找th标签作为header
    data = [_unpack(r) for r in rows[1:]]
    # 剩下的行作为data
    return TextParser(data, names=header).get_chunk()
    # 返回一个DataFrame

def getNewDataAnalyze(uid):
    doc = parse(urlopen('http://data.eastmoney.com/invest/invest/'+uid+'.html'))
    print(doc)
    doc2 =cleaner.clean_html(doc)
    tables =doc2.xpath('//table')
    print(len(tables))
    # tables = doc.xpath('//table')
    # print(len(tables))
    # df = parse_options_data(tables[0])
    # df['FXSCODE']=uid
    # print(df)
    # if str(df[0][0])!='暂无最新跟踪成分股...':
    #     df.to_sql('fxs_stcode', engine, if_exists='append', index=None)

    # df2 = parse_options_data(tables[1])
    # df.to_sql('fxs_stcode',engine,if_exists='append',index=None)
    # print(df2)

def getHistDataAnalyze(uid):
    doc = parse(urlopen('http://data.eastmoney.com/invest/invest/'+uid+'.html'))
    tables = doc.xpath('//table')
    # df = parse_options_data(tables[0])
    df2 = parse_options_data(tables[1])
    # print(df)
    print(df2)


def getFXSData():
    res = requests.get('http://data.eastmoney.com/invest/invest/ajax.aspx?st=0&sr=-1&p=2&ps=50&js=jmJKiDmc&type=all&name=&rt=50225126').text.replace('var jmJKiDmc =', '')
    res01 = demjson.decode(res)
    for i in res01['data']:
        vdic=eval(str(i))
        FxsName.append(vdic['FxsName'].encode('gb18030'))
        Ssjg.append(vdic['Ssjg'])
        FxsCode.append(vdic['FxsCode'])
        NewIndex.append(vdic['NewIndex'])
        LastYearIndex.append(vdic['LastYearIndex'])
        LastYearSyl.append(vdic['LastYearSyl'])
        Earnings_3.append(vdic['Earnings_3'])
        Earnings_6.append(vdic['Earnings_6'])
        CfgGs.append(vdic['CfgGs'])

def getStock20Data():
    doc = parse(urlopen('http://quote.stockstar.com/Radar/stockperformance_5_2_1_25.html'))
    tables = doc.xpath('//table')
    df =parse_options_data(tables[0])
    print(df)
    df.to_sql('stock20data', engine, if_exists='append', index=None)

if __name__=='__main__':
    getStock20Data()
    # for i in fxsCODE:
    #   print(i)
      #getNewDataAnalyze('11000241246')
#分析师页面的处理
#  getFXSData()
# data5={
# 'FXSNAME':FxsName,
# 'SSJG':Ssjg,
# 'FXSCODE':FxsCode,
# 'NEWINDEX':NewIndex,
# 'LASTYEARINDEX':LastYearIndex,
# 'LASTYEARSYL':LastYearSyl,
# 'EARNINGS_3':Earnings_3,
# 'EARNINGS_6':Earnings_6,
# 'CFGGS':CfgGs,
# }
# df5=pd.DataFrame(data5)
# df5.to_sql('emoney_fxs_ft',engine,if_exists='append',index=None)


#     #沪股通
#     get_sh_sz_Data(vpa['沪股通历史数据'],'var gPehKIxd=')
#     #深股通
#     get_sh_sz_Data(vpa['深股通历史数据'],'var jXZjuJzF=')
# data ={
#    'DetailDate': DetailDate,
#    'LCGCode': LCGCode,
#    'LCG': LCG,
#    'DRCJJME': DRCJJME,
#    'LCGZDF': LCGZDF,
#    'MRCJE': MRCJE,
#    'MCCJE': MCCJE,
#    'LSZJLR': LSZJLR,
#    'DRZJLR': DRZJLR,
#     }
# print(data)
# df =pd.DataFrame(data)
# df.to_sql('emoney_sh_hist',engine,if_exists='append',index=None)
###########################################################################
#     get10_Data(vpa['沪股通十大成交股'],'var wxNtqEYw=','H')
#     get10_Data(vpa['深股通十大成交股'],'var GQtKLRvI=','S')
# data2 ={
#     'CRDT':CRDT,
#    'Name':Name,
#     'Code':Code,
#     'Close':Close,
#     'ChangePercent':ChangePercent,
#     'HGTJME':HGTJME,
#     'HGTMRJE':HGTMRJE,
#     'HGTMCJE':HGTMCJE,
#     'HGTCJJE':HGTCJJE,
#     }
# df2=pd.DataFrame(data2)
# df2.to_sql('emoney_sh10_hist',engine,if_exists='append',index=None)
##########################################################################
# getHGTZFBData(vpa['沪股通涨幅榜'], 'var cuYZQaUl=')
# getHGTZFBData(vpa['深股通涨幅榜'], 'var HLuJtNeH=')
# data3 ={
#     'STCODE':STCODE,
#     'STNAME': STNAME,
#     'STPRICE': STPRICE,
#     'ZFB': ZFB,
#     'HSCRDT': HSCRDT,
# }
# df3 = pd.DataFrame(data3)
# df3.to_sql('emoney_sz_zfb',engine,if_exists='append',index=None)

###########################################################################
# getRZRQData(vpa['融资融券1日'], 'var fKZnOKrI=')
# data4 = {
#     'SCODE': scode,
#     'SNAME': sname,
#     'HFQJG': hfqjg,
#     'TDATE': tdate,
#     'CLOSE': close,
#     'ZDF': zdf,
#     'RZYEZB': rzyezb,
#     'RZYE': rzye,
#     'RZMRE': rzmre,
#     'RZMRE3': rzmre3,
#     'RZMRE5': rzmre5,
#     'RZMRE10': rzmre10,
#     'RZCHE': rzche,
#     'RZCHE3': rzche3,
#     'RZCHE5': rzche5,
#     'RZCHE10': rzche10,
#     'RZJMRE': rzjmre,
#     'RZJMRE3': rzjmre3,
#     'RZJMRE5': rzjmre5,
#     'RZJMRE10': rzjmre10,
#     'RQYE': rqye,
#     'RQYL': rqyl,
#     'RQMCL': rqmcl,
#     'RQMCL3': rqmcl3,
#     'RQMCL5': rqmcl5,
#     'RQMCL10': rqmcl10,
#     'RQCHL': rqchl,
#     'RQCHL3': rqchl3,
#     'RQCHL5': rqchl5,
#     'RQCHL10': rqchl10,
#     'RQJMCL': rqjmcl,
#     'RQJMCL3': rqjmcl3,
#     'RQJMCL5': rqjmcl5,
#     'RQJMCL10': rqjmcl10,
#     'RZRQYE': rzrqye,
#     'RZRQYECZ': rzrqyecz,
#     'CRDT': dta_date,
# }
# df4 = pd.DataFrame(data4)
# df4.to_sql('rzrq_day_dtl', engine, if_exists='append', index=None)