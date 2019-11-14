# -*-coding:utf8-*-
import csv
import smtplib
from email.mime.text import MIMEText


class Mailer(object):
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipients]

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

if __name__ == '__main__':
    with open('users.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        print(reader)
        users = [row for row in reader]
        print(users)

        mailer = Mailer()
        mailer.send('462439535@qq.com', 'x["email"] for x in users', 'This is your message', 'have a good day')



