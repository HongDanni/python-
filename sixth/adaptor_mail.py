# -*-coding:utf8-*-
import csv
import smtplib
from email.mime.text import MIMEText
from .user_fetcher import UserFetcher


class Mailer(object):
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipients

        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()


class Logger(object):
    def output(self, message):
        print('[Logger]'.format(message))


class LoggerAdaptor(object):
    def __init__(self, what_i_want):
        self.what_i_want = what_i_want

    def send(self, sender, recipients, subject, message):
        log_message = "From: {}\nTo: {}\nSubject: {}\nMessage: {}".format(sender, recipients, subject, message)
        self.what_i_want.output(log_message)

    def __getattr__(self, attr):
        return getattr(self.what_i_want, attr)


if __name__ == '__main__':
    user_fetcher = UserFetcher('users.csv')
    mailer = Mailer()
    mailer.send()





