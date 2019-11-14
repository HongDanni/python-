# -coding:utf8-*-
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def talk(self):
        print('Base talk')


class Pig(Base):
    def talk(self):
        print('Pig is talking')


class People(Base):
    def talk(self):
        print('People is talking')


def talk(obj):
    obj.talk()


pig = Pig()
pig.talk()
people = People()
people.talk()

talk(pig)
talk(people)









