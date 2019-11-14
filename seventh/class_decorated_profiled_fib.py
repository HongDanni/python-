# -*-coding:utf8-*-
import time


class ProfilingDecorator(object):
    def __init__(self, f):
        print('__init__:ProfilingDecorator')
        self.f = f

    def __call__(self, *args, **kwargs):
        print('__call__:ProfilingDecorator')
        start_time = time.time()
        result = self.f(*args)
        end_time = time.time()
        print('time for *args={} is {}'.format(*args, end_time-start_time))
        print('__call__()结束')
        return result


@ProfilingDecorator  # 调用初始化函数：__init__()
def fib(n):
    print('fib(n)开始')
    if n < 2:
        return
    fib = 1
    fib_prev = 1
    for num in range(2, n):
        fib_prev, fib = fib, fib_prev+fib
    print('fib(n)结束')
    return fib


if __name__ == '__main__':
    n = 77
    print('__main__')
    print('Fibonacci number for n={} is {}'.format(n, fib(n)))  # 调用fib()时,会先调用装饰器ProfilingDecorator里的__call__()
