# -*-coding:utf8-*-
import time


def fib_cached1(n, cache):
    if n < 2:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = fib_cached1(n-1, cache) + fib_cached1(n-2, cache)
    return cache[n]


if __name__ == '__main__':
    cache = {}
    start_time = time.time()
    fib_sequence = [fib_cached1(x, cache) for x in range(0, 80)]
    end_time = time.time()
    print(
        'Calculating the list of {} Fibonacci numbers took {} seconds'.format(
            len(fib_sequence), end_time-start_time
        )
    )
    print(fib_sequence)



