# -coding:utf8-*-


class Pizza:
    def __init__(self, size):
        self.size = size
    def getsize(self):
        print(self.size)


print(Pizza.getsize)
pizza = Pizza(1)
print(pizza)
print(pizza.__dir__())
print(Pizza)
print(Pizza.getsize)













