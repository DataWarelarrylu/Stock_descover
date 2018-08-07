import requests
import pandas as pd
import csv
import tushare as ts
import os
#下载财务文件
def getST_FIN(stcode):
    r = requests.get('http://quotes.money.163.com/service/zycwzb_'+stcode+'.html?type=year')
    with open(stcode+'zycw.csv', 'wb') as code:
        code.write(r.content)

# 读取文件
def readFile(filename,lie_name,vYear):
    with open(filename, 'r') as csv_file:
        reader =csv.DictReader(csv_file)
        for row in reader:
            if row['报告日期'] ==lie_name:
                return(row[vYear])

def stock_basic_info(date):
    '''获取当前市场所有股票的基本信息'''
    df_basic = ts.get_stock_basics(date='2018-01-25')
    df_basic.reset_index(drop=False,inplace=True)
    df_basic.rename(columns={'code':'代码','name':'股票名称','industry':'所属行业','area':'地区','pe':'市盈率',
                         'outstanding':'流通股本','totals':'总股本','totalAssets':'总资产(万)','liquidAssets':'流动资产',
                         'fixedAssets':'固定资产','reservedPerShare':'每股公积金','timeToMarket':'上市日期',
                        'gpr':'毛利率','npr':'净利润率','holders':'股东人数'},inplace=True)
    df_basic = df_basic.sort_values(by='代码')
    df_basic.drop([df_basic.columns[0]],axis=1,inplace=True)
    df_basic.to_excel(writer, sheet_name='basic2017')

def finance_data(year,quarter):
    sep = '_'
    sheet_suffix=sep.join([str(year),str(quarter)])

    '''按年度、季度获取业绩报表数据'''
    df_report = ts.get_report_data(year=2017,quarter=4)
    df_report.drop_duplicates(inplace=True)
    df_report.reset_index(drop=False,inplace=True)
    df_report.rename(columns={'code':'代码','name':'股票名称','eps':'每股收益','eps_yoy':'每股收益同比(%)',
                        'bvps':'每股净资产','roe':'净资产收益率','epcf':'每股现金流量(元)','net_profits':'净利润(万元)',
                        'profits_yoy':'净利润同比(%)','distrib':'分配方案','report_date':'发布日期'},inplace=True)
    df_report = df_report.sort_values(by='代码')
    df_report.drop([df_report.columns[0]],axis=1,inplace=True)
    df_report.to_excel(writer,sheet_name=sep.join(['report',sheet_suffix]))
    print("完成获取业绩报表数据\n")

    '''按年度，季度获取盈利能力数据'''
    df_profit = ts.get_profit_data(year=2017,quarter=4)
    df_profit.reset_index(drop=False,inplace=True)
    df_profit.rename(columns={'code':'代码','name':'股票名称','roe':'净资产收益率','net_profit_ratio':'净利润率(%)',
                          'gross_profit_rate':'毛利率(%)','net_profits':'净利润','eps':'每股收益',
                          'business_income':'营业收入(百万元)','bips':'每股主营业务收入(元)'},inplace=True)
    df_profit = df_profit.sort_values(by='代码')
    df_profit.drop([df_profit.columns[0]], axis=1, inplace=True)
    df_profit.to_excel(writer,sheet_name=sep.join(['profit',sheet_suffix]))
    print("完成获取盈利能力数据\n")

    '''按年度、季度获取营运能力数据'''
    df_operation = ts.get_operation_data(year=2017,quarter=4)
    df_operation.reset_index(drop=False,inplace=True)
    df_operation.rename(columns={'code':'代码','name':'股票名称','arturnover':'应收账款周转率(次)','arturndays':'应收账款周转天数(天)',
                             'inventory_turnover':'存货周转率(次)','inventory_days':'存货周转天数(天)','currentasset_turnover':'流动资产周转率',
                             'currentasset_days':'流动资产周转天数(天)'},inplace=True)
    df_operation = df_operation.sort_values(by='代码')
    df_operation.drop([df_operation.columns[0]], axis=1, inplace=True)
    df_operation.to_excel(writer,sheet_name=sep.join(['operation',sheet_suffix]))
    print("完成获取营运能力数据\n")

    '''按年度、季度获取成长能力数据'''
    df_growth = ts.get_growth_data(year=2017,quarter=4)
    df_growth.reset_index(drop=False,inplace=True)
    df_growth.rename(columns={'code':'代码','name':'股票名称','mbrg':'主营业务收入增长率(%)','nprg':'净利润增长率','nav':'净资产增长率',
                 'targ':'总资产增长率','epsg':'每股收益增长率','seg':'股东权益增长率'},inplace=True)
    df_growth = df_growth.sort_values(by='代码')
    df_growth.drop([df_growth.columns[0]], axis=1, inplace=True)
    df_growth.to_excel(writer,sheet_name=sep.join(['growth',sheet_suffix]))
    print("完成获取成长能力数据\n")

    '''按年度、季度获取偿债能力数据'''
    df_debtpaying = ts.get_debtpaying_data(year=2017,quarter=4)
    df_debtpaying.reset_index(drop=False,inplace=True)
    df_debtpaying.rename(columns={'code':'代码','name':'股票名称','currentratio':'流动比率','quickratio':'速动比率','cashratio':'现金比率',
                              'icratio':'利息支付倍数','sheqratio':'股东权益比率','adratio':'股东权益增长率'},inplace=True)
    df_debtpaying = df_debtpaying.sort_values(by='代码')
    df_debtpaying.drop([df_debtpaying.columns[0]], axis=1, inplace=True)
    df_debtpaying.to_excel(writer,sheet_name=sep.join(['debtpaying',sheet_suffix]))
    print("完成获取偿债能力数据\n")

    '''按年度、季度获取现金流量数据'''
    df_cashflow = ts.get_cashflow_data(year=2017,quarter=4)
    df_cashflow.reset_index(drop=False,inplace=True)
    df_cashflow.rename(columns={'code':'代码','name':'股票名称','cf_sales':'经营现金净流量对销售收入比率','rateofreturn':'资产的经营现金流量回报率',
                            'cf_nm':'经营现金净流量与净利润的比率','cf_liabilities':'经营现金净流量对负债比率',
                            'cashflowratio':'现金流量比率'},inplace=True)
    df_cashflow = df_cashflow.sort_values(by='代码')
    df_cashflow.drop([df_cashflow.columns[0]], axis=1, inplace=True)
    df_cashflow.to_excel(writer,sheet_name=sep.join(['cashflow',sheet_suffix]))
    print("完成获取现金流量数据\n")
    writer.save()
if __name__ =='__main__':
    '''在程序目录下建立report目录，用于放结果'''
    os.makedirs('{}/report'.format(os.getcwd()), exist_ok=True)
    File_Path = '{}/report{}{}'.format(os.getcwd(), os.sep, 'jbm.xlsx')
    print(File_Path)
    writer = pd.ExcelWriter(File_Path)
    writer.save
    # stock_basic_info('2018-1-25')
    # finance_data(2017, 4)
    # getST_FIN('601111')


