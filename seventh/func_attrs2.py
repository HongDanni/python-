# -*-coding:utf8-*-


def dummy_decorator(f):
    print('dummy_decorator begin')

    def wrap_f():
        print('wrap_f() begin')
        print('function to be decorated: ', f.__name__)
        print('nested wrapping function: ', f.__name__)
        print('wrap_f() to be end')
        return f()
    wrap_f.__name__ = f.__name__
    wrap_f.__doc__ = f.__doc__
    print('dummy_decorator to be end')
    return wrap_f


@dummy_decorator
def do_nothing():
    print('do_nothing')


if __name__ == '__main__':
    print('wrapped function: ', do_nothing.__name__)
    do_nothing()
