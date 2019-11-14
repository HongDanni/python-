# -*-coding:utf8-*-
from email.mime.text import MIMEText
import smtplib

# 构造简单纯文本邮件
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

from_addr = '462439535@qq.com'
to_addr = ['1739402313@qq.com']
smtp_server = ''
try:
    smtp_obj = smtplib.SMTP('smtp.qq.com', 587)
    smtp_obj.sendmail(from_addr, to_addr, 'test message')
    print('successfully send email')
except Exception as e:
    print('error:', e)









