# -*-coding:utf8-*-
import time
from functools import wraps


def profiling_decorator(f):
    @wraps(f)
    def wrap_f(n):
        start_time = time.time()
        result = f(n)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('time elapsed for n={} is {}s'.format(n, elapsed_time))
        return result
    return wrap_f


@profiling_decorator
def fib(n):
    if n < 2:
        return
    fib_prev = 1
    fib_curr = 1

    for num in range(2, n):
        fib_prev, fib_curr = fib_curr, fib_prev+fib_curr

    return fib_curr


if __name__ == '__main__':
    n = 77
    print("Fibonacci number for n={} :{}".format(n, fib(n)))




