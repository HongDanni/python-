# -*-coding:utf8-*-
from functools import wraps


def dummy_decorator(f):

    @wraps(f)
    def wrap_f():
        print('function to be decorated: ', f.__name__)
        print('nested wrapping function: ', wrap_f.__name__)
        return f()

    return wrap_f


@dummy_decorator
def do_nothing():
    print('do_nothing()')


if __name__ == '__main__':
    print('wrapped function: ', do_nothing.__name__)
    do_nothing()




