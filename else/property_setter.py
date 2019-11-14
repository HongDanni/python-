# -*-coding:utf8-*-


class Goods:
    discount = 0.8

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def get_price(self):
        print('@property get_price')
        print(self.price * Goods.discount)

    @get_price.setter
    def get_price(self, new_price):
        print('@get_price.setter get_price')
        self.price = new_price


app = Goods("apple", 10)
print(app.get_price)
print('*'*10)
app.get_price = 20
print(app.get_price)

