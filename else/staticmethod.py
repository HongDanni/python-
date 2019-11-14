# -*-coding:utf8-*-

# staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样

class A:
    def func(self,name):
        print(name)

    def func1(name):
        print(name)

    @staticmethod
    def func2(self,name):
        print(name)

    @staticmethod
    def func3(name):
        print(name)



a = A()
a.func('func')
a.func1()
a.func2(a, 'func2')
a.func3('func3')
print('*'*10)

A.func(A,"safly")
print('*'*10)
A.func1("safly")

print('*'*10)
A.func2(A,"safly")
print('*'*10)
A.func3("safly")

