# -*-coding:utf8-*-
import time

def fib(n):
    if n < 2:
        return
    fib = 1
    fib_prev = 1

    for number in range(2, n):
        fib_prev, fib = fib, fib+fib_prev
    return fib

def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print("time elapsed for n={} : {}".format(n, end_time-start_time))
    return result

def get_profiled_function(f):
    return lambda n: profile_me(f, n)

if __name__ == '__main__':
    n = 77
    fib_profiled = get_profiled_function(fib)
    print('Fibonacci number for n={} :{}'.format(n, fib_profiled(n)))







