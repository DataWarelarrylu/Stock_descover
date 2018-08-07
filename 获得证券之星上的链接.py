from lxml.html import parse
from 证券之星_新爬法 import *
#import requests
from urllib.request import urlopen
#response = requests.get('http://stock.stockstar.com/list/4007.shtml')
aa = parse(urlopen('http://stock.stockstar.com/list/4007.shtml'))
tt = aa.xpath('.//li')

print(tt[42].text_content())
