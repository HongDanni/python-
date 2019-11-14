# -coding:utf8-*-
from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def open(self):
        print('Base open file {}'.format(self.fName))

    def __int__(self, fName):
        print(self)
        self.fName = fName


class File(Base):
    def open(self):
        print('File open file {}'.format(self.fName))


f = File()
print(f)
f.fName = 'test.json'
f.open()
















