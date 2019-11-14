# -*-coding:utf8-*-

# @classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数
# 不管这个方式是从实例调用还是从类调用，它都用第一个参数把类传递过来
#classmethod
#需要使用静态变量，且不需要跟对象相关
class Goods:
    __discount = 0.8

    @classmethod
    def change(cls,newPrice):
        cls.__discount = newPrice
    @classmethod
    def getPrice(cls):
        return cls.__discount

#之前的使用方式
    def change1(self,newPri):
        Goods.__discount = newPri
    def getPrice1(self):
        return Goods.__discount

goods1 = Goods()
goods1.change1(10)
print(goods1.getPrice1())

Goods.change1(Goods,30)
print(Goods.getPrice1(Goods))

Goods.change(20)
print(Goods.getPrice())







