# -*-coding:utf8-*-
# 一个静态属性property本质就是实现了get，set，delete三种方法
class Foo:
    def get(self):
        print('get的时候运行我啊')

    def set(self,value):
        print('set的时候运行我啊',value)

    def delet(self):
        print('delete的时候运行我啊')
        #def __init__(self, fget=None, fset=None, fdel=None, doc=None)
    AAA=property(get,set,delet) #内置property三个参数与get,set,delete一一对应

f1=Foo()
f1.AAA
f1.AAA='aaa'
del f1.AAA




