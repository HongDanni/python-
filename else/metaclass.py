# -*-coding:utf8-*-


class Metaclass(type):
    def __new__(cls, name, bases, dct):
        print('HAHAHA')
        dct['a'] = 1
        return type.__new__(cls, name, bases, dct)


print('before Create OBJ')


class OBJ(object):
    __metaclass__ = Metaclass


print('after Create OBJ')

if __name__ == '__main__':
    print(OBJ.a)





