# -*-coding:utf8-*-


class A(object):
    bar = 1

    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static_foo')
        print(A.bar)
        A.foo(A())

    @classmethod
    def class_foo(cls):
        print('class_foo')
        print(cls.bar)
        print(A.bar)
        cls().foo()
        cls.foo(cls())
        cls().static_foo()


if __name__ == '__main__':
    # A.static_foo()
    A.class_foo()





