from lxml.html import parse
from pandas.io.parsers import TextParser
from urllib.request import urlopen
doc = parse(urlopen('http://quote.stockstar.com/Radar/stockperformance_8.htm'))
# tables = doc.xpath('//table')
# for i in tables[0]:
#     for j in i:
#         for a in j:
#             print(j[a])
#
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

# tables = doc.xpath('.//table')
# df = parse_options_data(tables[0])
# print(df)