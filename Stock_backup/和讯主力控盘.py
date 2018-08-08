from lxml.html import parse
from pandas.io.parsers import TextParser
from urllib.request import urlopen
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
def getHistDataAnalyze():
    doc = parse(urlopen('http://stockdata.stock.hexun.com/zlkp/'))
    tables = doc.xpath('//zltable')
    df = parse_options_data(tables[0])
    # df2 = parse_options_data(tables[1])
    print(df)
    # print(df2)

if __name__ == '__main__':
    getHistDataAnalyze()