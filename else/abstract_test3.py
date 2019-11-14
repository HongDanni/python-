# -coding:utf8-*-
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        print('Payment abstractmethod pay money {}'.format(money))

    @abstractmethod
    def get(self, money):
        print('Payment abstractmethod get money {}'.format(money))

    def total(self, money):
        print('Payment total money {}'.format(money))

    def __int__(self, name):
        print(self)
        self.name = name


class ApplePay(Payment):
    def pay(self, money):
        print('ApplePay pay %d' % money)

    def get(self, money):
        print('ApplePay get %d' % money)

app = Payment('danni')
print(app)
# app.pay(100)
# app.get(200)
# app.total(300)
# app.name = 'niba'
# print(app.name)
















