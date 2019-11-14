# -*-coding:utf8-*-
import time

def fib(n):
    start_time = time.time()
    if n < 2:
        return

    fib_prev = 1
    fib = 1

    for num in range(2, n):
        fib_prev, fib = fib, fib + fib_prev


    end_time = time.time()
    print("[time elapsed for n = {}] {}".format(n,end_time-start_time))
    return fib

if __name__ == '__main__':
    n = 77
    print('Fibonacci number {} is {}s'.format(n, fib(n)))