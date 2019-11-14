# -*-coding:utf8-*-


def dummy_decorator(f):
    print('dummy_decorator begin')

    def wrap_f():
        print('wrap_f() begin')
        print('function to be decorated: ', f.__name__)
        print('Nested wrapping function: ', wrap_f.__name__)
        print('wrap_f() end')
        return f()
    print('dummy_decorator end')
    return wrap_f


@dummy_decorator  # do_nothing = dummy_decorator(do_nothing)
def do_nothing():
    print('do_nothing()')
    return 'do_nothing() return'


if __name__ == '__main__':
    print('__main__')
    do_nothing()
    print('wrapped_function: ', do_nothing.__name__)  # 被装饰后，do_nothing()发生了变化








