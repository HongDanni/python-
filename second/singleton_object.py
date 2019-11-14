# -*-coding:utf8-*-


class SingletonObject(object):
    print('SingletonObject')
    class __SingletonObject():
        print('__SingletonObject')
        def __init__(self):
            print('__SingletonObject::__init__()')
            self.val = None

        def __str__(self):
            print('__SingletonObject::__str__()')
            return "{0!r} *** {1}".format(self, self.val)

        # the rest of the class definition will follow here, as per the previous logging script

    print('instance before')
    instance = None
    print('instance: ', instance)
    print('instance after')

    def __new__(cls):
        print('SingletonObject::__new__()')
        print('SingletonObject::instance: ', SingletonObject.instance)
        if not SingletonObject.instance:
            print('SingletonObject.instance为空')
            SingletonObject.instance = SingletonObject.__SingletonObject()
        return SingletonObject.instance

    def __getattr__(self, name):
        print('SingletonObject::__getattr__()')
        return getattr(self.instance, name)

    def __setattr__(self, name):
        print('SingletonObject::__setattr__()')
        return setattr(self.instance, name)











