# -coding:utf8-*-
from abc import ABCMeta, abstractmethod


class Dog:
    __kind = 'wangcai'  # 私有静态属性

    def get_kind(self):  # 调用私有静态属性
        print('调用私有静态属性：')
        print(Dog.__kind)

    def __func(self):
        print('私有方法：__func()')

    def func(self):
        print('调用私有方法：')
        self.__func()


print(Dog.__dict__)
dog = Dog()
dog.get_kind()
dog.func()
dog._Dog__func()









