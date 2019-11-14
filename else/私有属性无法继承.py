# -*-coding:utf8-*-

class A:
    __role = 'roleA'
    def __init__(self, name):
        self.__name = name

    def __func(self):
        print('私有方法：A::__func()')



class B(A):
    def getRole(self):
        print('B::role {}'.format(B.__role))  # 私有属性无法继承




a = A('danni')
print(dir(a))
print('*'*30)
b = B('niba')
print(dir(b))
# print(b.name)














