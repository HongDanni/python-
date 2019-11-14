# -*-coding:utf8-*-

import time

def fib(n):
    if n < 2:
        return
    fib = 1
    fib_pre = 1
    for num in range(2, n):
        fib_pre, fib = fib, fib+fib_pre
    return fib

def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print('time elapsed for {} is {}s'.format(n, end_time-start_time))
    return result

if __name__ == '__main__':
    n = 77
    print('Fibonacci number for {} is {}'.format(n, profile_me(fib, n)))

