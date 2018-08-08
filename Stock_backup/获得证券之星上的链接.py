from urllib.request import urlopen

from Stock_backup.证券之星_新爬法 import *

#response = requests.get('http://stock.stockstar.com/list/4007.shtml')
aa = parse(urlopen('http://stock.stockstar.com/list/4007.shtml'))
tt = aa.xpath('.//li')

print(tt[42].text_content())
