# -coding:utf8-*-
from abc import ABCMeta, abstractmethod


class Room:
    def __init__(self, name, area):
        self.name = name
        self.__area = area  # 私有对象属性

    def getArea(self):
        print('area is {}'.format(self.__area))


room = Room('danni', 90)
print(room.name)
room.getArea()
# print(room.__area)  # 私有对象属性无法调用


