import smtplib
from email.mime.text import MIMEText
from .user_fetcher import UserFetcher


class Mailer(object):
    def send(self, sender, recipients, subject, message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = [recipients]

        s = smtplib.SMTP('localhost')
        s.send_message(recipients)
        s.quit()


if __name__ == '__main__':
    user_fetcher = UserFetcher('users.csv')
    mailer = Mailer()

    mailer.send('462439535@qq.com', [x['email'] for x in user_fetcher.fetch_users()], 'this is your message', 'have a good day')



