# -*-coding:utf8-*-
import time


class ProfilingDecorator(object):
    def __init__(self, f):
        print('__init__()ProfilingDecorator')
        self.f = f

    def __call__(self, *args, **kwargs):
        print('__call__()ProfilingDecorator')
        print('start_time')
        start_time = time.time()
        print('result开始')
        result = self.f(*args)
        print('result结束')
        end_time = time.time()
        print('time elapsed for *args={} is {}s'.format(*args, end_time-start_time))
        print('__call__()ProfilingDecorator结束')
        return '***{}***'.format(result)

class ToTHMLDecorator(object):
    def __init__(self, f):
        print('__init__()ToHTMLDecorator')
        self.f = f

    def __call__(self, *args, **kwargs):
        print('__call__()ToHTMLDecorator')
        print('html')
        print('body开始')
        body = self.f(*args)
        print('body结束')
        return "<html><body>{}</body></html>".format(body)



@ToTHMLDecorator
@ProfilingDecorator
def fib(n):
    print('fib()开始')
    if n < 2:
        return
    fib_curr = 1
    fib_prev = 1

    for num in range(2, n):
        fib_prev, fib_curr = fib_curr, fib_curr+fib_prev
    print('fib()结束')
    return fib_curr


if __name__ == '__main__':
    print('__main__')
    n = 77
    print("Fibonacci number for n={} :{}".format(n, fib(n)))