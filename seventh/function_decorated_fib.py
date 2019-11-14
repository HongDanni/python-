# -*-coding:utf8-*-
import time


def profiling_decorator(f):
    print('profiling_decorator begin')
    def wrapped_f(n):
        print('wrapped_f begin')
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        print('time elapsed for n={} is {}'.format(n, end_time-start_time))
        print('wrapped_f end')
        return result
    print('profiling_decorator end')
    return wrapped_f


@profiling_decorator  # fib = profiling_decorator(fib)
def fib(n):
    print('fib() begin')
    if n < 2:
        return
    fib_curr = 1
    fib_prev = 1
    for num in range(2, n):
        fib_prev, fib_curr = fib_curr, fib_curr+fib_prev
    print('fib() end')
    return fib

if __name__ == '__main__':
    print('__main__')
    n = 77
    print('Fibonacci number for n={} :{}'.format(n, fib(n)))












