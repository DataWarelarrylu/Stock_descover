import requests
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'username@126.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量
my_user = 'username@chinadrtv.com'  # 收件人邮箱账号，为了后面易于维护，所以写成了变量

def getdata():
   res = requests.get('http://www.cnss.com.cn/caches/task/exponent/bdi/day.json').json()
   return (res['date']+'=='+res['index'])

def mail(varsubject):
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = formataddr(["发件人邮箱昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人邮箱昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = varsubject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.126.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, "password")  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 这句是关闭连接的意思
    except Exception:  # 如果try中的语句没有执行，则会执行下面的ret=False
        ret = False
    return ret

if __name__ =='__main__':
  res =getdata()
  mail(res)
