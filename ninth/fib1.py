# -*-coding:utf8-*-
import time


def fib(n):
    if n < 2:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    start_time = time.time()
    fib_sequence = [fib(x) for x in range(1, 30)]
    print(fib_sequence)
    end_time = time.time()

    print(
        "Calculating the list of {} Fibonacci numbers took {} seconds".format(
            len(fib_sequence), end_time-start_time
        )
    )




