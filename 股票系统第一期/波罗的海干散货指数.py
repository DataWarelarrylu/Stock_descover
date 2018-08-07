import requests
import re
import  time
vtime = '"'+time.strftime('%Y-%m-%d')+'"'
response = requests.get('http://www.96369.net/Indices/77').text
vpa = re.compile('var ddd.*?name.*?波罗的海干散货指数.*?normal.*?data(.*?)]]}];')
print(re.findall(vpa,response)[0])
for i in re.findall(vpa,response)[0].split('],['):
    if i.split(',')[0]=='2017-10-16':
      print(i.split(',')[0],i.split(',')[1])