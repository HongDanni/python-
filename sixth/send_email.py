# -*-coding:utf8-*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_pass = 'hrqsxpetzchzbhcg'


def send_email(sender, recipients, subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ','.join(recipients)

    maile_server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
    maile_server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
    res = maile_server.send_message(msg, sender, recipients)
    print('res: ', res)
    maile_server.quit()


if __name__ == '__main__':
    response = send_email('462439535@qq.com', ['dannihong96@163.com', '1739402313@qq.com'], 'This is message subject', 'This is a test message')
    print(response)








